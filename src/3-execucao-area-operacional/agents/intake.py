"""
#21 INTAKE - Triagem
Camada 3 - Área Operacional
Constituição v2.0
"""
import json, hashlib, datetime, pathlib

BASE = pathlib.Path(__file__).parents[2]
EVENT_STORE = BASE / "event_store.json"

def append_event(event_type: str, data: dict):
    store = json.loads(EVENT_STORE.read_text())
    prev_hash = store[-1]["hash"]
    ev = {
        "event": event_type,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "prev_hash": prev_hash,
        "data": data
    }
    ev["hash"] = hashlib.sha256(json.dumps(ev, sort_keys=True).encode()).hexdigest()
    store.append(ev)
    EVENT_STORE.write_text(json.dumps(store, indent=2))
    return ev

if __name__ == "__main__":
    append_event("INTAKE_TRIAGED", {"status": "ok"})
    print("INTAKE ok")
