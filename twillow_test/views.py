from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import SpeechToText


def save_speech_to_text(request):
    if request.method == "POST":
        text = request.POST.get("text")
        stt = SpeechToText(text=text)
        stt.save()

        # 이제 데이터를 HTML 템플릿에 전달할 수 있습니다.
        return render(request, "my_template.html", {"text": text})

    else:
        return JsonResponse({"error": "Invalid method"}, status=400)
