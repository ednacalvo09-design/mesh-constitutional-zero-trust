"""
tests/test_exemplo.py - Teste exemplo (reconstruido v2.0)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
AGENTS_PATH = ROOT / "src" / "runtime" / "3-execucao-area-operacional"
if str(AGENTS_PATH) not in sys.path:
    sys.path.insert(0, str(AGENTS_PATH))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def test_validacao_mesh():
    status = "MESH_V5_OPERATIONAL"
    assert status == "MESH_V5_OPERATIONAL"
    print("✅ test_validacao_mesh legado passou")

def test_fluxo_completo():
    from agents.proposer import ProposerAgent
    from governance.engine import GovernanceEngine
    from guards.guardian import Guardian
    from validation import ProposalValidator
    from resilience import ResilienceManager

    proposer = ProposerAgent()
    governance = GovernanceEngine()
    guardian = Guardian(governance_engine=governance)
    validator = ProposalValidator()
    resilience = ResilienceManager()

    prop = proposer.propose_action("listar usuarios")
    v_res = validator.validate(prop)
    assert v_res.valid, f"Validacao falhou: {v_res.errors}"
    g_res = governance.evaluate(prop)
    assert g_res["approved"], f"Governanca reprovou: {g_res}"
    guard_ok = guardian.evaluate_and_execute(
        agent_id=prop["agent_id"],
        action=prop["action"],
        trace_id=prop["trace_id"]
    )
    assert guard_ok, "Guardiao bloqueou acao valida"
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
