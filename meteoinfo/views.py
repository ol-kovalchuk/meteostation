from django.shortcuts import render
from django.core.paginator import Paginator

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


def all_readings(request):
    readings = Reading.objects.order_by("-created_at")

    paginator = Paginator(readings, 50)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "all.html",
        {
            "page_obj": page_obj,
        },
    )
