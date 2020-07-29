from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, HttpResponse
from mycelery.sms.tasks import send_sms, send_sms2
from datetime import timedelta, datetime


def test(request):
    ############### 异步任务 #################

    # 1. 声明一个和celery一模一样的任务函数，但是我们可以导包来解决
    # send_sms.delay("110")
    # send_sms2.delay("119")
    # send_sms.delay() 如果调用的任务函数没有参数，则不需要填写任何内容

    ############### 定时任务 #################

    ctime = datetime.now()
    # 默认用utc时间
    utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    time_delay = timedelta(seconds=10)
    task_time = utc_ctime + time_delay
    result = send_sms.apply_async(["911", ], eta=task_time)
    print(result.id)

    return HttpResponse('ok')
