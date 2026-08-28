class ProposerAgent:
    """Agente Proponente: responsável por gerar ideias, rascunhos ou propostas de ações."""
    def __init__(self, agent_id: str = "agent_proposer_01"):
        self.agent_id = agent_id

    def propose_action(self, description: str) -> dict:
        """Gera uma proposta de ação para ser validada pelo ecossistema."""
        print(f"🤖 [{self.agent_id}] Gerando proposta...")
        return {
            "agent_id": self.agent_id,
            "action": description,
            "input_data": "dados_brutos_de_entrada_exemplo",
            "output_data": f"resultado_processado_para_{description}"
        }