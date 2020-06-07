from django.http import HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
import json

@csrf_exempt 
def publish_or_read_message(request):

    if request.method == 'GET':
        queue = request.GET.get('q', None)

        if queue is None:
            return HttpResponseBadRequest("there is some problem with queue name parameter")


        #1 TODO get info about this queue from metadata service
        #2 TODO handle case if queue is not present
        #  TODO select random server in the cluster
        #3 TODO return all the messages until now, format = timestamp:queue:message in a list format
        #4 TODO handle case of failure in reading message. maybe server is unhealthy and retry

        return HttpResponse("queue:" + queue + "\nmessage:this is the message")

    if request.method == 'POST':

        content = json.loads(request.body.decode())
        queue = content.get('queue', None)

        if queue is None:
            return HttpResponseBadRequest("queue name is required")
        message = content.get('message', '')

        #1 TODO get info about this queue from metadata service
        #2 TODO handle case if queue is not present
        #  TODO select random server in the cluster
        #3 TODO write messages
        #  TODO update offset
        #4 TODO handle case of failure in reading message. maybe server is unhealthy and retry

        return HttpResponse("\nmessage:" + message + "\npublished to queue:" + queue, status=HTTPStatus.CREATED)