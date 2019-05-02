from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView, CreateView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        # self.request.session['reviewed_products'] = []
        if self.request.method == 'GET':
            form = ReviewForm(self.request.POST or None)  # instance= None

        reviews = Review.objects.all().filter(product=self.object.id)
        context['reviews'] = reviews

        if 'reviewed_products' in self.request.session and self.object.id in self.request.session['reviewed_products']:
            context["is_review_exist"] = True
            return context

        context["form"] = form

        return context


    def post(self, request, **kwargs):
        form = ReviewForm(request.POST or None)
        pk = kwargs['pk']
        if form.is_valid():
            text = request.POST['text']
            product = Product.objects.get(id=pk)
            Review.objects.create(text=text, product=product)
        # else:
        #     print(request)
        #     return render(request, 'app/product_detail.html', {'form': form})

        return redirect('product_detail', pk=pk)

    # def post(self, request, *args, **kwargs):
    #     form = ReviewForm(self.request.POST or None)
    #     pk = kwargs['pk']
    #
    #     if form.is_valid():
    #         text = request.POST['text']
    #         product = Product.objects.get(id=pk)
    #         Review.objects.create(text=text, product=product)
    #     else:
    #         return render(request, 'app/product_detail.html')
    #
    #     if 'reviewed_products' in request.session:
    #         value = request.session['reviewed_products']
    #         value.append(kwargs['pk'])
    #         request.session['reviewed_products'] = value
    #     else:
    #         request.session['reviewed_products'] = [pk]
    #
    #     return redirect('product_detail', pk=pk)
