from django.db import transaction
from django.shortcuts import render

from app import models


# Create your views here.

@transaction.atomic
def index(request):
    message = ""
    if request.method == "POST":
        if request.POST['method'] == "POST":
            try:
                if 'new_category' in request.POST:
                    if request.POST['title'] is not "":
                        with transaction.atomic():
                            # todo POST request => INSERT INTO Products_category title VALUES {title}
                            foo = models.Products_category.objects.create(title=request.POST['title'])
                            transaction.on_commit(lambda: print("Удачно"))
                    else:
                        message = "Форма не заполнена"

                elif 'new_product' in request.POST:
                    id = request.POST['category_id']
                    if request.POST['title'] is not "" and \
                            models.Products_category.objects.filter(id=id).exists():
                        with transaction.atomic():
                            # todo POST request => INSERT INTO Products (title, category_id) VALUES ({title}, {category_id})
                            models.Products.objects.create(
                                title=request.POST['title'],
                                category_id=id
                            )
                            # коммитим
                            transaction.on_commit(lambda: print("Удачно"))
                    else:
                        message = "Форма не заполнена"

                else:
                    message = "Форма не найдена"

            except Exception as e:
                print(e)
                message = "Добавление отменено"

        elif request.POST['method'] == "UPDATE":
            id = request.POST['product_id']
            try:
                if 'update_count' in request.POST:
                    count = request.POST['product_count']
                    with transaction.atomic():
                        # todo UPDATE request => UPDATE Products SET count = {count} WHERE id = {id};
                        if models.Products.objects.filter(id=id).exists() and count:
                            model = models.Products.objects.get(id=id)
                            model.count = count
                            model.save()
                        transaction.on_commit(lambda: print("Удачно"))

                elif 'update_price' in request.POST:
                    price = request.POST['product_price']
                    with transaction.atomic():
                        # todo UPDATE request => UPDATE Products SET price = {price} WHERE id = {id};
                        if models.Products.objects.filter(id=id).exists() and price:
                            model = models.Products.objects.get(id=id)
                            model.price = price
                            model.save()
                        transaction.on_commit(lambda: print("Удачно"))
            except Exception as e:
                print(e)
                message = "Обновление отменено"
        elif request.POST['method'] == "DELETE":
            if 'delete_product' in request.POST:
                id = request.POST['product_id']
                try:
                    with transaction.atomic():
                        if models.Products.objects.filter(id=id).exists():
                            # todo DELETE request => DELETE FROM Products WHERE id = {id};
                            models.Products.objects.get(id=id).delete()
                        transaction.on_commit(lambda: print("Удачно"))
                except Exception as e:
                    print(e)
                    message = "Удаление отменено"
    # todo GET => SELECT * FROM Products
    products = models.Products.objects.all()
    # todo GET => SELECT * FROM Products_category
    categorys = models.Products_category.objects.all()
    return render(request, 'index.html', context={'categorys': categorys, 'products': products, 'message': message})
