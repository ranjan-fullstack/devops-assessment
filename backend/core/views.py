from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Sucessfully Auto Deployment done by CI CD with AWS working fine!"})

    

