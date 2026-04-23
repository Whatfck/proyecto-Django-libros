# Archivo de configuración para Vercel
# Este archivo le indica a Vercel cómo ejecutar la aplicación Django

import os
import sys
from pathlib import Path

# Agregar proyecto al path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'proyecto'))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

# Importar WSGI
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
