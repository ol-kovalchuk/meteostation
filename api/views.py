import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Reading


@csrf_exempt
def readings(request):
    if request.method == "GET":
        return JsonResponse({"status": "API is alive"})

    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    data = json.loads(request.body)

    reading = Reading.objects.create(
        temperature=data["temperature"],
        humidity=data["humidity"],
    )

    return JsonResponse(
        {
            "message": "Data saved",
            "id": reading.id,
        },
        status=201,
    )


def latest_reading(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET method required"}, status=405)

    reading = Reading.objects.order_by("-created_at").first()

    if reading is None:
        return JsonResponse({"error": "No readings yet"}, status=404)

    return JsonResponse(
        {
            "temperature": reading.temperature,
            "humidity": reading.humidity,
            "created_at": reading.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
