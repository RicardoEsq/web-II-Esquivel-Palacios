
from django.http import JsonResponse
from .models import User
import json
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def listUsers(request):
    users = User.objects.all()
    data = {
        "users":users
    }
    print(users)
    return render(request, "users/user_list.html", data)



def createUserView(request):
    return render(request, "users/create.html")


def createUserByFetch(request):
    
    body_unicode = request.body.decode('utf-8')
    body =  json.loads(body_unicode)

    return JsonResponse({
        "NOMBRE_RECIBIDO": body.get("name")
    })


def createUser(request):
    if request.method == "POST":
        try:
            
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            
            name = body_data.get("name")
            email = body_data.get("email")
            age = body_data.get("age")
            rfc = body_data.get("rfc")
            photo = body_data.get("photo")

            
            user = User.objects.create(name=name, email=email, age=age, rfc=rfc, photo=photo)

            
            return JsonResponse({"message": "User created successfully", "status": "success", "user_id": user.id}, status=201)
        except Exception as e:
            return JsonResponse({"message": str(e), "status": "error"}, status=400)

    return JsonResponse({"message": "Invalid request method", "status": "error"}, status=405)

def userDetail(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":  # 👈 Si el usuario envía el formulario...
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.rfc = request.POST.get("rfc")
        user.save()  # 👈 Guardamos los cambios en la base de datos

        return redirect("userDetail", id=user.id)  # 👈 Redirige a la misma página para ver los cambios reflejados.

    return render(request, "users/detail.html", {"user": user})