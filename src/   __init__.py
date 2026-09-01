import sys
import pathlib
import importlib.util

# Adiciona src ao path
SRC_ROOT = pathlib.Path(__file__).parent
RUNTIME_ROOT = SRC_ROOT / "runtime"
sys.path.insert(0, str(SRC_ROOT))
sys.path.insert(0, str(RUNTIME_ROOT))

def load_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# Mapeia seus novos nomes organizados no Finder
# Ajuste aqui se o arquivo estiver em outra subpasta
constitution_path = list(RUNTIME_ROOT.rglob("constitution.py"))[0]
event_store_path = list(RUNTIME_ROOT.rglob("event_store.py"))[0]
guardian_path = list(RUNTIME_ROOT.rglob("guardian.py"))[0]
proposer_path = list(RUNTIME_ROOT.rglob("proposer.py"))[0]

constitution_mod = load_module_from_path("constitution", constitution_path)
event_store_mod = load_module_from_path("event_store", event_store_path)
guardian_mod = load_module_from_path("guardian", guardian_path)
proposer_mod = load_module_from_path("proposer", proposer_path)

Constitution = constitution_mod.Constitution
EventStore = event_store_mod.EventStore
Guardian = guardian_mod.Guardian
ProposerAgent = proposer_mod.ProposerAgent

def main():
    print("🚀 Iniciando o Ecossistema MESH (Zero-Trust)...")
    print(f"📂 Pastas novas encontradas: {[p.name for p in RUNTIME_ROOT.iterdir()]}")

    # 1. Inicializa o Núcleo
    constitution = Constitution(version="v1-fundacao-alicerce")
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
