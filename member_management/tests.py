from django.test import TestCase
from . import models


class IndexViewTests(TestCase):
    def test_no_members(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No members found.")
        self.assertQuerysetEqual(response.context['members'], [])

    def test_one_admin(self):
        admin = models.Member.objects.create(first_name="Admin", surname="Lastname", email="admin@gmail.com",
                                             phone_number="1111111111", role=True)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['members'], [admin])

    def test_three_members(self):
        admin = models.Member.objects.create(first_name="Admin", surname="Lastname", email="admin@gmail.com",
                                             phone_number="1111111111", role=True)
        member_1 = models.Member.objects.create(first_name="Member", surname="Lastname", email="member@gmail.com",
                                                phone_number="1111111111", role=False)
        member_2 = models.Member.objects.create(first_name="John", surname="Doe", email="jdoe@gmail.com",
                                                phone_number="1111111111", role=False)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['members'], [admin, member_1, member_2], ordered=False)


class AddViewTests(TestCase):
    def add_admin(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)


class EditViewTests(TestCase):
    def edit_nonexistent(self):
        response = self.client.get('/edit')
        self.assertEqual(response.status_code, 200)
