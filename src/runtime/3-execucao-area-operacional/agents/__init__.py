"""
agents/__init__.py - Base do ecossistema (reconstruído)
Compatível com 3-execucao-area-o... / agents / scripts
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from datetime import datetime
import uuid
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ecossistema.agents")

@dataclass
class Proposal:
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    agent_id: str = "base"
    action: str = ""
    input_data: Any = None
    output_data: Any = None
    status: str = "proposed"  # proposed | validated | executed | failed
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "agent_id": self.agent_id,
            "action": self.action,
            "input_data": self.input_data,
            "output_data": self.output_data,
            "status": self.status,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }

class BaseAgent(ABC):
    """Classe base para todos os agentes do ecossistema."""
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.logger = logging.getLogger(f"agent.{agent_id}")

    @abstractmethod
    def execute(self, proposal: Proposal) -> Proposal:
        pass

    def validate_input(self, data: Any) -> bool:
        return data is not None
