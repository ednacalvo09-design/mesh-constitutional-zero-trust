[gemini-code-1789359231405.md](https://github.com/user-attachments/files/32179046/gemini-code-1789359231405.md)
# CONSTITUIÇÃO ARQUITETURAL DO MESH
## Projeto: Constitutional Zero-Trust Multi-Agent System (Fase Pesquisa)
**Repositório:** `mesh-constitutional-zero-trust` (Constitution Authority)
**Proposer externo:** `glm-5` (fork zai-org/GLM-5) - fica FORA da pasta mestre

> Princípio de ouro: `Learning never grants authority`. O proposer nunca altera a Constituição diretamente.

---

### 1. VISÃO GERAL E TOPOLOGIA DO GRAFO

O MESH opera como um DAG orquestrado por um Supervisor (Router). Fluxo com barreira sincronizadora:

```mermaid
graph TD
    S[Supervisor / Router] --> A1[Agente 1 - Histórico/Filosófico]
    S --> A2[Agente 2 - Técnico Oficial]
    S --> A3[Agente 3 - Engenharia]

    A1 --> FORK{Fork Barreira}
    A2 --> FORK
    A3 --> FORK

    FORK --> A4[Agente 4 - Acadêmico 2024-2026<br/>8 subagentes]
    FORK --> A5[Agente 5 - Risco/Ética/Auditoria<br/>8 subagentes]

    A4 --> SYN[OUTPUT - Synthesis]
    A5 --> SYN
