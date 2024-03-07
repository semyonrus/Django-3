from django.shortcuts import redirect
import csv
from django.shortcuts import render
from .models import Phone
from django.utils.text import slugify


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'catalog.html', context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, 'product.html', context)


def load_data_from_csv(request):
    with open('phones.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)  # Пропускаем заголовок

        for row in csvreader:
            phone = Phone()
            phone.id = int(row[0])
            phone.name = row[1]
            phone.price = float(row[3])
            phone.slug = slugify(row[1])
            phone.save()

    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'catalog.html', context)

def show_catalog(request):
    sort_type = request.GET.get('sort')  # Получаем параметр sort из запроса

    if sort_type == 'name':  # Сортировка по названию
        phones = Phone.objects.all().order_by('name')
    elif sort_type == 'min_price':  # Сортировка по минимальной цене
        phones = Phone.objects.all().order_by('price')
    elif sort_type == 'max_price':  # Сортировка по максимальной цене
        phones = Phone.objects.all().order_by('-price')
    else:  # Сортировка по умолчанию по id
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, 'catalog.html', context)

