# MESH Constitutional Zero-Trust — v2.0 (25 Agentes) — Set 2026

> **CONSTITUTION AUTHORITY** — Fonte da Verdade. Este repo AUTORIZA, não propõe.
> Regra de Ouro: **Learning never grants authority.**

---

## CAMADA 1 - FUNDAÇÃO IMUTÁVEL (nunca muda)

### Quem é este repo
- `glm-5` (fork zai-org/GLM-5, fora deste repo) = **PROPOSER** — propõe, não executa
- `mesh-constitutional-zero-trust` (ESTE REPO) = **CONSTITUTION AUTHORITY** — define limites e autoriza
- `tool-gateway` = **EXECUTOR** — único que pode tocar em ferramentas/sistema
- `event-store` = **MEMÓRIA IMUTÁVEL** — tudo registrado com hash-chain em `src/1-fundacao-alicerce/event_store.json`

### Fluxo SDD Obrigatório
```
glm-5 (PROPOSER - fora)
  ↓ propõe (com constitution_hash + previous_event_hash)
Proposal Gate (.github/workflows/mesh-validation.yaml) → bolinha vermelha = proteção
  ↓ proposta válida?
Constitution (ESTE REPO) → autoriza?
  ↓ autorizado?
Tool Gateway (executa)
  ↓
Event Store (event_store.json com hash-chain imutável)
```

### Separação de Papéis Zero-Trust
| Componente | Função | Local |
|---|---|---|
| GLM-5 | Propor | Pasta separada `../glm-5/` |
| Proposal Gate | Validar proposta | `.github/workflows/mesh-validation.yaml` |
| Constitution | Autorizar | `src/1-fundacao-alicerce/constitution/` |
| Tool Gateway | Executar | `src/4-governanca-autorizacao-validacao/guards/` |
| Event Store | Registrar | `src/1-fundacao-alicerce/event_store.json` |

---

## CAMADA 2 - FASE MUTÁVEL (25 Agentes Corrigidos)

### Grafo Oficial — 25 Agentes com Supervisor Paralelo (Send API)

```
                [SUPERVISOR - Router Paralelo]
                          ↓ Send API
    ┌─────────────────────┼─────────────────────┐
    ↓                     ↓                     ↓
[A1] HISTÓRICO      [A2] TÉCNICO         [A3] ENGENHARIA
7 pontes Königsberg  LangGraph Send API   Código produção
    ↓                     ↓                     ↓
┌─────────┐          ┌─────────┐                ↓
↓         ↓          ↓         ↓            [OUTPUT]
[A4] ACADÊMICO  [A5] RISCO/ÉTICA       Consolida final
8 subs +        8 subs +              A3+A4+A5
consolidate     consolidate
paralelo        paralelo
```

**Total 25 = 1 SUPERVISOR + 3 (A1,A2,A3) + 1 A4 + 8 (A4.x) + 1 consolidate A4 + 1 A5 + 8 (A5.x) + 1 consolidate A5 + 1 OUTPUT**

### FASE 1 — Subagentes Isolados (Busca) = A1, A2, A3 em paralelo
- Cada um busca fonte diferente, sem comunicação direta, via Supervisor Send API
- **A1 Historical:** história dos grafos, 7 pontes Königsberg
- **A2 Technical:** spec LangGraph, Send API, context isolamento
- **A3 Engineering:** código produção, scripts
- **Benchmark Fase 1:** Mesma pergunta "O que é IA e o que dizem as fontes?" — mede diversidade + ausência alucinação

### FASE 2 — Fórum com Shared Task List = A4 + A5 + OUTPUT
- **A4 Academic (CAI - Constitutional AI) — 8 subs paralelos:**
  - A4.1 Constitutional Sources
  - A4.2 Principle Extraction
  - A4.3 Critique Formation
  - A4.4 Revision Rules
  - A4.5 Training Data Curation
  - A4.6 Harmlessness Check
  - A4.7 Helpfulness Audit
  - A4.8 Honesty Verification
  - + Consolidate A4 (paralelo)

- **A5 Risk/Ethics (IEPL + Immutable Ledger) — 8 subs paralelos:**
  - A5.1 Risk Taxonomy
  - A5.2 Ethical Principles
  - A5.3 Violation Detection (15 min timeout)
  - A5.4 Bias Audit
  - A5.5 Authority Check (Learning never grants authority)
  - A5.6 Fail-Safe Verification
  - A5.7 Audit Trail Integrity (hash-chain previous_event_hash)
  - A5.8 Immutable Ledger (constitution_hash)
  - + Consolidate A5 (paralelo)

- **OUTPUT:** Consolida tudo (A3+A4+A5)
- **Benchmark Fase 2:** Mesma pergunta + Shared Task List + Communicate — mede se síntese melhora e debate reduziu alucinação

---

## CAMADA 3 - ZERO-TRUST TÉCNICO (Correções DeepSeek)

### MeshState 25 Agentes
```python
class MeshState(TypedDict):
    user_query: str
    constitution_hash: str  # sha256(CONSTITUTION.md) - qual constituição autorizou
    previous_event_hash: str  # hash do evento anterior - ledger imutável
    historical_context: str   # A1
    technical_spec: str       # A2
    engineering_code: str     # A3
    academic_dossier: str     # A4 (8 subs)
    audit_plan: str           # A5 (8 subs)
    final_report: str         # OUTPUT
```

### Event Store Imutável
- Path correto: `src/1-fundacao-alicerce/event_store.json` (não `.mesh/audit_trail.json`)
- Todo evento com `constitution_hash` + `previous_event_hash`
- Verificação: `python -m src.4-governanca-autorizacao-validacao.validation.verify_ledger`

### Estrutura Pastas Corrigida (Clean Slate)
```
mesh-constitutional-zero-trust/
  CONSTITUTION.md
  CLAUDE.md (3 camadas - este arquivo é referência)
  SDD-MESH-NOVA-ARQUITETURA.md (planta completa 25 agentes)
  README.md (este arquivo)
  .github/workflows/
    mesh-validation.yaml (com jq + verify_ledger real + sem git push loop)
  src/
    1-fundacao-alicerce/
      constitution/
      core/base_agent.py (zero-trust)
      data/
      event_store.json (ledger hash-chain)
    2-comunicacao-sistema-nervoso/
      orchestrator/supervisor.py (SUPERVISOR paralelo Send API)
    3-execucao-area-operacional/
      agents/
        __init__.py (zero-trust + MeshState 25)
        proposer.py (só propõe, não executa)
        a1_historical.py, a2_technical.py, a3_engineering.py
        a4_academic/ (a4_1_...a4_8_ + consolidate.py)
        a5_risk/ (a5_1_...a5_8_ + consolidate.py)
        output.py
    4-governanca-autorizacao-validacao/
      guards/ (proposal_gate.py, constitution_gate.py)
      validation/verify_ledger.py
    5-referencia-qualidade-memoria/
      tests/benchmark_fase1.py e benchmark_fase2.py
```
❌ Removido: `src/runtime/` (legado v5) e `src/__init__.py` na raiz do src

---

## O que MUDA e o que NUNCA MUDA

**MUDA de fase para fase:**
- Grafo: Fase 1 = sem aresta comunicação, Fase 2 = com Communicate + Shared Task List
- Funções: Fase 1 = buscar, Fase 2 = debater no fórum
- Parâmetros refletem caráter: Técnico, Histórico/Filosófico, Verificador/Ético

**NUNCA MUDA (imutável na autoridade):**
- Nenhum agente dos 25 pode alterar a Constituição
- Aprendizado pode modificar conhecimento, mas nunca regras de autoridade
- A5.5 Authority Check verifica em todo evento: `Learning never grants authority`

---

## Próximos Passos SDD

1. ✅ README 3 camadas + 25 agentes — FEITO (este arquivo)
2. ✅ CLAUDE.md 3 camadas — FEITO
3. ✅ SDD-MESH-NOVA-ARQUITETURA.md 25 agentes — FEITO
4. ⏳ Ajustar `.github/workflows/mesh-validation.yaml` (jq + verify_ledger real)
5. ⏳ Remover `src/runtime/` legado
6. ⏳ Implementar SUPERVISOR paralelo + 25 agentes
7. ⏳ Rodar benchmark Fase 1 e Fase 2

Referência: Constituição (fonte da verdade) = este repo. Planta local = `SDD-MESH-NOVA-ARQUITETURA.md`
