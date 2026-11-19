import os
from dotenv import load_dotenv

secret_key = "18fd24bf6a2ad4dac04a33963db1c42f"

# Fix 2.3: Secret key will be read from .env instead of this file, which was originally pushed to github
# load_dotenv()
# secret_key = os.environ["FLASK_SECRET_KEY"]