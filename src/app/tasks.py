import celery
import os, sys
import logging
from time import sleep
import random
from celery.signals import after_setup_logger

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.train import Model

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)


@app.task(bind=True)
def train(self, training_parameters=None):
    # State 1
    model = Model()
    self.update_state(state='Loading Training Data')
    self.send_event(type_='task-Loading Training Data')
    model.fetch_data()
    sleep(random.random() * 10)

    # State 2
    self.update_state(state='Feature engineering')
    self.send_event(type_='task-Feature engineering')
    model.feat_eng()
    sleep(random.random() * 10)

    # State 3
    self.update_state(state='Model Fitting')
    self.send_event(type_='task-Model Fitting')
    model.fit(training_parameters)
    sleep(random.random() * 10)

    # State 4
    score = model.evaluate()
    self.update_state(state='Model Evaluation', meta={'F1 score': score})
    self.send_event(type_='task-Model Evaluation')
    sleep(random.random() * 10)


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    logger.addHandler(logging.StreamHandler(sys.stdout))
