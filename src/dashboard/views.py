from django.shortcuts import render
from .models import Visitor


def basicView(request):

    objects = Visitor.objects.all()

    if not objects:
        objects = Visitor()
        objects.save()
        print("I am here")

    context = {"visitors": objects}

    new = Visitor()
    new.save()

    return render(request, "dashboard/main.html", context)
