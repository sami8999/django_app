from django.shortcuts import render
from django.http import JsonResponse

from .models import Cat 
import json
from django.views.decorators.csrf import csrf_exempt

def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })


@csrf_exempt
def cats(request):
    
    """
    View that handles both GET and POST requests. 

    - For GET requests, it retrieves all cat records from the database and
      returns them in JSON format.
    - For POST requests, it creates a new cat record based on the provided
      JSON data.

    Parameters:
    request (HttpRequest): The HTTP request object from Django.

    Returns:
    JsonResponse: For GET requests, a list of all cats. For POST requests,
                  a success message or an error message in case of incomplete data.
    
    This function is CSRF exempt, so a CSRF token is not needed. 
    """

    if request.method == "GET":
        cats = Cat.objects.all()
        data = [
            {
                "id": cat.pk,
                "name": cat.name,
                "age": cat.age,
                "breed": cat.breed,
                "is_adopted": cat.is_adopted,
            }
            for cat in cats
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        age = data.get("age")
        breed = data.get("breed")
        is_adopted = True if data.get("is_adopted")=="true" else False

        if name and age is not None and breed:
            cat = Cat.objects.create(
                name=name,
                age=age,
                breed=breed,
                is_adopted=is_adopted,
            )
            return JsonResponse({"message": "Cat added successfully."})
        else:
            return JsonResponse(
                {"message": "Incomplete data. Please provide name, age, breed, and is_adopted."},
                status=400,
            )

@csrf_exempt
def update_cat(request, pk):
    
    """
    View that handles update or deletion of a specific cat record identified by its primary key. 

    - For PUT requests it updates the cat record with the specified pk based on the provided JSON data.
    - For DELETE requests it deletes the cat record with the specified pk.

    Parameters:
    request (HttpRequest): The HTTP request object, containing the payload in case of PUT.
    pk (int): The primary key of the cat to be updated or deleted.

    Returns:
    JsonResponse: In the case of PUT, it returns a success message or an error message 
                  if the data is incomplete or the cat is not found. For DELETE, it returns
                  a success message or a 404 status if the cat is not found.

    """
    
    try:
        cat = Cat.objects.get(pk=pk)
    except Cat.DoesNotExist:
        return JsonResponse({"message": f"Cat with ID: {pk} not found."}, status=404)

    if request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON format."}, status=400)

        name = data.get("name")
        age = data.get("age")
        breed = data.get("breed")
        is_adopted = True if data.get("is_adopted")=="true" else False 

        if name is not None and age is not None and breed is not None and is_adopted is not None:
            cat.name = name
            cat.age = age
            cat.breed = breed
            cat.is_adopted = is_adopted
            cat.save()
            return JsonResponse({"message": "Cat updated successfully."})
        else:
            return JsonResponse(
                {"message": "Incomplete data. Please provide name, age, breed, and is_adopted."},
                status=400,
            )

    elif request.method == "DELETE":
        cat.delete()
        return JsonResponse({"message": "Cat deleted successfully."})