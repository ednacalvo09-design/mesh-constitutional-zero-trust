<img width="1365" height="768" alt="2" src="https://github.com/user-attachments/assets/86f92e2a-c638-4d86-9fa2-9a0ea06c0733" />

# mesh-constitutional-zero-trust

**Constitution Authority — Constitutional Zero-Trust Multi-Agent System (Autonomous Research Phase)**

This repository serves as the constitutional authority for the MESH project.

* **Source of Truth**: See `CONSTITUICAO-MESH.md` — Contains complete topology, 25 sub-agents (1.1 to 5.8), LangGraph code with nested sub-graphs, and the immutable audit + IEPL mechanism.
* **Golden Rule**: *Learning never grants authority* — External proposer `glm-5` (zai-org/GLM-5 fork) only proposes and never executes without authorization from this constitution.
* **Structure**:
* `CONSTITUICAO-MESH.md` — Complete architectural constitution
* `src/1-fundacao-alicerce/event_store.jsonl` — Immutable audit ledger
* `.github/workflows/mesh-audit.yml` — Chain validation + IEPL check


* **Flow**: `glm-5 (PROPOSER)` ➔ `Proposal Gate` ➔ `Constitution` ➔ `Tool Gateway` ➔ `Event Store`
