from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JW2ytIOxJFy7n0LIOhhfyBeSaaSUOKj07rrHYcY5lR9AKNpwrV1iMWY1Y0s5DtVUJNJapdKw37f9O9qHSyqDHjU002eWG4Am8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
