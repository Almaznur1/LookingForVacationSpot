from waitress import serve
from where_to_go.wsgi import application
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    serve(application, port='8000')
