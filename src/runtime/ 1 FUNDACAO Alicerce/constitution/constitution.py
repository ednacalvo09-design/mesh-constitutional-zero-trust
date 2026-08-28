"""
MESH — Constituição
Autoridade máxima. Versão limpa para Monterey 12.7.6
"""

class Constitution:
  def __init__(self, version=""):
    self.version = version
    print(f"Constituição {version} carregada - Hardware OK")

  def validate(self, action: str, data: str = "") -> dict:
    texto = f"{action} {data}".lower()
    bloqueadas = ["destruir", "deletar", "excluir", "drop", "apagar banco", "rm -rf /", "format", "delete from"]
    for palavra in bloqueadas:
      if palavra in texto:
        return {"allowed": False, "violations": [f"palavra proibida: {palavra}"], "status": "REJECTED_BY_CONSTITUTION"}
    return {"allowed": True, "violations": [], "status": "CONSTITUTIONALLY_VALID"}