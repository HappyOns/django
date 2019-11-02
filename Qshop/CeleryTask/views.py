from django.http import HttpResponse
from CeleryTask.tests import add
def get_celery(request):
    x,y=1,2
    add.delay(x,y)
    return HttpResponse('hahah')
