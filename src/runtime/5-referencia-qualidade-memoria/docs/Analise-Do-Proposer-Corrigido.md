# Análise-do-proposer.py-antigo.md
### Comparação: versão antiga vs versão nova — MESH v5

**Data da análise:** 30/08/2026 — após bug de internet
**Local:** `3-execucao-area-operacional/agents/proposer.py`

---

## Versão Antiga (que você reenviou)

```python
class ProposerAgent:
  def propose_action(self, description: str) -> dict:
    return {
      "agent_id": self.agent_id,
      "action": description,
      "input_data": "dados_brutos_de_entrada_exemplo",
      "output_data": f"resultado_processado_para_{description}"
    }
```

**Problemas identificados:**

1.  **Não herda de BaseAgent:** No ecossistema atual, todo agent herda de `BaseAgent` definido em `agents/__init__.py`. Esse aqui é isolado.

2.  **Sem validação:** Retorna `input_data` e `output_data` hardcoded. Não gera `trace_id`, `status`, `timestamp`.

3.  **Sem integração com governance:** Não passa por `ProposalValidator` (validation/), `GovernanceEngine` (governance/) e `Guardian` (guards/).

4.  **Sem async / logging:** Versão nova usa `async propose`, `logger` e padrão formal de Proposal.

5.  **Incompatível com Constitution evolutiva:** Não verifica palavras proibidas (`destruir, deletar, drop, rm -rf /`).

---

## Versão Nova (reconstruída v2.0) — Compatível com ecossistema 3-execucao + guards + governance + resilience

```python
"""
agents/proposer.py - Proposer v2.0
Compatível com BaseAgent + Proposal + governance + validation + resilience
"""
from agents import BaseAgent, Proposal
from validation import ProposalValidator
from governance.engine import GovernanceEngine
from guards.guardian import Guardian
from resilience import with_resilience
import logging

logger = logging.getLogger("proposer")

class ProposerAgent(BaseAgent):
    def __init__(self, agent_id="agent_proposer_01"):
        super().__init__(agent_id=agent_id)
        self.validator = ProposalValidator()
        self.governance = GovernanceEngine()
        self.guardian = Guardian(governance_engine=self.governance)

    @with_resilience(max_retries=3, backoff=0.5)
    def propose_action(self, action: str, input_data=None):
        # 1. Cria Proposal formal com trace_id de 8 chars
        proposal = self.create_proposal(action=action, input_data=input_data)
        
        # 2. Valida schema
        v_result = self.validator.validate(proposal)
        if not v_result.valid:
            logger.warning(f"[Proposer] Validação falhou: {v_result.errors}")
            return v_result.to_dict()
        
        # 3. Avalia na governança
        g_result = self.governance.evaluate(proposal.to_dict())
        if not g_result.get("approved"):
            logger.warning(f"[Proposer] Reprovado pela Constituição: {g_result}")
        
        logger.info(f"[Proposer] Proposta {proposal.trace_id} criada: {action}")
        return proposal.to_dict()
```

**O que a nova versão corrige:**

- Herda de `BaseAgent`, gera `trace_id` automático (8 chars)
- Usa `ProposalValidator` → checa `trace_id, agent_id, action`
- Integra com `GovernanceEngine` → bloqueia `deletar, destruir, delete_all`
- Integra com `Guardian.evaluate_and_execute()` → zero-trust
- Decorator `@with_resilience()` → retry com backoff + circuit breaker
- Log estruturado e compatível com `EventStore` IMUTÁVEL

---

## Estrutura dos 5 Módulos (atualizada)

Ver `README.md` nesta mesma pasta `docs/` para hierarquia completa.
Regra: `Constituição = EVOLUTIVA` | `Histórico = IMUTÁVEL`

**Status:** Proposer antigo arquivado aqui para referência. Usar apenas a v2.0 em produção.
