from django.shortcuts import path
from . import views
urlpatterns = [
  path("", views.items, name="items"),
  path("checkout/<int:item_id>/", views.checkout, name="checkout"),
  path("order/<int:order_id>/", views.order_status, name="order_status"),
]
