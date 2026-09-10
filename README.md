# mesh-constitutional-zero-trust
**Constitution Authority - Constitutional Zero-Trust Multi-Agent System v1.0 (2026)**

Este repositório é a autoridade constitucional do projeto MESH. 

**Source of Truth:** Ver [CONSTITUICAO-MESH.md](./CONSTITUICAO-MESH.md) - Contém a topologia completa, os 25 subagentes (1.1 a 5.8), o código LangGraph com sub-grafos aninhados e o mecanismo de auditoria imutável + IEPL.

**Regra de Ouro:** `Learning never grants authority` - O proposer `glm-5` (fork externo) só propõe, nunca executa sem autorização desta constituição.

**Estrutura:**
- `CONSTITUICAO-MESH.md` - Constituição arquitetural completa
- `src/1-fundacao-alicerce/event_store.json` - Ledger imutável
- `.github/workflows/mesh-audit.yml` - Validação de cadeia + IEPL

Fluxo: `glm-5 (PROPOSER) -> Proposal Gate -> Constituição -> Tool Gateway -> Event Store`
