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
    def test_add_admin(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': 'Jane',
            'surname': 'Doe',
            'email': 'jdoe@gmail.com',
            'phone_number': '1111111111',
            'role': 'True'
        }
        response = self.client.post('/add', data)
        self.assertEqual(response.status_code, 302)

    def test_add_regular(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': 'Jane',
            'surname': 'Doe',
            'email': 'jdoe@gmail.com',
            'phone_number': '1111111111',
            'role': 'False'
        }
        response = self.client.post('/add', data)
        self.assertEqual(response.status_code, 302)

    def test_add_invalid(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': 'Jane',
            'surname': 'Doe',
            'email': 'not an email',
            'phone_number': '1111111111',
            'role': 'True'
        }
        response = self.client.post('/add', data)
        self.assertEqual(response.status_code, 200)


class EditViewTests(TestCase):
    def test_edit_nonexistent(self):
        response = self.client.get('/edit/1')
        self.assertRedirects(response, '/not-found')

    def test_edit_name(self):
        models.Member.objects.create(first_name="John", surname="Doe", email="jdoe@gmail.com",
                                     phone_number="1111111111", role=False)
        response = self.client.get('/edit/1')
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': 'Jane',
            'surname': 'Doe',
            'email': 'jdoe@gmail.com',
            'phone_number': '1111111111',
            'role': 'False'
        }
        response = self.client.post('/edit/1', data)
        self.assertEqual(response.status_code, 302)

    def test_edit_email(self):
        models.Member.objects.create(first_name="John", surname="Doe", email="jdoe@gmail.com",
                                     phone_number="1111111111", role=False)
        response = self.client.get('/edit/1')
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': 'John',
            'surname': 'Doe',
            'email': 'johnd@gmail.com',
            'phone_number': '1111111111',
            'role': 'False'
        }
        response = self.client.post('/edit/1', data)
        self.assertEqual(response.status_code, 302)

    def test_edit_invalid(self):
        response = self.client.get('/edit')
        self.assertEqual(response.status_code, 200)

    def test_edit_role(self):
        models.Member.objects.create(first_name="John", surname="Doe", email="jdoe@gmail.com",
                                     phone_number="1111111111", role=False)
        response = self.client.get('/edit/1')
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': 'John',
            'surname': 'Doe',
            'email': 'jdoe@gmail.com',
            'phone_number': '1111111111',
            'role': 'True'
        }
        response = self.client.post('/edit/1', data)
        self.assertEqual(response.status_code, 302)
