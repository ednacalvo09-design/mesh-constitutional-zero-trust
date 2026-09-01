"""
tests/verifier.py - Verificador de testes (reconstruído v2.0)
Compatível com governance/engine + guards/guardian + agents/Proposal
"""

from governance.engine import ConstitutionVerifier

# Mantém compatibilidade com import antigo: from tests.verifier import ConstitutionVerifier
# Mas agora aponta para o verificador real da governança

__all__ = ["ConstitutionVerifier"]

# Teste rápido se rodar direto
if __name__ == "__main__":
    v = ConstitutionVerifier()
    print(v.verify_proposal({"trace_id": "abc", "agent_id": "a1", "action": "listar usuarios"}))
    print(v.verify_proposal({"trace_id": "abc", "agent_id": "a1", "action": "deletar usuarios"}))
