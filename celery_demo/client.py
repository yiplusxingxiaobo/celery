# -*- coding: utf-8 -*-

from celery_app import task1
from celery_app import task2
from celery_app import task3

task1.add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)
task2.mltiply.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)
task3.sub.apply_async(args=[6,3])
print('hello world,this are the celery async task')
