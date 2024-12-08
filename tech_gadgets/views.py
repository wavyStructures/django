from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from .dummy_data import gadgets

# Create your views here.
def start_page_view(request):
    return HttpResponse('<h1>Welcome to the Tech Gadgets Homepage</h1>')

def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id >= 0:
        new_slug = slugify(gadgets[gadget_id]['name']) 
        new_url = reverse('gadget_slug_url', args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound('<h1>Page not found</h1>')

class GadgetView(View):
    
    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
# def single_gadget_view(request, gadget_slug=""):
    
#     if request.method == "GET":
#     gadget_match = None
    
#     for gadget in gadgets:
#         if slugify(gadget["name"]) == gadget_slug:
#             gadget_match = gadget
            
#         if gadget_match:
#             return JsonResponse(gadget_match)
#         raise Http404()
    def post(self, request, *args, **kwargs):
            try:
                data = json.loads(request.body)
                print(f"Data received: {data}")
                return JsonResponse({"response": "hat geklappt"})
            except:
                return JsonResponse({"response": "Invalid request"})
