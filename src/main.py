from mesh.core.constitution import Constitution
from mesh.core.event_store import EventStore
from mesh.core.guardian import Guardian
from mesh.v5.agents.proposer import ProposerAgent

def main():
    print("🚀 Iniciando o Ecossistema MESH v5.0 (Zero-Trust)...")
    
    # 1. Inicializa o Núcleo
    constitution = Constitution(version="v5.0")
    event_store = EventStore()
    guardian = Guardian(constitution=constitution, event_store=event_store)
    
    # 2. Inicializa o Agente Proponente
    proposer = ProposerAgent(agent_id="agent_proposer_01")
    
    # 3. Simula uma ação válida
    print("\n--- Teste 1: Ação Válida ---")
    prop_ok = proposer.propose_action("analisar dados de telemetria")
    guardian.evaluate_and_execute(
        agent_id=prop_ok["agent_id"],
        action=prop_ok["action"],
        input_data=prop_ok["input_data"],
        output_data=prop_ok["output_data"]
    )
    
    # 4. Simula uma ação que viola a constituição (contém "destruir")
    print("\n--- Teste 2: Ação Inválida/Bloqueada ---")
    prop_bad = proposer.propose_action("destruir banco de dados principal")
    guardian.evaluate_and_execute(
        agent_id=prop_bad["agent_id"],
        action=prop_bad["action"],
        input_data=prop_bad["input_data"],
        output_data=prop_bad["output_data"]
    )
    
    print("\n✨ Execução do ecossistema finalizada com sucesso!")

if __name__ == "__main__":
    main()