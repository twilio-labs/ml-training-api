# src/app/__init__.py


import json
import falcon
import logging
from celery.result import AsyncResult
import sys
from app.tasks import train

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Ping:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps('pong!')


class CreateTask:

    def on_post(self, req, resp):
        obj = req.get_media(default_when_empty={})
        task = train.delay(training_parameters=obj)
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            }
        }
        resp.body = json.dumps(result)


class CheckStatus:

    def on_get(self, req, resp, task_id):
        task_result = AsyncResult(task_id)
        result = {'status': task_result.status, 'result': task_result.result}
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result)


app = falcon.API()

app.add_route('/ping', Ping())
app.add_route('/create', CreateTask())
app.add_route('/status/{task_id}', CheckStatus())
