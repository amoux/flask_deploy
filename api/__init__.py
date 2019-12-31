import time
from flask import jsonify
from flask_restplus import Api
from flask_restplus import Resource
from tasks import celery
import config

api = Api(prefix=config.APP_PREFIX)


class TaskStatusAPI(Resource):

    def get(self):
        task = celery.AsyncResult(task_id)
        return jsonify(task.result)


class DataProcessingAPI(Resource):

    def post(self):
        task = process_data.delay()
        return {'task_id': task.id}, 200


@celery.task()
def process_data():
    time.sleep(60)


# data preprocessing endpoint.
api.add_resource(DataProcessingAPI, '/process_data')
# task status endpoint.
api.add_resource(TaskStatusAPI, '/tasks/<string:task_id>')
