import os
import sys
from django.core.handlers.wsgi import WSGIHandler

# Add Django project to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_django_app.settings')

# Create WSGI application
application = WSGIHandler()

def handler(request):
    """Handle requests via Vercel serverless"""
    from django.http import HttpRequest, HttpResponse
    from io import BytesIO
    
    # Convert Vercel request to Django request
    django_request = HttpRequest()
    django_request.path = request.path
    django_request.method = request.method
    django_request.body = BytesIO(request.body)
    
    # Process via Django
    response = application.get_response(django_request)
    
    # Convert Django response to Vercel response
    return {
        'statusCode': response.status_code,
        'headers': dict(response.items()),
        'body': response.content.decode('utf-8')
    }