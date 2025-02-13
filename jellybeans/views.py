from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import JellybeanFlavor


# Create your views here.
def jellybeanFlavorView(request):
    jellyBeanFlavors = JellybeanFlavor.objects.all().order_by('name')
    context = {
        "jellyBeanFlavors" : jellyBeanFlavors,
    }
    return render(request, "jellybeans.html", context)

def aboutView(request):
    return render(request, "about.html")

def deleteFlavor(request, flavorId):
    flavor = get_object_or_404(JellybeanFlavor, id=flavorId)
    flavor.delete()

    messages.success(request, f'Jellybean "{flavor.name}" was successfully deleted.')
    
    return redirect('jellybeans')

def addFlavor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        photoUrl = request.POST.get("photoUrl")

        JellybeanFlavor.objects.create(name=name, description=description, photoUrl=photoUrl)
        
        return redirect('jellybeans')
        
    return render(request, "createFlavor.html")

def updateFlavor(request, flavorId):
    flavor = get_object_or_404(JellybeanFlavor, id=flavorId)

    if request.method == "POST":
        flavor.name = request.POST.get("name")
        flavor.description = request.POST.get("description")
        flavor.photoUrl = request.POST.get("photoUrl")

        flavor.save()

        return redirect('jellybeans')
    
    context = {
        "flavor" : flavor,
    }

    return render(request, "updateFlavor.html", context)

def healthCheck(request):
    #Returns a simple JSON response to indicate the app is healthy
    return JsonResponse({"status": "ok"}, status=200)
