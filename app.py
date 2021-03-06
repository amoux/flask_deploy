import logging
import os

from flask import Flask

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'starting app in {config.APP_ENV} enviroment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)
    # initialize sqlalchemy
    db.init_app(app)

    # define a hello world page
    @app.route('/')
    def hello_world():
        return "Hello, World!"
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
