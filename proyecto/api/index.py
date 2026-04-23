import os
import sys
import django
from pathlib import Path

# Agregar el directorio padre al path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto.settings")
django.setup()

# Importar la aplicación WSGI
from proyecto.wsgi import application

# Vercel llama a esta función
def handler(request):
    return application(request)
