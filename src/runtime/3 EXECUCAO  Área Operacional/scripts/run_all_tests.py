import sys
import unittest
from pathlib import Path

# Adiciona src/ ao PATH
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from src.mesh.tests.unit.test_constitution import test_constitution
from src.mesh.tests.unit.test_event_store import test_event_store
from src.mesh.tests.unit.test_governance import test_governance
from src.mesh.tests.unit.test_orchestrator import test_orchestrator




def run_suite():
    print("=" * 60)
    print("   MESH v5.0 — BACTERIA GLOBAL DE TESTES DE ARQUITETURA   ")
    print("=" * 60)
    
    print("\n[1/4] Executando Testes Constitucionais...")
    test_constitution()
    
    print("\n[2/4] Executando Testes do Event Store...")
    test_event_store()
    
    print("\n[3/4] Executando Testes de Governança (Proposal Gate)...")
    test_governance_flow()
    
    print("\n[4/4] Executando Testes do Orquestrador Central...")
    test_orchestrator()
    
    print("\n" + "=" * 60)
    print("   🎉 TODOS OS TESTES FORAM APROVADOS COM SUCESSO! 🎉   ")
    print("=" * 60)

if __name__ == "__main__":
    run_suite()
