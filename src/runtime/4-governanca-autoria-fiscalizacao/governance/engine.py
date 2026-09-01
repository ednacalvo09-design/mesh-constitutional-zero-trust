"""
governance/engine.py - Motor de governança (versão corrigida)
Compatível com agents.Proposal e ecossistema 3-execucao
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    from agents import Proposal
except ImportError:
    # fallback se rodar isolado
    Proposal = dict

from . import GovernanceResult
import logging

logger = logging.getLogger("governance.engine")

class ConstitutionVerifier:
    """Verificador simples de regras constitucionais"""
    def __init__(self):
        self.rules = ["action_not_empty", "agent_id_valid", "no_forbidden_words"]
        self.forbidden = ["delete_all", "shutdown", "rm -rf"]
    
    def verify_proposal(self, proposal) -> GovernanceResult:
        # Extrai dados de dict ou Proposal
        if isinstance(proposal, dict):
            trace_id = proposal.get("trace_id", "unknown")
            action = proposal.get("action", "")
            agent_id = proposal.get("agent_id", "")
        else:
            trace_id = getattr(proposal, "trace_id", "unknown")
            action = getattr(proposal, "action", "")
            agent_id = getattr(proposal, "agent_id", "")
        
        checked = []
        
        # Regra 1: ação não vazia
        checked.append("action_not_empty")
        if not action or len(action.strip()) == 0:
            return GovernanceResult(False, "Ação vazia não permitida", trace_id, rules_checked=checked)
        
        # Regra 2: agent_id válido
        checked.append("agent_id_valid")
        if not agent_id:
            return GovernanceResult(False, "agent_id ausente", trace_id, rules_checked=checked)
        
        # Regra 3: palavras proibidas
        checked.append("no_forbidden_words")
        for word in self.forbidden:
            if word in action.lower():
                return GovernanceResult(False, f"Palavra proibida detectada: {word}", trace_id, rules_checked=checked)
        
        return GovernanceResult(True, "Proposta aprovada pela governança", trace_id, rules_checked=checked)

class GovernanceEngine:
    def __init__(self, event_store=None, storage_path=None):
        self.verifier = ConstitutionVerifier()
        self.event_store = event_store
        self.storage_path = storage_path
        logger.info(f"GovernanceEngine inicializado")

    def evaluate(self, proposal):
        result = self.verifier.verify_proposal(proposal)
        logger.info(f"[{result.trace_id}] Avaliado: {'APROVADO' if result.approved else 'REPROVADO'} - {result.reason}")
        return result.to_dict()

    def process_proposal(self, proposal):
        res = self.evaluate(proposal)
        if self.event_store:
            try:
                self.event_store.append_event("GOVERNANCE_PROPOSAL_EVALUATED", res)
            except Exception as e:
                logger.warning(f"Falha ao salvar no event_store: {e}")
        return res

# Compatibilidade com imports antigos: from mesh.constitution.verifier import ConstitutionVerifier
# Mantemos alias
__all__ = ["GovernanceEngine", "ConstitutionVerifier", "GovernanceResult"]
