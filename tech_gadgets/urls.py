from django.urls import path
from .views import start_page_view, single_gadget_int_view,\
 GadgetView, RedirectToGadgetView

urlpatterns = [
    path('start/',  start_page_view),
    path('',  RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name='gadget_slug_url'),  
]
  