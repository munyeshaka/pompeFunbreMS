from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models import *
from django.views import View
from django.http import JsonResponse, HttpResponse
#from django.conf import settings


'''
class CheckOut(View):
    def post(self, request):
        clint = request.POST.get('client')
        phone = request.POST.get('phone')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            cartOrder = CartOrder(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            cartOrder.save()
        request.session['cart'] = {}

        return redirect('cart')
'''
class CheckOut(View):
    def post(self, request):
        feu = request.POST.get('feu')
        ne = request.POST.get('ne')
        decede = request.POST.get('decede')
        dateCeremony = request.POST.get('dateCeremony')
        customer = request.session.get('customer')
        morgue = request.POST.get('morgue')
        avance = request.POST.get('avance')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(feu, ne, decede, dateCeremony, morgue, customer, cart, products)

        total_amt=0
        totalAmt=0

        for product in products:
            print(cart.get(str(product.id)))
            orders = Orders(customer=Customer(id=customer),
                product=product,
                price=product.price,
                feu=feu,
                ne=ne,
                decede=decede,
                dateCeremony=dateCeremony,
                avance=avance,
                morgue=morgue,
                quantity=cart.get(str(product.id))
                )
            orders.save()
        request.session['cart'] = {}
        
        return redirect('store')
        
        '''
        return redirect(request, 'orders.html', {'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'form':form}))
        
        '''