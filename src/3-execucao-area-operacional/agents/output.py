"""
#25 OUTPUT - Agente Final - Era system_final_consolidate.py
Camada 3 - Área Operacional
Constituição v2.0 - Consolida A3+A4+A5 e fecha ledger
Este arquivo substitui system_final_consolidate.py
"""
import json, hashlib, datetime, pathlib

BASE = pathlib.Path(__file__).parents[2]
EVENT_STORE = BASE / "event_store.json"
A4 = BASE / "data" / "a4_academic"
A5 = BASE / "data" / "a5_risk"
REPORTS = BASE / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

def final_consolidate():
    # 1. Lê nova estrutura v2.0
    a4_files = list(A4.glob("a4_*.json")) if A4.exists() else []
    a5_files = list(A5.glob("a5_*.json")) if A5.exists() else []
    
    # 2. Gera relatório final
    final = {
        "constitution": "v2.0",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "a4_academic_count": len(a4_files),
        "a5_risk_count": len(a5_files),
        "a4_files": [p.name for p in a4_files],
        "a5_files": [p.name for p in a5_files],
        "status": "CONSOLIDATED_25_AGENTS"
    }
    
    # 3. Escreve em reports/
    out_path = REPORTS / f"final_{datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    out_path.write_text(json.dumps(final, indent=2))
    
    # 4. Fecha ledger com hash
    if EVENT_STORE.exists():
        store = json.loads(EVENT_STORE.read_text())
        prev = store[-1]["hash"] if store else "0"*64
        ev = {
            "event": "OUTPUT_FINALIZED",
            "timestamp": final["timestamp"],
            "prev_hash": prev,
            "report": str(out_path)
        }
        ev["hash"] = hashlib.sha256(json.dumps(ev, sort_keys=True).encode()).hexdigest()
        store.append(ev)
        EVENT_STORE.write_text(json.dumps(store, indent=2))
    
    return final

if __name__ == "__main__":
    print(json.dumps(final_consolidate(), indent=2))
