from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
	def test_create_user_with_email_successful(self):
		"""Test creating user with email is successful"""
		email = 'email@domain.com'
		password = 'password'
		user = get_user_model().objects.create_user(
			email = email,
			password = password
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))
	
	def test_new_user_email_normalized(self):
		"""Test the email for new user is normalized"""
		email = 'email@DOMAIN.com'
		user = get_user_model().objects.create_user(email, 'password')

		self.assertEqual(user.email, email.lower())
	
	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises error"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'password')

	def test_create_new_superuser(self):
		"""Test creating a new superusser"""
		user = get_user_model().objects.create_superuser(
			'email@domain.com',
			'password'
		)

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)
		