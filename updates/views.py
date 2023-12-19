import json
from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from updates.forms import UpdatesForm
from django.core import serializers
from django.urls import reverse
from updates.models import Updates
from book.models import Book
from user.models import Author
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required

@csrf_exempt
def post_update(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user
        author_username = author.username

        update_entry = Updates(title=title, content=content, author=author, author_username=author_username)
        update_entry.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

# @login_required
def get_updates_json(request):
    author_get = Author.objects.get(user=request.user)
    posts = Updates.objects.filter(author = author_get).order_by('-data_added')
    return HttpResponse(serializers.serialize('json', posts), content_type="application/json")

def get_updates_json_all(request):
    posts = Updates.objects.all().order_by('-data_added')
    return HttpResponse(serializers.serialize('json', posts))

def show_updates(request):
    user = request.user
    if user.role == 'AUTHOR':
        return render(request, 'updates.html')
    elif user.role == 'READER':
        return render(request, 'updates_user.html')

def show_json(request):
    data = Updates.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def post_delete(request, pk):
    try:
        posts = Updates.objects.get(id=pk)
        posts.delete()
        return JsonResponse({'message' : 'update deleted'})
    except Updates.DoesNotExist:
        return JsonResponse({'error':'post not exist'})

@csrf_exempt
def create_updates_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        author = Author.objects.get(user=request.user)

        new_update = Updates.objects.create(
            author = Author.objects.get(user=request.user),
            author_username = author.username,
            title = data["title"],
            content = data["content"],
            # data_added = data["data_added"]
        )

        new_update.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
