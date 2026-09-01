"""
tests/teste_bloqueio.py - Teste de bloqueio (reconstruído v2.0)
Antes importava mesh.core.constitution (defasado)
Agora usa governance + guards + resilience
"""

import sys
from pathlib import Path
ROOT = Path('/tmp/projeto_final')
sys.path.insert(0, str(ROOT))

from governance.engine import GovernanceEngine
from guards.guardian import Guardian

# Simula event_store simples se não tiver
class SimpleStore:
    def append_event(self, tipo, data):
        print(f"[EVENT] {tipo}: {data}")

store = SimpleStore()
governance = GovernanceEngine(event_store=store)
guardian = Guardian(event_store=store, governance_engine=governance)

print("\n--- Teste 3: deletar usuarios (deve BLOQUEAR) ---")
result1 = guardian.evaluate_and_execute(
  agent_id="agent_proposer_01",
  action="deletar usuarios",
  input_data="deletar usuarios da producao",
  output_data={}
)
print(f"Resultado: {'BLOQUEADO ✅' if not result1 else 'APROVADO ❌ (era pra bloquear)'}")

print("\n--- Teste 4: listar usuarios (deve APROVAR) ---")
result2 = guardian.evaluate_and_execute(
  agent_id="agent_proposer_01",
  action="listar usuarios",
  input_data="listar usuarios para relatorio",
  output_data={}
)
print(f"Resultado: {'APROVADO ✅' if result2 else 'BLOQUEADO ❌ (era pra aprovar)'}")

print("\n--- Resumo ---")
print(f"Teste bloqueio: {'PASSOU' if not result1 else 'FALHOU'}")
print(f"Teste aprovação: {'PASSOU' if result2 else 'FALHOU'}")
