# MESH — 5-referencia-qualidade-memoria / docs
### Constituição Zero-Trust — Documentação Evolutiva

**Regra combinada e corrigida (30/08/2026):**
> **Constituição (`constitution/`) = EVOLUTIVA, organismo vivo**
> **Histórico (`event_store` / `mesh_events.json`) = IMUTÁVEL, hash-chained, append-only**
> **Executor = zero-trust (não valida a própria proposta)**

---

## Estrutura dos 5 Módulos — runtime/

```
src/runtime/
├── 1-fundacao-alicerce/
│   ├── constitution/
│   │   └── __init__.py          → Constitution evolutiva
│   │       - bloqueia: destruir, deletar, drop, rm -rf /, DROP DATABASE
│   │       - retorna: CONSTITUTIONALLY_VALID / REJECTED_BY_CONSTITUTION
│   ├── core/
│   │   ├── event_store.py       → IMUTÁVEL, hash-chain
│   │   ├── executor.py          → zero-trust
│   │   ├── invariants.py        → exige trace_id + bloqueios críticos
│   │   └── history.py
│   └── data/
│       └── mesh_events.json     → histórico imutável persistido
│
├── 2-comunicacao-sistema-nervoso/
│   ├── bridge/__init__.py       → Ponte: Constituição → Executor → EventStore
│   ├── bus/__init__.py          → EventBus.publish() já grava no imutável
│   ├── protocols/__init__.py
│   └── orchestrator/
│       ├── mesh.py              → MeshOrchestrator (maestro)
│       └── __init__.py
│
├── 3-execucao-area-operacional/
│   ├── agents/
│   │   ├── __init__.py          → BaseAgent + Proposal (trace_id 8 chars)
│   │   └── proposer.py          → ProposerAgent.propose_action()
│   ├── resilience/__init__.py   → ResilienceManager + @with_resilience + circuit_breaker
│   ├── validation/__init__.py   → ProposalValidator + ValidationResult
│   └── scripts/
│       ├── main.py
│       └── run_all_tests.py
│
├── 4-governanca-autorizacao/
│   ├── governance/engine.py     → GovernanceEngine + ConstitutionVerifier (verificador REAL)
│   └── guards/guardian.py       → Guardian.evaluate_and_execute()
│
└── 5-referencia-qualidade-memoria/
    ├── docs/
    │   ├── README.md            → este arquivo
    │   ├── Análise-do-proposer.py-antigo.md → análise versão antiga vs nova
    │   └── Estrutura dos 5 Modulos.md
    └── tests/
        ├── verifier.py          → v2.0 - reexporta de governance.engine
        ├── teste_bloqueio.py    → testa bloqueio "deletar usuarios" vs aprova "listar"
        └── test_exemplo.py      → fluxo completo: proposer→validator→governance→guardian
```

---

## Fluxo Oficial Ponta-a-Ponta

```
1. Proposer.propose_action("listar usuarios")
   → gera Proposal { trace_id, agent_id, action, status=proposed }

2. ProposalValidator.validate(proposal)
   → checa campos obrigatórios: trace_id, agent_id, action

3. GovernanceEngine.evaluate(proposal) / ConstitutionVerifier.verify_proposal()
   → verifica na Constituição EVOLUTIVA

4. Guardian.evaluate_and_execute()
   → se aprovado: executa + registra EXECUTED no EventStore IMUTÁVEL
   → se reprovado: registra REJECTED_BY_CONSTITUTION no EventStore

5. ResilienceManager.retry / circuit_breaker
   → retry com backoff + proteção de circuito

6. EventBus.publish("proposal_executed")
   → notifica subscribers + já gravou no mesh_events.json
```

## Testes de Validação

- **Deve BLOQUEAR:** `deletar usuarios`, `delete_all`, `destruir dados`, `rm -rf /`
- **Deve APROVAR:** `listar usuarios`, `listar usuarios para relatorio`

Rodar:
```bash
python3 src/runtime/3-execucao-area-operacional/scripts/run_all_tests.py
python3 tests/teste_bloqueio.py
python3 tests/test_exemplo.py
```

## Correção de Bugs de Upload (importante)

Se der erro "Ocorreu um erro. Tente novamente" ao arrastar do Finder:
- NÃO arrastar. Usar botão **+ > Carregar arquivos**
- Para .md, preferir copiar e colar o texto direto

---
**Status atual:** Fundação Alicerce 100% + Comunicação 100% + Execução 90% (faltando só recriar este README e o Análise-do-proposer)
Última atualização: 01/09/2026 — Edna Calvo Leite
