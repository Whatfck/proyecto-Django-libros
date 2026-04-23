#!/usr/bin/env python
"""
WSGI config para Vercel
"""
import os
import sys
from pathlib import Path

# Configurar path
project_dir = Path(__file__).resolve().parent / 'proyecto'
sys.path.insert(0, str(project_dir))
sys.path.insert(0, str(project_dir.parent))

# Variables de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

# Setup Django
import django
django.setup()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
