from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from django.views import  View
from store.models import Products

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

# class Cart(View):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cart_id = self.request.session.get("cart_id", None)
#         id cart_id:
#             cart = Cart.objects.get(id=cart_id)
#             else:
#                 cart = None
#         context["cart"] = cart
#         return context
    
'''
from django.conf import settings

from store.models import Products


def __init__(self, session):
    """
    Initialize shopping cart.
    """
    self.session = session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
        cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart

def add(self, product, quantity=1, update_quantity=False):
    """
    Add new product to cart, or update quantity of item already in cart.
    """
    product_id = str(product.id)
    if product_id not in self.cart:
        self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price),
                                    'name': product.name,
                                    }
    if update_quantity:
        self.cart[product_id]['quantity'] = quantity
    else:
        self.cart[product_id]['quantity'] += quantity
    self.save()

def get_cart_list(self):
    """
    Returns the cart as a list, this format is more suitable than a dictionary for
    the frontend to make a detail view with.
    """
    cart_list = []
    print(self.cart)
    for product_id, value in self.cart.items():
        cart_list.append({
            "id": product_id,
            "name": value['name'],
            "price": value['price'],
            "quantity": value['quantity'],
        })
    return cart_list

def save(self):
    self.session[settings.CART_SESSION_ID] = self.cart
    self.session.modified = True
    '''