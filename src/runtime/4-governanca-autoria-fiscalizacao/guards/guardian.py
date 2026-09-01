"""
guards/guardian.py - Guardião (versão corrigida)
Compatível com agents.Proposal + governance/engine
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    from agents import Proposal
    from governance.engine import GovernanceEngine
except ImportError:
    Proposal = dict
    GovernanceEngine = None

from . import GuardResult
import logging

logger = logging.getLogger("guards.guardian")

class Guardian:
    def __init__(self, constitution=None, event_store=None, governance_engine=None):
        # constitution antigo -> agora usa GovernanceEngine
        self.constitution = constitution
        self.event_store = event_store
        self.governance = governance_engine or (GovernanceEngine(event_store=event_store) if GovernanceEngine else None)
        print("Guardian inicializado (v2.0)")
        logger.info("Guardian v2.0 inicializado")

    def evaluate_and_execute(self, agent_id, action, input_data=None, output_data=None, trace_id=""):
        """
        Mantém assinatura antiga (agent_id, action, input_data, output_data)
        mas internamente usa Proposal + GovernanceEngine
        """
        print(f"[GUARDIAN] {agent_id} -> {action}")
        
        # Monta proposta no formato novo
        proposal = {
            "agent_id": agent_id,
            "action": action,
            "input_data": input_data,
            "output_data": output_data,
            "trace_id": trace_id or f"guard-{agent_id[:4]}"
        }
        
        # Valida via governance se disponível
        if self.governance:
            gov_result = self.governance.evaluate(proposal)
            allowed = gov_result.get("approved", False)
            violations = [] if allowed else [gov_result.get("reason", "bloqueado")]
        elif self.constitution and hasattr(self.constitution, "validate"):
            # fallback estrutura antiga
            result = self.constitution.validate(action, input_data)
            allowed = result.get("allowed", False)
            violations = result.get("violations", [])
        else:
            # validação mínima
            allowed = bool(action and "delete_all" not in action)
            violations = [] if allowed else ["ação bloqueada por regra padrão"]

        # Loga evento
        if self.event_store:
            try:
                self.event_store.append_event("GOVERNANCE_PROPOSAL_EVALUATED", {
                    "agent_id": agent_id,
                    "action": action,
                    "allowed": allowed,
                    "violations": violations,
                    "trace_id": proposal["trace_id"]
                })
            except:
                pass

        if not allowed:
            print(f"[BLOQUEADO] {violations}")
            return False
        
        print("[APROVADO]")
        return True

    # Novo método recomendado
    def evaluate_proposal(self, proposal) -> GuardResult:
        """Método novo que aceita Proposal direto"""
        if isinstance(proposal, dict):
            agent_id = proposal.get("agent_id", "unknown")
            action = proposal.get("action", "")
            trace_id = proposal.get("trace_id", "")
        else:
            agent_id = getattr(proposal, "agent_id", "unknown")
            action = getattr(proposal, "action", "")
            trace_id = getattr(proposal, "trace_id", "")

        ok = self.evaluate_and_execute(agent_id, action, trace_id=trace_id)
        return GuardResult(
            allowed=ok,
            agent_id=agent_id,
            action=action,
            violations=[] if ok else ["bloqueado pela governança"],
            trace_id=trace_id
        )
