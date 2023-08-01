from waitress import serve
from where_to_go.wsgi import application


if __name__ == '__main__':
    serve(application, port='8000')
