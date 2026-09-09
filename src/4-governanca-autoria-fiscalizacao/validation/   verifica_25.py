# verifica_25.py - Script simples pra Edna rodar e verificar se fechou os 25 (Monterey 12.7 compativel)
import json
from pathlib import Path

def verifica():
    root = Path(".")
    print("🔍 Verificando MESH Hibrida 25 agentes...\n")
    
    checks = []
    
    # A4
    a4_path = root / "forum" / "A4_academic"
    a4_files = list(a4_path.glob("A4_*.py")) if a4_path.exists() else []
    print(f"A4_academic: {len(a4_files)}/9 arquivos")
    for f in sorted(a4_files): print(f"  ✅ {f.name}")
    checks.append(len(a4_files)==9)
    
    print()
    
    # A5
    a5_path = root / "forum" / "A5_audit"
    a5_files = list(a5_path.glob("A5_*.py")) if a5_path.exists() else []
    # Also check nested
    if len(a5_files)==0 and (a5_path / "A5_audit").exists():
        a5_files = list((a5_path / "A5_audit").glob("A5_*.py"))
    print(f"A5_audit: {len(a5_files)}/9 arquivos")
    for f in sorted(a5_files): print(f"  ✅ {f.name}")
    has_authority = any("authority" in f.name for f in a5_files)
    print(f"  {'✅' if has_authority else '❌'} A5.5 Authority Check presente: {has_authority}")
    checks.append(len(a5_files)==9 and has_authority)
    
    print()
    print(f"Formula: 1 supervisor + 3 Fase1 + {len(a4_files)} A4 + {len(a5_files)} A5 + 1 output + 2 consol = {1+3+len(a4_files)+len(a5_files)+1+2} agentes")
    
    if all(checks):
        print("\n🎉 FASE 2 FÓRUM 18 AGENTES FECHADA! Pronto pra OUTPUT AGENT #25!")
    else:
        print("\n⚠️ Ainda faltam arquivos - verifique A4/A5")

if __name__ == "__main__":
    verifica()
