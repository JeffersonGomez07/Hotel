# api/index.py
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
from app import app  # importa tu app Flask desde app.py

# Esto hace que tu app sea compatible con Vercel serverless
application = DispatcherMiddleware(Response('Not Found', status=404), {
    '/': app
})