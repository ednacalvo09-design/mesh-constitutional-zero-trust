"""
validation/__init__.py - Validação de propostas (reconstruído)
Compatível com agents.Proposal + governance + guards
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger("validation")

@dataclass
class ValidationResult:
    valid: bool
    reason: str
    trace_id: str
    errors: List[str] = None

    def __post_init__(self):
        if self.errors is None:
            self.errors = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "valid": self.valid,
            "reason": self.reason,
            "trace_id": self.trace_id,
            "errors": self.errors
        }

class ProposalValidator:
    """Validador de schema e regras básicas da Proposal"""
    def __init__(self):
        self.required_fields = ["trace_id", "agent_id", "action"]

    def validate(self, proposal) -> ValidationResult:
        # Suporta dict ou Proposal
        if isinstance(proposal, dict):
            trace_id = proposal.get("trace_id", "unknown")
            data = proposal
        else:
            trace_id = getattr(proposal, "trace_id", "unknown")
            data = proposal.to_dict() if hasattr(proposal, "to_dict") else proposal.__dict__

        errors = []

        for field in self.required_fields:
            if field not in data or not data[field]:
                errors.append(f"Campo obrigatório ausente: {field}")

        action = data.get("action", "")
        if action and len(action) < 3:
            errors.append("action muito curta")

        if errors:
            return ValidationResult(False, "Validação falhou", trace_id, errors)

        return ValidationResult(True, "Proposta válida", trace_id, [])

def validate_proposal(proposal) -> Dict[str, Any]:
    """Função helper rápida"""
    validator = ProposalValidator()
    return validator.validate(proposal).to_dict()

__all__ = ["ProposalValidator", "ValidationResult", "validate_proposal"]
