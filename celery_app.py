from celery import Celery
from kombu import Queue
from app import create_app
from config import Config

flask_app = create_app()

celery = Celery(
    "worker",
    include=[
        "app.tasks.Registermessaging_task",
        "app.tasks.heavy_task",
        "app.tasks.send_emailFor_orderPlaced",
        "app.tasks.task_after_payment",
        "app.tasks.app_notification.firebase_notification"
    ]
)
celery.config_from_object(Config)
celery.conf.update(flask_app.config)

# 🔥 DEFINE QUEUES
celery.conf.task_queues = (
    Queue("default"),
    Queue("email_queue"),
    Queue("heavy_queue"),
)

# 🔥 DEFAULT QUEUE
celery.conf.task_default_queue = "default"

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)

celery.Task = ContextTask