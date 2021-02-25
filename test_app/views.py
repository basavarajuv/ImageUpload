from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *


def model_query(request):
    req_id = 2
    query_id = MyModelName.objects.get(id=req_id)
    query_name = MyModelName.objects.filter(name=query_id)
    if query_name.count() > 1:
        res_data = MyModelName.objects.filter(name=query_id).values('id', 'name', 'email').exclude(id=req_id)
    else:
        res_data = 'No duplicates with this id'

    return HttpResponse(res_data)


def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('image uploaded')
    else:
        form = ImageForm()

    return render(request, 'index.html', {'form': form})


def show_images(request):
    res = UploadFiles.objects.all()
    context = {"res": res}

    return render(request, "images.html", context)


from django.db import connection


def test_example(request):
    queries = connection.queries
    print(queries)

    return HttpResponse("success")
