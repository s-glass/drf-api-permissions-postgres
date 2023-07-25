from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import State


class StateTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_state = State.objects.create(name="California", owner=testuser1, city="Arcata", description="Lush greenery and ocean.")
        test_state.save()

    def test_states_model(self):
        state = State.objects.get(id=1)
        actual_owner = str(state.owner)
        actual_name = str(state.name)
        actual_city = str(state.name)
        actual_description = str(state.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Guanajuato")
        self.assertEqual(actual_city, "Guanajuato")
        self.assertEqual(actual_description, "Such a cool place.")

    def test_states_model(self):
        test_state = State.objects.get(id=2)
        expected_state_name = "California"
        self.assertEqual(str(test_state), expected_state_name)