from celery import Celery
from helpers.config import get_settings


settings = get_settings()

celery_app = Celery(
    "mini_rag",
    broker=settings.Celery_BROKER_URL,
    backend=settings.Celery_RESULT_BACKEND,
)
celery_app.conf.update(
    task_serializer=settings.Celery_TASK_SERIALIZER,
    result_serializer=settings.Celery_TASK_SERIALIZER,
    accept_content=[settings.Celery_TASK_SERIALIZER],
    task_acks_late=settings.CELERY_TASK_ACKS_LATE,
    task_time_limit=settings.Celery_TASK_TIME_LIMIT,
    # Result backend - Store results as JSON for status tracking
    task_ignore_result=False,
    result_expires=3600,
    # Connection pool settings for RabbitMQ
    broker_connection_retry_on_startup=True,
    broker_connection_retry=True,
    broker_connection_max_retries=10,
    # Worker concurrency settings
    # worker_concurrency=settings.CELERY_WORKER_CONCURRENCY,
    worker_cancel_long_running_tasks_on_connection_loss=True,
)

celery_app.conf.task_default_queue = "default"
