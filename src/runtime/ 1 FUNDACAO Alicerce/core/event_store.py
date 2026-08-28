from typing import List, Dict, Any
from datetime import datetime

class EventStore:
    def __init__(self):
        self.events: List[Dict[str, Any]] = []

    def append(self, event: Dict[str, Any]):
        event["timestamp"] = datetime.utcnow().isoformat()
        self.events.append(event)

    def get_all(self) -> List[Dict[str, Any]]:
        return self.events
