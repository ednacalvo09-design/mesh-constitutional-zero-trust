"""
MESH — MeshOrchestrator — Orquestrador Principal
Regra combinada:
- Constituição = EVOLUTIVA, aperfeiçoável, versionada
- Histórico (event_store) = IMUTÁVEL, hash-chained, auditável
- Execução = Zero-Trust

Fluxo: Proposta → Constituição → Bridge → Executor → EventStore imutável
"""

from typing import Dict, Any

class MeshOrchestrator:
    def __init__(self, constitution, event_store, executor, bridge=None, bus=None):
        self.constitution = constitution
        self.event_store = event_store
        self.executor = executor
        self.bridge = bridge
        self.bus = bus
        print("🎼 MeshOrchestrator iniciado")
        print(f"   - Constituição: {self.constitution.version} (evolutiva)")
        print(f"   - Histórico: {len(self.event_store.get_all())} eventos (imutável)")

    def submit(self, proposal: Dict[str, Any], proposed_by: str) -> Dict[str, Any]:
        print(f"\n--- Nova proposta: {proposal.get('trace_id')} por {proposed_by} ---")
        
        # Usa Bridge se tiver, senão faz direto
        if self.bridge:
            result = self.bridge.process_proposal(proposal, proposed_by)
        else:
            # 1. Verifica Constituição evolutiva
            check = self.constitution.verify_proposal(proposal)
            if not check.get("approved", False):
                self.event_store.append({
                    "trace_id": proposal.get("trace_id"),
                    "type": "REJECTED",
                    "reason": check.get("reason")
                })
                return check
            
            # 2. Executa zero-trust
            result = self.executor.execute(proposal, proposed_by=proposed_by)
            
            # 3. Registra no imutável
            self.event_store.append({
                "trace_id": proposal.get("trace_id"),
                "type": "EXECUTED",
                "result": result
            })
        
        # 4. Publica no bus se tiver
        if self.bus and result.get("success"):
            self.bus.publish("proposal_executed", proposal)
        
        return result

    def get_constitution_history(self):
        return self.constitution.get_history() if hasattr(self.constitution, 'get_history') else []

    def get_event_history(self):
        return self.event_store.get_all()