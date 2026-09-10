# 4-guards/constitution_gate.py - verifica hash
import json, hashlib, pathlib
def verify():
    p = pathlib.Path("src/1-fundacao-alicerce/constitution/constitution.json")
    data = p.read_bytes()
    h = hashlib.sha256(data).hexdigest()
    print(f"constitution sha256: {h}")
    return h
