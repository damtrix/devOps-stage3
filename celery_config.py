from celery import Celery

def make_celery(app_name=__name__):
    return Celery(app_name, broker='amqp://guest:guest@localhost:5672')

celery = make_celery()
celery.conf.update(result_backend='rpc://')