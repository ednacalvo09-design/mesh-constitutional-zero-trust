class Guardian:
    def __init__(self, constitution, event_store):
        self.constitution = constitution
        self.event_store = event_store
        print("Guardian inicializado")
    def evaluate_and_execute(self, agent_id, action, input_data, output_data):
        print(f"[GUARDIAN] {agent_id} -> {action}")
        result = self.constitution.validate(action, input_data)
        self.event_store.append_event("GOVERNANCE_PROPOSAL_EVALUATED", {"agent_id": agent_id, "action": action, "allowed": result["allowed"], "violations": result["violations"]})
        if not result["allowed"]:
            print(f"[BLOQUEADO pela Constituição] {result['violations']}")
            return False
        print("[APROVADO]")
        return True
