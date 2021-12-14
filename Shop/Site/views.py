from django.http.response import JsonResponse
from .forms import Item
from django.shortcuts import render
from .models import Categories, Clothes, Profile_Cart, Profile, Favourite,Orders,Order
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

def main_page(request):
    return render(request,'main_page.html')

def assortment(request):
    categories = Categories.objects.all().order_by('id')
    return render(request, 'assortment.html',
                  {'categories': categories})

def show_category(request, category_id):
    one_category = Clothes.objects.all().filter(garment=category_id)
    title = Categories.objects.get(pk=category_id).name
    items_in_cart = Profile_Cart.objects.all().filter(user=request.user.id)
    items_in_favourite = Favourite.objects.all().filter(user=request.user.id)
    ids_cart = [item.item.id for item in items_in_cart]
    ids_favourite = [item.item.id for item in items_in_favourite]

    return render(request, 'one_category.html',
                  {'category': one_category,
                   'title': title,
                   'items_in_users_cart': ids_cart,
                   'items_in_favourite': ids_favourite})

@login_required(login_url='login')
def show_favourite(request):
    title = 'Избранное'
    items_in_cart = Profile_Cart.objects.all().filter(user=request.user.id)
    items_in_favourite = Favourite.objects.all().filter(user=request.user.id)
    ids_cart = [item.item.id for item in items_in_cart]
    ids_favourite = [item.item.id for item in items_in_favourite]
    one_category = Clothes.objects.all().filter(pk__in=ids_favourite)
    return render(request, 'favourite.html',
                  {   'category': one_category,
                      'title': title,
                      'items_in_users_cart': ids_cart,
                      'items_in_favourite': ids_favourite})


@login_required(login_url='login')
def show_cart(request):
    items_in_cart = Profile_Cart.objects.all().filter(user=request.user.id)
    ids = [item.item.id for item in items_in_cart]
    cloth = Clothes.objects.all().filter(pk__in=ids)
    full_price = cloth.aggregate(Sum('price'))
    return render(request, 'cart.html', {'items_in_cart': cloth, 'full_price': full_price['price__sum']})



@login_required(login_url='login')
def show_orders(request):
    orders = Orders.objects.all().filter(user=request.user.id).order_by('-id')  #выбираем все заказы
    orders_dict = {}
    for order in orders:
        items_in_order = Order.objects.all().filter(order_id = order.id) #для каждого заказа выбираем товары
        ids_of_items = []
        for item in items_in_order:
            ids_of_items.append(item.item)  #формируем список вещей в заказе
        orders_dict[order] = ids_of_items

    return render(request, 'orders.html', {'orders': orders_dict})

@login_required(login_url='login')
def add_or_delete(request):
    if request.method == 'POST' and request.is_ajax():
        form = Item(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']

            # если записи нет
            if not Profile_Cart.objects.filter(user=Profile.objects.get(user=request.user.id), item=Clothes.objects.get(id=item_id)).exists():
                item_in_cart = Profile_Cart(user=Profile.objects.get(
                    user=request.user.id), item=Clothes.objects.get(id=item_id))
                item_in_cart.save()
                counter = Profile_Cart.objects.filter(
                    user=request.user.id).count()
                return JsonResponse({"status": 'added', "id": item_id, 'counter': counter}, status=200)
            else:
                item_in_cart = Profile_Cart.objects.get(user=Profile.objects.get(
                    user=request.user.id), item=Clothes.objects.get(id=item_id))
                item_in_cart.delete()
                counter = Profile_Cart.objects.filter(
                    user=request.user.id).count()
                return JsonResponse({"status": 'deleted', "id": item_id, 'counter': counter}, status=200)

    if request.method == 'GET':
        return redirect('/')

@login_required(login_url='login')
def add_or_delete_favourite(request):
    if request.method == 'POST' and request.is_ajax():
        form = Item(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']

            # если записи нет
            if not Favourite.objects.filter(user=Profile.objects.get(user=request.user.id), item=Clothes.objects.get(id=item_id)).exists():
                item_in_favourite = Favourite(user=Profile.objects.get(
                    user=request.user.id), item=Clothes.objects.get(id=item_id))
                item_in_favourite.save()
                return JsonResponse({"status": 'added', "id_svg": f"f{item_id}", "id_path": f"f{item_id}p"}, status=200)
            else:
                item_in_favourite = Favourite.objects.get(user=Profile.objects.get(
                    user=request.user.id), item=Clothes.objects.get(id=item_id))
                item_in_favourite.delete()
                return JsonResponse({"status": 'deleted', "id_svg": f"f{item_id}", "id_path": f"f{item_id}p"}, status=200)

    if request.method == 'GET':
        return redirect('/')

@login_required(login_url='login')
def del_from_cart(request):
    if request.method == 'POST':
        form = Item(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']
            item_in_cart = Profile_Cart.objects.get(user=Profile.objects.get(
                user=request.user.id), item=Clothes.objects.get(id=item_id))
            item_in_cart.delete()
            return redirect('cart')
    if request.method == 'GET':
        return redirect('cart')

@login_required(login_url='login')   
def del_from_favourite(request):
    if request.method == 'POST':
        form = Item(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']
            item_in_cart = Favourite.objects.get(user=Profile.objects.get(
                user=request.user.id), item=Clothes.objects.get(id=item_id))
            item_in_cart.delete()
            return redirect('favourite')
    if request.method == 'GET':
        return redirect('favourite')



@login_required(login_url='login')
def clear_cart(request):
    if request.method == 'POST':
        items = Profile_Cart.objects.all().filter(user=Profile.objects.get(user=request.user.id))  # получаем объекты из корзины
        items.delete()
        return redirect('cart')
    if request.method == 'GET':
        return redirect('cart')

class MyLoginView(LoginView):
    template_name = 'login.html'


@login_required(login_url='login')
def make_order(request):
    if request.method == 'POST':
        items = Profile_Cart.objects.all().filter(
            user=Profile.objects.get(user=request.user.id))
        ids_of_items = [i.item.id for i in items]
        if ids_of_items == []:
            return redirect('cart')
        else:
            price = Clothes.objects.all().filter(pk__in = ids_of_items).aggregate(Sum('price'))
            new_order = Orders(user = Profile.objects.get(user=request.user.id),order_price = price['price__sum'])
            new_order.save()
            for i in ids_of_items:
                Order(order_id = Orders.objects.get(id = new_order.id),item = Clothes.objects.get(id = i)).save()
            items.delete()
        return redirect('cart')
    if request.method == 'GET':
        return redirect('cart')
