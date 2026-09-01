# **mesh-constitutional-zero-trust**

**Constitutional Multi-Agent Orchestration | Zero-Trust Execution | Immutable Event Memory | A2A Governance**  
mesh-constitutional-zero-trust é uma arquitetura soberana desenvolvida para governar, orquestrar e validar agentes autônomos (A2A) com ênfase absoluta em previsibilidade, segurança e conformidade.

## ---

**What is MESH?**

O **MESH** é uma malha distribuída onde agentes operam sob uma Autoridade Constitucional estrita. Nenhum agente, modelo ou proposta recebe confiança automática (*Zero-Trust*), garantindo que a execução técnica e a tomada de decisões permaneçam rigidamente alinhadas às regras de governança do sistema.

## ---

**Core Principles - Atualizado conforme combinado**

> * **Constitutional Authority (EVOLUTIVA):** A lógica e as decisões dos agentes são subordinadas a diretrizes fundamentais. IMPORTANTE: A Constituição é um organismo vivo. Ela será atualizada, aperfeiçoada e versionada no decorrer do aprimoramento do projeto, para refletir novas regras, aprendizados e evoluções da malha.
> * **Zero-Trust Execution:** Nenhuma entidade ou componente do sistema possui privilégios implícitos. Toda interação, troca de mensagens ou proposta de código passa por validação rigorosa.
> * **Immutable Event Memory (IMUTÁVEL):** O histórico de eventos do sistema é gravado de forma fiel e auditável (append-only e hash-chained), preservando a verdade histórica dos fatos sem permitir adulterações retroativas. O que é imutável é o PASSADO. As regras de governança e o código do sistema são totalmente dinâmicos e evolutivos.
> * **Sovereign Runtime:** O código soberano e a infraestrutura local mantêm o controle final das operações, utilizando modelos externos estritamente como auditores ou proponentes.

## ---

**Architecture & Folder Structure - Nova Organização**

A estrutura modular do projeto foi reorganizada fisicamente em `src/runtime/`, separando claramente os domínios de responsabilidade e garantindo total clareza na função de cada "cômodo" da casa. Nomes padronizados em minúsculo com hífen para compatibilidade com Python:

```
mesh-constitutional-zero-trust/
└── src/
    ├── main.py  <- ponto de entrada atualizado para nova organização
    └── runtime/
        ├── 1-fundacao-alicerce/          <- [O Alicerce] Base estrutural, core, dados e histórico fiel
        │   ├── constitution/             <- Diretrizes fundamentais da malha (EVOLUTIVA)
        │   ├── core/                     <- Núcleo de processamento fundamental
        │   ├── data/                     <- Camada de dados e persistência
        │   └── event-store/              <- Registro imutável e fiel de eventos passados (IMUTÁVEL)
        │
        ├── 2-comunicacao-sistema-nervoso/  <- [O Sistema Nervoso] Fluxo, pontes e barramento
        │   ├── bridge/                   <- Conectores e pontes de integração externa
        │   ├── bus/                      <- Barramento de troca de mensagens A2A
        │   └── orchestrator/             <- Orquestrador de fluxo
        │
        ├── 3-execucao-area-operacional/   <- [A Área Operacional] Agentes ativos e execução
        │   ├── agents/                   <- Agentes autônomos (ex: proposer)
        │   └── scripts/                  <- Scripts utilitários
        │
        ├── 4-governanca-autoria-fiscalizacao/ <- [A Autoridade e Fiscalização] Regras dinâmicas
        │   ├── governance/               <- Políticas evolutivas (acompanham a Constituição)
        │   ├── guards/                   <- Barreiras de proteção (guardian)
        │   ├── resilience/               <- Tolerância a falhas
        │   └── validation/               <- Auditoria e conformidade
        │
        └── 5-referencia-qualidade-memoria/ <- [A Memória e Qualidade] Docs e testes
            ├── docs/                     <- Documentação técnica
            └── tests/                    <- Testes automatizados
```

## ---

**Detalhamento da Função de Cada Pasta**

| Macro-Pasta | Função Principal | O Que Pertence Aqui | Regra de Imutabilidade |
| :--- | :--- | :--- | :--- |
| **1-fundacao-alicerce** | Sustenta as bases lógicas e a memória histórica fidedigna. | constitution/ (regras evolutivas), core/, data/ e event-store/ (fatos históricos fiéis) | constitution/ = EVOLUTIVO. event-store/ = IMUTÁVEL |
| **2-comunicacao-sistema-nervoso** | Sistema nervoso que conecta os nós, garantindo fluxo ordenado. | bus, bridge, orchestrator | Evolutivo |
| **3-execucao-area-operacional** | Área operacional onde os agentes realizam o trabalho prático. | agents/, scripts/ | Evolutivo |
| **4-governanca-autoria-fiscalizacao** | Núcleo de fiscalização e controle evolutivo. | governance, guards, resilience, validation | Evolutivo e aperfeiçoável |
| **5-referencia-qualidade-memoria** | Repositório de suporte humano e técnico. | docs/, tests/ | Evolutivo |

*Documentação atualizada em 30/08/2026 para sincronização oficial do repositório mesh-constitutional-zero-trust, garantindo que a Constituição seja evolutiva e o Histórico seja imutável, com total clareza de papéis.*

> **Nota para organização:** Todos os diretórios usam padrão `kebab-case` (minúsculo com hífen) conforme organização realizada no Finder e no Drive, garantindo compatibilidade com `src/runtime/` e `git status clean`.
