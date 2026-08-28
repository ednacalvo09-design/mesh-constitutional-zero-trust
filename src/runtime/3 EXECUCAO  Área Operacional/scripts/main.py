from mesh.v5.constitution.verifier import ConstitutionVerifier
from mesh.v5.governance.engine import GovernanceEngine
from mesh.v5.orchestrator.mesh import MeshOrchestrator

def main():
    print("🚀 Iniciando o Ecossistema MESH v5.0 (Zero-Trust)...")
    print("Constituição v5.0 carregada")
    print("Guardian inicializado\n")

    orchestrator = MeshOrchestrator()

    print("--- Teste 1: Ação Válida ---")
    print("🤖 [agent_proposer_01] Gerando proposta...")
    valid_task = {"trace_id": "trc_main_001", "agent": "agent_proposer_01", "payload": "listar usuarios"}
    res1 = orchestrator.dispatch(valid_task)
    print(f"[GUARDIAN] agent_proposer_01 -> listar usuarios")
    print(f"[APROVADO] listar usuarios\n" if res1["executed"] else f"[BLOQUEADO] {res1['reason']}\n")

    print("--- Teste 2: Ação Inválida/Bloqueada ---")
    print("🤖 [agent_proposer_01] Gerando proposta...")
    invalid_task = {"trace_id": "trc_main_002", "agent": "agent_proposer_01", "payload": "destruir banco de dados principal"}
    res2 = orchestrator.dispatch(invalid_task)
    print(f"[GUARDIAN] agent_proposer_01 -> destruir banco de dados principal")
    print(f"[BLOQUEADO pela Constituição] {res2.get('violations')}" if not res2["executed"] else f"[APROVADO] {invalid_task['payload']}")
    print("\n✨ Execução do ecossistema finalizada com sucesso!")

if __name__ == "__main__":
    main()
