# mesh-constitutional-zero-trust
mesh-constitutional-zero-trust
MESH Constitutional — 25 agentes: Supervisor Router (Send API) → Fase1 A1,A2,A3 paralelo → Fase2 A4=8 subs CAI + A5=8 subs IEPL + OUTPUT → Synthesis. Constituição Evolutiva vs Histórico Imutável append-only hash-chained. Learning never grants authority.

Constitutional AI [blocked]
Zero-Trust [blocked]
25 Agents [blocked]
LangGraph [blocked]

1. Fundação Imutável
Princípio: Learning never grants authority

Aprendizado nunca concede autoridade automaticamente
Constituição pode evoluir, Histórico nunca muda
Zero-Trust em cada tool call
Fluxo Constitucional:

Proposal Gate → Constitution → Tool Gateway → Event Store
Cada evento carrega constitution_hash + previous_event_hash → verify-immutability

2. Arquitetura 25 Agentes (Corrigido)
Total 25 = 1 Supervisor + 5 principais + 2 consolidate + 16 subs + 1 OUTPUT

Supervisor Router (parallel Send API)
   ├─ Fase 1 (paralelo): A1, A2, A3
   └─ Fase 2 (paralelo): A4(8 subs CAI) + A5(8 subs IEPL) + OUTPUT
        └─ Synthesis → Governance → Guardian → Executor → Event Store
Mapeamento
Agente	Módulo	Função
Supervisor	src/__init__.py	Router Send API + MeshState
A1	1-fundacao-alicerce	Fundação / Proposer
A2	2-comunicacao-sistema-nervoso	Comunicação / Proposer
A3	3-execucao-area-operacional	Execução / Proposer
A4	4-governanca-autoridade-fiscalizacao	Governança + 8 subs CAI
A4.1-8	4-.../subs	Constitutional AI debate
A4.consolidate	4-...	Consolidador acadêmico
A5	5-referencia-qualidade-memoria	Qualidade + 8 subs IEPL
A5.1-8	5-.../subs	Integrated Evaluation Protocol
A5.consolidate	5-...	Consolidador auditoria
OUTPUT	src/__init__.py	Synthesis final
Fase 1 vs Fase 2
Fase 1 — Baixa latência: A1,A2,A3 em paralelo via Supervisor → proposals → Event Store

Fase 2 — Alta qualidade: A4=8 subs paralelos → consolidate (fórum acadêmico) + A5=8 subs paralelos → consolidate (auditoria) + OUTPUT → Governance → Guardian

3. Estrutura Clean Slate (Oficial)
mesh-constitutional-zero-trust/
  src/
    1-fundacao-alicerce/
    2-comunicacao-sistema-nervoso/
    3-execucao-area-operacional/
    4-governanca-autoridade-fiscalizacao/
      subs/ (a4_1..a4_8) + consolidate.py
    5-referencia-qualidade-memoria/
      subs/ (a5_1..a5_8) + consolidate.py
    __init__.py (MeshState 25 + Supervisor + proposer só propõe)
  README.md (este arquivo)
  CLAUDE.md
  SDD-MESH-NOVA-ARQUITETURA.md
Removidos no clean slate: src/runtime/, pastas UPPERCASE, v5.0 no path, READMEs legados.

4. Event Store (Append-Only)
yaml
event:
  id: uuid
  agent: A1 | A4.3 | A5.consolidate | OUTPUT
  phase: Fase1 | Fase2
  constitution_hash: sha256(constitution.yaml)
  previous_event_hash: sha256(prev)
  decision: [APROVADO] | [BLOQUEADO]
  hash: sha256(constitution_hash + previous_hash + payload)
5. Quick Start
bash
git clone https://github.com/ednacalvo09-design/mesh-constitutional-zero-trust
cd mesh-constitutional-zero-trust
python -m src
# Supervisor → Fase1 (A1,A2,A3) → Fase2 (A4,A5,OUTPUT) → Event Store
6. SDD
CLAUDE.md → 3 camadas (Fundação Imutável + Fase Atual 25 + Zero-Trust técnico)
SDD-MESH-NOVA-ARQUITETURA.md → DAG completo + hash-chain + benchmark
Constituição Evolutiva vs Histórico Imutável. Learning never grants authority.
