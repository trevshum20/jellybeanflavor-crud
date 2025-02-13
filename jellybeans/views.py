from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import JellybeanFlavor


# view for creating a flavor (CREATE)
def addFlavor(request):
    # if request method is POST, process their form submission
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        photoUrl = request.POST.get("photoUrl")

        JellybeanFlavor.objects.create(name=name, description=description, photoUrl=photoUrl)
        
        return redirect('jellybeans')
    
    # if request method is not post, we know they are GETing our html page and haven't filled out
    # or posted the create form
    return render(request, "createFlavor.html")

# view for listing all jelly bean flavors (READ)
def jellybeanFlavorView(request):
    jellyBeanFlavors = JellybeanFlavor.objects.all().order_by('name')
    context = {
        "jellyBeanFlavors" : jellyBeanFlavors,
    }
    return render(request, "jellybeans.html", context)

# view for updating a flavor (Update)
def updateFlavor(request, flavorId):
    flavor = get_object_or_404(JellybeanFlavor, id=flavorId)

    # if request method is POST, process their form submission
    if request.method == "POST":
        flavor.name = request.POST.get("name")
        flavor.description = request.POST.get("description")
        flavor.photoUrl = request.POST.get("photoUrl")

        flavor.save()

        return redirect('jellybeans')
    
    context = {
        "flavor" : flavor,
    }

    # if request method is not post, we know they are GETing our html page and haven't filled out
    # or posted the update form
    return render(request, "updateFlavor.html", context)

# view for deleting a flavor (DELETE)
def deleteFlavor(request, flavorId):
    flavor = get_object_or_404(JellybeanFlavor, id=flavorId)
    flavor.delete()
    
    return redirect('jellybeans')

# view for the about page
def aboutView(request):
    return render(request, "about.html")

# view for AWS Elastic Beanstalk health checks. Simply returns a 200 ok response. Used for app health monitoring
def healthCheck(request):
    return JsonResponse({"status": "ok"}, status=200)
