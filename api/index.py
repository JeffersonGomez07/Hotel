from app import app  # Importa tu app Flask desde app/__init__.py

# Vercel Serverless Function necesita exponer la app como 'application'
application = app
