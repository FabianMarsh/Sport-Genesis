from django.shortcuts import render
from .models import Subscriptions


def all_subscriptions(request):
    """ A view to show all subscriptions """

    subscriptions = Subscriptions.objects.all()

    context = {
        "subscriptions": subscriptions,
    }

    return render(request, "subscriptions/subscriptions.html", context)
