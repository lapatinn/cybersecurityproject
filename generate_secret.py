# Fix 2.3.1: Generate cryptographic secret key and write to config.py

from pathlib import Path
import secrets

env_file = Path(".env")

if env_file.exists():
    raise SystemExit(".env on jo olemassa. Sitä ei ylikirjoitettu.")

secret_key = secrets.token_hex(32)
env_file.write_text(f"FLASK_SECRET_KEY={secret_key}\n")
env_file.chmod(0o600)

print("FLASK_SECRET_KEY generoitu tiedostoon .env")