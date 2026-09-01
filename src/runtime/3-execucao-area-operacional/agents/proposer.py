"""
agents/proposer.py - Versão NOVA (substitui a defasada)
Responsável por gerar propostas formais para o ecossistema.
"""

from . import BaseAgent, Proposal, logger
from typing import Any, Dict

class ProposerAgent(BaseAgent):
    """Agente Proponente: gera ideias, rascunhos e propostas de ações."""

    def __init__(self, agent_id: str = "agent_proposer_01"):
        super().__init__(agent_id=agent_id)

    def propose_action(self, description: str, input_data: Any = None, context: Dict = None) -> Dict:
        """
        Gera uma proposta de ação formal para ser validada.
        Compatível com o código antigo, mas com estrutura nova.
        """
        self.logger.info(f"Gerando proposta: {description}")

        proposal = Proposal(
            agent_id=self.agent_id,
            action=description,
            input_data=input_data or f"dados_brutos_para_{description}",
            output_data=None,
            status="proposed",
            metadata=context or {"source": "proposer", "version": "2.0"}
        )

        # Simula processamento inicial
        proposal.output_data = f"rascunho_processado_para_{description}"
        
        print(f"🤖 [{self.agent_id}] Proposta {proposal.trace_id} gerada -> {description}")
        return proposal.to_dict()

    def execute(self, proposal: Proposal) -> Proposal:
        """Implementação exigida pelo BaseAgent"""
        proposal.status = "proposed"
        proposal.output_data = f"resultado_processado_para_{proposal.action}"
        return proposal

# Compatibilidade com código que importa direto
def get_proposer():
    return ProposerAgent()
