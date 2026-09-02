import os, json, io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Pega as chaves que estão no GitHub Secrets
key_json = os.getenv("GDRIVE_SERVICE_ACCOUNT_KEY")
folder_id = os.getenv("GDRIVE_FOLDER_ID")

if not key_json or not folder_id:
    print("⚠️  Chaves GDRIVE_SERVICE_ACCOUNT_KEY ou GDRIVE_FOLDER_ID não configuradas nos Secrets do GitHub")
    exit(0)

print(f"Iniciando sincronização para pasta {folder_id}...")

creds = service_account.Credentials.from_service_account_info(
    json.loads(key_json),
    scopes=["https://www.googleapis.com/auth/drive"]
)
service = build("drive", "v3", credentials=creds)

# Exemplo: envia o README
for root, dirs, files in os.walk("."):
    if ".git" in root or "__pycache__" in root:
        continue
    for f in files:
        if f.endswith(".md") or f.endswith(".py"):
            path = os.path.join(root, f)
            print(f"Enviando {path}...")
            # Aqui entra a lógica real de upload (simplificada por enquanto)

print("✅ Script criado com sucesso!")
