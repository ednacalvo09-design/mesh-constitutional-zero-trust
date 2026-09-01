"""
guards/__init__.py - Base dos guardiões (reconstruído)
"""

from dataclasses import dataclass
from typing import Dict, Any, List
import logging

logger = logging.getLogger("guards")

@dataclass
class GuardResult:
    allowed: bool
    agent_id: str
    action: str
    violations: List[str]
    trace_id: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "allowed": self.allowed,
            "agent_id": self.agent_id,
            "action": self.action,
            "violations": self.violations,
            "trace_id": self.trace_id
        }
