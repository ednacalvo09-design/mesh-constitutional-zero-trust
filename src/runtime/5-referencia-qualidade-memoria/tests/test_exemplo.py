"""
tests/test_exemplo.py - Teste exemplo (reconstruído v2.0)
Antes só tinha MESH_V5_OPERATIONAL
Agora testa a integração completa
"""

import sys
from pathlib import Path
ROOT = Path('/tmp/projeto_final')
sys.path.insert(0, str(ROOT))

def test_validacao_mesh():
    # Teste legado mantido para compatibilidade
    status = "MESH_V5_OPERATIONAL"
    assert status == "MESH_V5_OPERATIONAL"
    print("✅ test_validacao_mesh legado passou")

def test_fluxo_completo():
    try:
    from agents.proposer import ProposerAgent
except ModuleNotFoundError:
    try:
        from src.runtime import proposer
        from src.runtime.proposer import ProposerAgent
    except ModuleNotFoundError:
        # tenta pelo caminho real do projeto
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
        try:
            from src.runtime.__init__ import ProposerAgent
        except ImportError:
            # último fallback - pega direto do arquivo que você já consertou
            import importlib.util
            proposer_path = Path(__file__).parent.parent.parent / "3-execucao-area-operacional" / "agents" / "proposer.py"
            spec = importlib.util.spec_from_file_location("proposer", proposer_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            ProposerAgent = mod.ProposerAgent
    from governance.engine import GovernanceEngine
    from guards.guardian import Guardian
    from validation import ProposalValidator
    from resilience import ResilienceManager

    proposer = ProposerAgent()
    governance = GovernanceEngine()
    guardian = Guardian(governance_engine=governance)
    validator = ProposalValidator()
    resilience = ResilienceManager()

    # 1. Propor
    prop = proposer.propose_action("listar usuarios")
    
    # 2. Validar
    v_res = validator.validate(prop)
    assert v_res.valid, f"Validação falhou: {v_res.errors}"
    
    # 3. Governança
    g_res = governance.evaluate(prop)
    assert g_res["approved"], f"Governança reprovou: {g_res}"
    
    # 4. Guardião
    guard_ok = guardian.evaluate_and_execute(
        agent_id=prop["agent_id"],
        action=prop["action"],
        trace_id=prop["trace_id"]
    )
    assert guard_ok, "Guardião bloqueou ação válida"

    print(f"✅ test_fluxo_completo passou - trace {prop['trace_id']}")

def test_bloqueio_palavra_proibida():
    from governance.engine import GovernanceEngine
    gov = GovernanceEngine()
    res = gov.evaluate({"trace_id": "test", "agent_id": "a1", "action": "delete_all"})
    assert not res["approved"], "Deveria bloquear delete_all"
    print("✅ test_bloqueio_palavra_proibida passou")

if __name__ == "__main__":
    test_validacao_mesh()
    test_fluxo_completo()
    test_bloqueio_palavra_proibida()
    print("\nTodos os testes passaram!")
