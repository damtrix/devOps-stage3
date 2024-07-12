from celery import Celery

def make_celery(app_name=__name__):
    return Celery(app_name, broker='pyamqp://guest@localhost//')

celery = make_celery()
celery.conf.update(result_backend='rpc://')