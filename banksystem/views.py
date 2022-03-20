from django.shortcuts import render
from .models import CustomersModel


def customers(request):
    customer = CustomersModel.objects.all()
    context = {
        'customers': customer,
    }
    return render(request, 'customers/customers.html', context)
