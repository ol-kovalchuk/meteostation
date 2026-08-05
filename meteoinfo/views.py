from django.shortcuts import render

from api.models import Reading


def home(request):
    reading = Reading.objects.order_by("-created_at").first()

    return render(
        request,
        "home.html",
        {
            "reading": reading,
        },
    )
