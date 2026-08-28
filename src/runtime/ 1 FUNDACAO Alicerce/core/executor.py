from typing import Dict, Any

class Executor:
    def __init__(self, executor_id: str):
        self.executor_id = executor_id

    def execute(self, proposal: Dict[str, Any], proposed_by: str) -> Dict[str, Any]:
        if proposed_by == self.executor_id:
            return {"success": False, "reason": "Zero-trust: executor nao pode validar propria proposta", "rollout_reward": 0}
        print(f"Executor {self.executor_id} executando: {proposal.get('payload', '')}")
        return {"success": True, "reason": "Executado com zero-trust", "rollout_reward": 1.0}

if __name__ == "__main__":
    print("--- Teste Proposer vs Executor ---")
    exec1 = Executor("executor-35b")
    prop = {"trace_id": "trc_123", "agent": "MasterAgent", "payload": "git status"}
    r1 = exec1.execute(prop, proposed_by="proposer-9b")
    print(f"Teste 1 (valido): {r1}")
    r2 = exec1.execute(prop, proposed_by="executor-35b")
    print(f"Teste 2 (invalido - mesmo ID): {r2}")
