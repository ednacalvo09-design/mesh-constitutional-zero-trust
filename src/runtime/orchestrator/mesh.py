from mesh.governance.engine import GovernanceEngine

class MeshOrchestrator:
    def __init__(self, governance=None):
        self.governance = governance or GovernanceEngine()

    def dispatch(self, task):
        result = self.governance.process_proposal(task)
        approved = result.get("approved", False)
        violations = result.get("violations", [])
        reason = result.get("reason") or (violations[0] if violations else "ok")
        if approved:
            print(f"Tarefa '{task.get('payload')}' executada com sucesso sob o MESH Harness v5.0.")
            return {
                "executed": True,
                "status": result.get("status"),
                "reason": reason,
                "result": result,
                "violations": violations
            }
        else:
            print(f"Tarefa '{task.get('payload')}' BLOQUEADA: {violations}")
            return {
                "executed": False,
                "status": result.get("status"),
                "reason": reason,
                "result": result,
                "violations": violations
            }

Orchestrator = MeshOrchestrator
