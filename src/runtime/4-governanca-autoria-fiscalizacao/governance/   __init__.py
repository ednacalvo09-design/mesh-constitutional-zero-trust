"""
governance/__init__.py - Base de governança (reconstruído)
"""

from dataclasses import dataclass
from typing import Dict, Any, List
from datetime import datetime

@dataclass
class GovernanceResult:
    approved: bool
    reason: str
    trace_id: str
    timestamp: str = ""
    rules_checked: List[str] = None
    
    def __post_init__(self):
        if not self.timestamp:
            from datetime import datetime
            self.timestamp = datetime.now().isoformat()
        if self.rules_checked is None:
            self.rules_checked = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "approved": self.approved,
            "reason": self.reason,
            "trace_id": self.trace_id,
            "timestamp": self.timestamp,
            "rules_checked": self.rules_checked
        }
