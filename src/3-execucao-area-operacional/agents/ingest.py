"""
#22 INGEST - Ingestão a4_1..a4_8 e a5_1..a5_8
Camada 3 - Área Operacional
Constituição v2.0 - Lê data/a4_academic/ e data/a5_risk/
"""
import pathlib
BASE = pathlib.Path(__file__).parents[2]
A4 = BASE / "data" / "a4_academic"
A5 = BASE / "data" / "a5_risk"

def ingest():
    a4_files = sorted(A4.glob("a4_*.json")) if A4.exists() else []
    a5_files = sorted(A5.glob("a5_*.json")) if A5.exists() else []
    return {"a4_count": len(a4_files), "a5_count": len(a5_files), "a4": [p.name for p in a4_files], "a5": [p.name for p in a5_files]}

if __name__ == "__main__":
    print(ingest())
