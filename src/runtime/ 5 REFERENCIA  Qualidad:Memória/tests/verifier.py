class ConstitutionVerifier:
    def __init__(self):
        self.forbidden_words = ["deletar", "destruir", "excluir", "apagar", "drop", "delete", "rm -rf", "format", "sudo rm"]

    def _check(self, text):
        t = (text or "").lower()
        for w in self.forbidden_words:
            if w in t:
                return True, w
        return False, None

    def validate(self, action: str, input_data=None, proposal=None):
        if isinstance(proposal, dict) and not proposal.get("trace_id"):
            return {
                "allowed": False, "approved": False, "executed": False,
                "status": "REJECTED_BY_CONSTITUTION", "valid": False,
                "violations": ["missing trace_id"], "reason": "missing trace_id"
            }
        blocked, word = self._check(action)
        if blocked:
            msg = f"palavra proibida: {word}"
            return {
                "allowed": False, "approved": False, "executed": False,
                "status": "REJECTED_BY_CONSTITUTION", "valid": False,
                "violations": [msg], "reason": msg
            }
        return {
            "allowed": True, "approved": True, "executed": True,
            "status": "CONSTITUTIONALLY_VALID", "valid": True,
            "violations": [], "reason": "ok"
        }

    def verify_proposal(self, proposal):
        if isinstance(proposal, dict):
            action = proposal.get("payload") or proposal.get("action") or str(proposal)
            return self.validate(action, None, proposal)
        return self.validate(str(proposal), None, None)

    def verify(self, *args, **kwargs):
        return self.verify_proposal(kwargs.get("proposal") or (args[0] if args else ""))
