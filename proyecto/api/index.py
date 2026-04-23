import os
import sys
import django
from pathlib import Path

# Setup path
current_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(current_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

# Ensure SECRET_KEY and DEBUG are set
if not os.environ.get('SECRET_KEY'):
    os.environ['SECRET_KEY'] = 'django-insecure-development-key'

os.environ.setdefault('DEBUG', 'False')

django.setup()

from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

wsgi_app = get_wsgi_application()

def application(environ, start_response):
    """WSGI application for Vercel"""
    return wsgi_app(environ, start_response)

# Para Vercel Serverless Functions
def handler(request):
    """Manejo de petición para Vercel"""
    from django.core.handlers.wsgi import WSGIHandler
    
    handler_instance = WSGIHandler()
    
    # Preparar environ desde request de Vercel
    environ = {
        'REQUEST_METHOD': request.get('method', 'GET').upper(),
        'SCRIPT_NAME': '',
        'PATH_INFO': request.get('path', '/'),
        'QUERY_STRING': request.get('queryStringParameters', '') or '',
        'CONTENT_TYPE': request.get('headers', {}).get('content-type', ''),
        'CONTENT_LENGTH': request.get('headers', {}).get('content-length', ''),
        'SERVER_NAME': request.get('headers', {}).get('host', 'localhost').split(':')[0],
        'SERVER_PORT': '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': None,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # Agregar headers
    for key, val in request.get('headers', {}).items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{key}'] = val
    
    response_started = False
    status = None
    response_headers = []
    
    def start_response(status_str, headers):
        nonlocal response_started, status
        response_started = True
        status = int(status_str.split()[0])
        response_headers.extend(headers)
    
    try:
        response = handler_instance(environ, start_response)
        body = b''.join(response)
        
        return {
            'statusCode': status or 200,
            'headers': dict(response_headers),
            'body': body.decode('utf-8') if isinstance(body, bytes) else body
        }
    except Exception as e:
        import traceback
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': f'Error: {str(e)}\n{traceback.format_exc()}'
        }


