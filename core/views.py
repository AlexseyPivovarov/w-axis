from django.shortcuts import render, HttpResponseRedirect, get_list_or_404, get_object_or_404
from django.views.generic import View
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.views import Response
from django.urls import reverse
from rest_framework import status
from .forms import CartForm
from json import dumps
from django.core.serializers.json import DjangoJSONEncoder

from .models import Product, Cart
from .serializer import ProductSerializer, CartSerializer


# Create your views here.
class ShoppingCartList(View):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)


class ProductList(View):
    template_name = 'productList.html'

    def get(self, request, **kwargs):
        context = {}
        context['data'] = []
        context['action'] = reverse("products")
        if kwargs:
            context['data'] = [item.id for item in get_object_or_404(Cart, id=kwargs.get('id')).product.all()]
            context['action'] = reverse("update", kwargs=kwargs)
        proddict = []
        for item in ProductSerializer(get_list_or_404(Product), many=True).data:
            item = dict(item)
            item['checked'] = item['id'] in context['data']
            proddict.append(item)
        context['products'] = dumps(proddict)
        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs):
        try:
            products_ids = dict(request.POST)["product"]
        except KeyError:
            return self.get(request, **kwargs)
        products = Product.objects.filter(id__in=products_ids).all()
        cost = sum((item.price for item in products))
        if kwargs:
            cart = get_object_or_404(Cart, id=kwargs.get('id'))
            cart.cost = cost
        else:
            cart = Cart(cost=cost)
        cart.save()
        cart.product.set(products)
        return HttpResponseRedirect('/')


class Products(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Carts(ListAPIView):

    def list(self, request, *args, **kwargs):
        serializer = CartSerializer(self.filter_queryset(Cart.objects.all()), many=True)
        data = []
        for item in serializer.data:
            item = dict(item)
            serializer = ProductSerializer(Product.objects.filter(id__in=item['product']).all(), many=True)
            item['product'] = serializer.data
            data.append(item)
        return Response(data)


class DeleteView(DestroyAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'