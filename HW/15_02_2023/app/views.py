from django.shortcuts import render

from app import models


# Create your views here.


def index(request):
    message = ""
    if request.method == "POST":
        if request.POST['method'] == "POST":
            if 'new_category' in request.POST:
                if request.POST['title'] is not "":
                    # todo POST request => INSERT INTO Products_category title VALUES {title}
                    models.Products_category.objects.create(title=request.POST['title'])
                else:
                    message = "Форма не заполнена"
            elif 'new_product' in request.POST:
                id = request.POST['category_id']
                if request.POST['title'] is not "" and \
                        models.Products_category.objects.filter(id=id).exists():
                    # todo POST request => INSERT INTO Products (title, category_id) VALUES ({title}, {category_id})
                    models.Products.objects.create(
                        title=request.POST['title'],
                        category_id=id
                    )
                else:
                    message = "Форма не заполнена"
            else:
                message = "Форма не найдена"
        elif request.POST['method'] == "UPDATE":
            id = request.POST['product_id']
            if 'update_count' in request.POST:
                count = request.POST['product_count']
                # todo UPDATE request => UPDATE Products SET count = {count} WHERE id = {id};
                if models.Products.objects.filter(id=id).exists() and count:
                    model = models.Products.objects.get(id=id)
                    model.count = count
                    model.save()

            elif 'update_price' in request.POST:
                price = request.POST['product_price']
                # todo UPDATE request => UPDATE Products SET price = {price} WHERE id = {id};
                if models.Products.objects.filter(id=id).exists() and price:
                    model = models.Products.objects.get(id=id)
                    model.price = price
                    model.save()

        elif request.POST['method'] == "DELETE":
            if 'delete_product' in request.POST:
                id = request.POST['product_id']
                if models.Products.objects.filter(id=id).exists():
                    # todo DELETE request => DELETE FROM Products WHERE id = {id};
                    models.Products.objects.get(id=id).delete()

    # todo GET => SELECT * FROM Products
    products = models.Products.objects.all()
    # todo GET => SELECT * FROM Products_category
    categorys = models.Products_category.objects.all()
    return render(request, 'index.html', context={'categorys': categorys, 'products': products, 'message': message})
