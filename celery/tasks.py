import time
import os
from celery import Celery

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

app = Celery('my_task',broker=broker,backend=backend)




@app.task(name='my_task_demo_add_task')
def add(x,y):
    time.sleep(5)
    return x + y


@app.task(name='my_task_demo_sub_task')
def sub(x,y):
    time.sleep(5)
    return x - y

if __name__ == "__main__":
    os.system('celery worker -A tasks --loglevel=info')
