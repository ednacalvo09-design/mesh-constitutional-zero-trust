from mesh.constitution.verifier import ConstitutionVerifier
from mesh.event_store.store import EventStore

class GovernanceEngine:
    def __init__(self, event_store=None, storage_path=None):
        self.verifier = ConstitutionVerifier()
        self.event_store = event_store

    def evaluate(self, proposal):
        return self.verifier.verify_proposal(proposal)

    def process_proposal(self, proposal):
        res = self.evaluate(proposal)
        if self.event_store:
            try:
                self.event_store.append_event("GOVERNANCE_PROPOSAL_EVALUATED", res)
            except:
                pass
        return res
