from datetime import datetime
import pytz
import requests

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render, redirect
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_api import models

from django_api import serializers as django_serializers


@api_view(http_method_names=["GET", "DELETE", "POST"])
@permission_classes((permissions.AllowAny,))
def task(request: HttpRequest, id: int, user_id=-1):
    if user_id != -1:
        delete = request.data.get("_method", None)
        if request.method == "GET":
            try:
                task = models.Tasks.objects.filter(id=id, user_id=user_id)
                print('task', task)
                data_json = django_serializers.PostsSerializer(instance=task, many=True)
                return Response(data=data_json.data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(data={"error": f"Данных не существует"}, status=status.HTTP_204_NO_CONTENT)

        # elif request.method in ["PUT", "PATCH"]:
        #     task = models.Tasks.objects.get(id=id)
        #     message = "Without changes"
        #     id = request.data.get("id", None)
        #     title = request.data.get("title", None)
        #     completed = request.data.get("completed", None)
        #
        #     if id is None:
        #         return Response(data={"error": f"При обновлении не был указан id"},
        #                         status=status.HTTP_204_NO_CONTENT)
        #     else:
        #         post = models.Tasks.objects.get(id=id)
        #         if post.title != title and title is not None:
        #             post.title = title
        #             message = "Successfully update"
        #         if post.completed != completed and completed is not None:
        #             post.title = completed
        #             message = "Successfully update"
        #         post.save()
        #
        #         return Response(data={"detail": "Successfully update"}, status=status.HTTP_200_OK)

        elif request.method == "DELETE" or delete is not None:
            try:
                task = models.Tasks.objects.get(id=id)
                task.delete()
                # return Response(data={"detail": "Successfully deleted"}, status=status.HTTP_200_OK)
                # return HttpResponsePermanentRedirect("/")

                mess = f"User with id = {task.user_id} delete task with id = {id}"
                # response1 = requests.get(f"http://127.0.0.2:8000/new_log/{mess}")

                print("Удалил \n\n\n")
                return Response(data={"status": f"OK"}, status=status.HTTP_200_OK)
                # return redirect(reverse('django_app:index', kwargs={"user_id": user_id}))
            except:
                task = models.Tasks.objects.get(id=id)
                task.delete()
                # return Response(data={"detail": "Successfully deleted"}, status=status.HTTP_200_OK)
                # return HttpResponsePermanentRedirect("/")

                mess = f"User with id = {task.user_id} delete task with id = {id}"
                # response1 = requests.get(f"http://127.0.0.2:8000/new_log/{mess}")

                print("Удалил \n\n\n")
                return Response(data={"status": f"OK"}, status=status.HTTP_200_OK)
                # return redirect(reverse('django_app:index', kwargs={"user_id": user_id}))


        elif request.method == "POST":
            # task = models.Tasks.objects.get(id=id)
            title = request.data.get("title", None)
            description = "description"

            # request.data.get("description", None)

            now = datetime.now(pytz.UTC)
            created = now.strftime("%Y-%m-%d %H:%M:%S.%f%z")

            if title is None or description is None:
                return Response(data={"detail": "Not successfully created"}, status=status.HTTP_204_NO_CONTENT)

            new_data_in_db = models.Tasks.objects.create(
                user_id=user_id,
                title=title,
                description=description,
                created=created,
                update=created
            )
            # Content
            # {
            #     "title": "title",
            #     "description": "description"
            # }
            new_data_in_db.save()

            mess = f"User with id = {user_id} crate task on {created}"
            # response1 = requests.get(f"http://127.0.0.2:8000/new_log/{mess}")


            # return HttpResponsePermanentRedirect("/")
            return Response(data={"status": f"OK"}, status=status.HTTP_200_OK)
            # return redirect(reverse('django_app:index', kwargs={"user_id": user_id}))

    else:
        return Response(data={"error": f"Вы не авторизованы"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE", "POST"])
@permission_classes((permissions.AllowAny,))
def tasks(request: HttpRequest, id="-1", user_id=-1):
    tasks = models.Tasks.objects.filter(user_id=user_id)  # TODO QuerySet != JSON
    print(tasks)
    data_json = django_serializers.PostsSerializer(instance=tasks, many=True)
    return Response(data=data_json.data, status=status.HTTP_200_OK)

    # except Exception as e:
    #     print(e, ' ошибка')
    #     return Response(data={"error": f"Данных не существует"}, status=status.HTTP_204_NO_CONTENT)
