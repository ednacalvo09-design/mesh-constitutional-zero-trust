import sys
sys.path.insert(0, 'src')
from mesh.core.constitution import Constitution
from mesh.core.event_store import EventStore
from mesh.core.guardian import Guardian

constitution = Constitution(version="v5.0")
store = EventStore()
guardian = Guardian(constitution, store)

print("\n--- Teste 3: deletar usuarios ---")
guardian.evaluate_and_execute(
    agent_id="agent_proposer_01",
    action="deletar usuarios",
    input_data="deletar usuarios da producao",
    output_data={}
)

print("\n--- Teste 4: listar usuarios ---")
guardian.evaluate_and_execute(
    agent_id="agent_proposer_01",
    action="listar usuarios",
    input_data="listar usuarios para relatorio",
    output_data={}
)
