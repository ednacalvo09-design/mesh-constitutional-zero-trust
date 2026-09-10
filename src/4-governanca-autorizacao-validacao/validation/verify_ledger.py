# 4-validation/verify_ledger.py
from guards.constitution_gate import verify
if __name__ == "__main__":
    verify()
    print("ledger ok - event_store deve estar em src/5-referencia-qualidade-memoria/event_store.jsonl")
