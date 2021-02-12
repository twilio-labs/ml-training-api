# ml-training-api
A service for training machine learning models asynchronously

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
