"""
MESH v5.0 - Proposer vs Executor Separation
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from mesh.core.constitutional_authority import ConstitutionVerifier
except ImportError:
    from src.mesh.core.constitutional_authority import ConstitutionVerifier

class Executor:
    def __init__(self, executor_id: str):
        self.executor_id = executor_id
        self.verifier = ConstitutionVerifier()

    def execute(self, proposal: dict, proposed_by: str) -> dict:
        if proposed_by == self.executor_id:
            return {
                "success": False,
                "reason": f"NEGADO: Proposer == Executor ({proposed_by})",
                "rollout_reward": 0
            }
        result = self.verifier.verify_proposal(proposal)
        if not result["approved"]:
            return {"success": False, "reason": result["reason"], "rollout_reward": 0}
        print(f"✓ Executor {self.executor_id} executando: {proposal['payload']}")
        return {"success": True, "reason": "Executado com zero-trust", "rollout_reward": 1.0}

if __name__ == "__main__":
    print("--- Teste Proposer vs Executor ---")
    exec1 = Executor("executor-35b")
    prop = {"trace_id": "trc_123", "agent": "MasterAgent", "payload": "git status"}
    r1 = exec1.execute(prop, proposed_by="proposer-9b")
    print(f"Teste 1 (valido): {r1}")
    r2 = exec1.execute(prop, proposed_by="executor-35b")
    print(f"Teste 2 (invalido - mesmo ID): {r2}")
