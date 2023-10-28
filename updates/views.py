from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from updates.forms import UpdatesForm
from django.core import serializers
from django.urls import reverse
from updates.models import Updates
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_update(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.author

        update_entry = Updates(title=title, content=content, author=author)
        update_entry.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_updates_json(request):
    posts = Updates.objects.all()
    return HttpResponse(serializers.serialize('json', posts))