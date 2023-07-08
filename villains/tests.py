from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Villain


class VillainTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_villain = Villain.objects.create(name='flower', owner=testuser1, desc="test desc ...")
        test_villain.save()

    def test_model(self):
        villain = Villain.objects.get(id=1)
        actual_author = str(villain.author)
        actual_name = str(villain.name)
        actual_desc = str(villain.desc)
        self.assertEqual(actual_author, "testuser1")
        self.assertEqual(actual_name, "flower")
        self.assertEqual(actual_desc, "test desc ...")
