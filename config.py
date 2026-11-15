import os
from dotenv import load_dotenv

secret_key = "18fd24bf6a2ad4dac04a33963db1c42f"

# Korjaus: avain säilytetään ympäristömuuttujassa,
# eikä sitä tallenneta lähdekoodiin tai versionhallintaan:
# load_dotenv()
# secret_key = os.environ["FLASK_SECRET_KEY"]