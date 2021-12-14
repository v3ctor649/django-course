from Site.models import Profile_Cart,Favourite,Orders

def shopping_cart(request):
    return {'counter_items_in_cart':Profile_Cart.objects.filter(user  = request.user.id).count(),
    'counter_items_in_favourite':Favourite.objects.filter(user = request.user.id).count(),
    'counter_items_in_orders':Orders.objects.filter(user = request.user.id).count()}




    