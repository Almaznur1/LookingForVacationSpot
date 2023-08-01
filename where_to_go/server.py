from waitress import serve
from where_to_go.wsgi import application
import logging
from where_to_go.settings import WAITRESS_HOST


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    serve(application, host=WAITRESS_HOST, port='8000')
