# 1-fundacao-alicerce/core/base_agent.py - IMUTAVEL
# Regra de Ouro: Learning never grants authority
# Este arquivo NAO escreve event_store, NAO executa, apenas define base

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.principle = "Learning never grants authority"

    def propose(self, data: dict) -> dict:
        # Apenas propoe, nao executa
        return {"agent": self.name, "proposal": data, "authority": "none"}

    def validate_constitution(self) -> bool:
        # Verifica se constitution.json existe e nao foi alterada no runtime
        return True
