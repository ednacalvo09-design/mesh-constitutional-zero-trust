"""
MESH — Constituição
Autoridade máxima EVOLUTIVA do ecossistema.
Versão: v1-fundacao-alicerce | 30/08/2026
Regra combinada: Esta Constituição é um organismo vivo, será atualizada,
aperfeiçoada e versionada no decorrer do projeto. O que é IMUTÁVEL é o
histórico (event_store), não as regras.
"""

class Constitution:
  def __init__(self, version="v1-fundacao-alicerce-evolutiva"):
    self.version = version
    print(f"📜 Constituição {version} carregada - Evolutiva e aperfeiçoável - Hardware OK")

  def validate(self, action: str, data: str = "") -> dict:
    texto = f"{action} {data}".lower()
    bloqueadas = ["destruir", "deletar", "excluir", "drop", "apagar banco", "rm -rf /", "format", "delete from"]
    for palavra in bloqueadas:
      if palavra in texto:
        return {"allowed": False, "violations": [f"palavra proibida: {palavra}"], "status": "REJECTED_BY_CONSTITUTION"}
    return {"allowed": True, "violations": [], "status": "CONSTITUTIONALLY_VALID"}
