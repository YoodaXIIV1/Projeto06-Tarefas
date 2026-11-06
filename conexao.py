import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(Path(__file__).with_name('.env'))
uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
cliente.admin.command('ping')  # verifica se o servidor responde
banco = cliente['laboratorio_python']