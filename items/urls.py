from django.urls import path
from items.views import CrudItemAPIView, CrudItemDetailAPIView

urlpatterns = [
    path('items/', CrudItemAPIView.as_view()),
    path('items/<int:id>/', CrudItemDetailAPIView.as_view()),
]
