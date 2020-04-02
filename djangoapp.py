import sys
sys.path.insert(0, './example_django_app')
from example_django_app import wsgi

app = wsgi.application
