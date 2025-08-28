from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Order

# Home page -> Products
def items(request):
    items = Item.objects.all()
    return render(request, "items.html", {"items": items})

# Checkout page
def checkout(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        phone = request.POST["phone"]
        # Hapa tunaunda order ya test tu (bila API bado)
        order = Order.objects.create(
            customer_phone=phone,
            item=item,
            amount=item.price,
            status="pending"
        )
        return redirect("order_status", order.id)

    return render(request, "checkout.html", {"item": item})

# Order status page
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "status.html", {"order": order})


# Create your models here.

# Create your views here.
