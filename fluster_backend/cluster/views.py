import json
from dropbox.client import DropboxClient
from django.http import HttpResponse
from time import sleep


def launch_clustering(request, token):
    client = DropboxClient(token)
    # Simulate work:
    sleep(3.0)
    return HttpResponse(json.dumps(client.metadata('/')))
