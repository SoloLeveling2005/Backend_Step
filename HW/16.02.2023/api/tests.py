from django.test import TestCase
from django.test import Client


# # Create your tests here.
#
#
class GetMethodTest(TestCase):
    def setUp(self):
        print("\nGetMethodTest")

    def test(self):
        """
        Получение данных с БД
        """

        client = Client()
        response = client.get('/get/')

        self.assertEqual(response.status_code, 202)

class PostMethodTest(TestCase):
    def setUp(self):
        print("\nPostMethodTest")

    def test(self):
        """
        Добавление данных в БД
        """

        title = "Думай и богатей"
        client = Client()
        response = client.post('/post/', {'title': title})

        self.assertEqual(response.status_code, 200)


class UpdateMethodTest(TestCase):
    def setUp(self):
        print("\nUpdateMethodTest")

    def test(self):
        """
        Обновление данных в БД
        """

        book_id = 1
        client = Client()
        response = client.post('/update/', {'id': book_id})

        self.assertEqual(response.status_code, 200)



class DeleteMethodTest(TestCase):
    def setUp(self):
        print("\nDeleteMethodTest")

    def test(self):
        """
        Удаление данных из БД
        """
        book_id = 0
        client = Client()
        response = client.post('/delete/', {'id': book_id})

        self.assertEqual(response.status_code, 200)