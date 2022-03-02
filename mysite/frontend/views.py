from django.shortcuts import render


def home(request):
    return render(request, 'frontend/home.html')

# def ajax_create_view(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         alias = request.POST.get('alias')
#         new_hero = Hero.obects.get_or_create(name=name, alias=alias)
#         data = serializers.serialize('json', new_hero[0]) 
#         return JsonResponse(data, safe=False)
#     else:
#         return JsonResponse({'method' : Nope})

# def ajax_create_hero(request):
#     pass
