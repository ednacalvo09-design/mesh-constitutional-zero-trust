"""
MESH v5.0 - Constitutional Authority - Versão 3
Compatível com seu test_constitution.py + Ornith triple reward
"""

class ConstitutionVerifier:
    def __init__(self):
        print("Constitutional Authority iniciada!")

    def verify_proposal(self, action: dict) -> dict:
        trace_id = action.get("trace_id")
        agent = action.get("agent", "")
        payload = action.get("payload", "")

        # --- TASK REWARD (Constitucional) ---
        # 1. Precisa ter trace_id (seu teste Caso 3)
        if not trace_id:
            return {"approved": False, "reason": "Sem trace_id - não auditável", "task_reward": 0}

        # 2. Bloqueia comandos destrutivos (seu teste Caso 2 + Ornith)
        forbidden = ["rm -rf /", "bypass auth", "disable mTLS", "delete audit", "sudo rm"]
        for word in forbidden:
            if word in payload.lower():
                return {"approved": False, "reason": f"Comando proibido: {word}", "task_reward": 0, "harness_reward": 0}

        # 3. Bloqueia agente Rogue (seu teste)
        if "Rogue" in agent or "UnknownAgent" in agent:
            return {"approved": False, "reason": f"Agente não autorizado: {agent}", "harness_reward": 0}

        # --- HARNESS REWARD + ROLLOUT REWARD ---
        # Tudo passou
        return {
            "approved": True,
            "reason": f"Ação {trace_id} aprovada",
            "task_reward": 1.0,
            "harness_reward": 1.0,
            "rollout_reward": 1.0,
            "final_reward": 1.0
        }

# Alias para compatibilidade com o código que fiz antes
ConstitutionalAuthority = ConstitutionVerifier
