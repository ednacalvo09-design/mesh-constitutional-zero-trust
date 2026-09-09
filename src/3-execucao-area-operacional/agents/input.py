"""
#20 INPUT - Porta de Entrada
Camada 3 - Área Operacional
Constituição v2.0 - Recebe proposta e inicia event_store
"""
import json, hashlib, datetime, pathlib

BASE = pathlib.Path(__file__).parents[2]
EVENT_STORE = BASE / "event_store.json"
LEDGER = BASE / "data" / "a4_academic"

def init_event_store(proposal_id: str):
    event = {
        "event": "INPUT_RECEIVED",
        "proposal_id": proposal_id,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "prev_hash": "0"*64
    }
    event["hash"] = hashlib.sha256(json.dumps(event, sort_keys=True).encode()).hexdigest()
    EVENT_STORE.write_text(json.dumps([event], indent=2))
    return event

if __name__ == "__main__":
    print("INPUT pronto - conforme README v2.0")
