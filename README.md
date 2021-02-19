# ml-training-api
[![A Twilio Labs Project](https://img.shields.io/static/v1?label=&message=Twilio-Labs&color=F22F46&labelColor=0D122B&logo=twilio&style=flat-square)](https://www.twilio.com/labs)

This is a simple framework of a service for training machine learning models asynchronously.

## Falcon + Celery

Example of how to handle training machine learning models asynchronously with Falcon, Celery, and message queues
![diagram](/diagram.png)

### Quick Start

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to http://localhost:8000/ping to view the app or to http://localhost:5555 to view the Flower dashboard.

Trigger a new task with hyperparameters (optional):

```sh
$ curl -X POST http://localhost:8000/create \
    -d '{"alpha":0.5}' \
    -H "Content-Type: application/json"
```

Check the status:

```sh
$ curl http://localhost:8000/status/<TASK_ID>
```

The [model](https://github.com/twilio-labs/ml-training-api/tree/main/src/model) used in this repo is a general text classficiation model built using td-idf features and naive bayes model. But you can plug in any model of your own choice.

## Let's work together

Everything in this toolkit is released under [Twilio Labs](https://www.twilio.com/docs/labs) and fully open-source. If you find any problems with this, [please file an issue](https://github.com/twilio-labs/ml-training-api/issues) or even create a pull request to work together with us on the toolkit. We would love to hear your ideas and feedback!

## License

MIT
