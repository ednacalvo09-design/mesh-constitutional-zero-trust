"""
MESH — Bridge — Ponte de Comunicação Sistema Nervoso
Regra combinada:
- Constituição (constitution/) = EVOLUTIVA
- Histórico (event_store) = IMUTÁVEL
Esta ponte garante que toda mensagem passe pela Constituição
antes de ir para o Executor, e registre no histórico imutável.
"""

from typing import Dict, Any

class Bridge:
    def __init__(self, constitution, event_store, executor):
        self.constitution = constitution
        self.event_store = event_store
        self.executor = executor
        print("🌉 Bridge iniciada — Constituição evolutiva + histórico imutável")

    def process_proposal(self, proposal: Dict[str, Any], proposed_by: str) -> Dict[str, Any]:
        # 1. Verifica na Constituição evolutiva
        verification = self.constitution.verify_proposal(proposal)
        
        if not verification.get("approved", False):
            # Registra falha no histórico IMUTÁVEL
            self.event_store.append({
                "trace_id": proposal.get("trace_id"),
                "type": "REJECTED_BY_CONSTITUTION",
                "proposal": proposal,
                "reason": verification.get("reason")
            })
            return verification

        # 2. Executa com zero-trust
        result = self.executor.execute(proposal, proposed_by=proposed_by)
        
        # 3. Registra sucesso no histórico IMUTÁVEL
        self.event_store.append({
            "trace_id": proposal.get("trace_id"),
            "type": "EXECUTED",
            "proposal": proposal,
            "result": result
        })
        
        return result