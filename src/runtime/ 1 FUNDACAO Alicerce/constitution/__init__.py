class Constitution:
    def __init__(self, version="v5.0"):
        self.version = version
        print(f"Constituição {version} carregada")
    
    def validate(self, action, data):
        texto = f"{action} {data}".lower()
        bloqueadas = ["destruir", "deletar", "excluir", "drop", "apagar banco"]
        for palavra in bloqueadas:
            if palavra in texto:
                return {"allowed": False, "violations": [f"palavra proibida: {palavra}"]}
        return {"allowed": True, "violations": []}

ConstitutionVerifier = Constitution
