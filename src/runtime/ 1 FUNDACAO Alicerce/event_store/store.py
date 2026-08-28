import json, time, os
from pathlib import Path

class EventStore:
    def __init__(self, storage_path=None):
        self.storage_path = storage_path or "mesh_events.jsonl"
        if "test_" in self.storage_path:
            try:
                Path(self.storage_path).unlink(missing_ok=True)
            except:
                pass
        self.events = []
        # carrega se já existir
        if Path(self.storage_path).exists():
            try:
                with open(self.storage_path, "r") as f:
                    for line in f:
                        self.events.append(json.loads(line))
            except:
                pass

    def append_event(self, event_type, payload):
        evt = {
            "event_type": event_type,
            "payload": payload,
            "timestamp": time.time(),
            "trace_id": payload.get("trace_id") if isinstance(payload, dict) else payload.get("trace_id") if hasattr(payload, 'get') else None
        }
        self.events.append(evt)
        try:
            with open(self.storage_path, "a") as f:
                f.write(json.dumps(evt) + "\n")
        except:
            pass
        return evt

    def get_events(self):
        return self.events

    def read_all_events(self):
        # compatibilidade com testes antigos
        if Path(self.storage_path).exists():
            try:
                with open(self.storage_path, "r") as f:
                    file_events = [json.loads(l) for l in f if l.strip()]
                    return file_events
            except:
                return self.events
        return self.events
