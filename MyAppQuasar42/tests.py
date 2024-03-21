from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from .models import MBReservation, MBLieux

# Test for the views
class TestViews(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

#Test for the models  

class TestModels(TestCase):

    def test_mblieux_str(self):
        lieu = MBLieux.objects.create(Nom_du_lieu_choisie='Terrain1')
        self.assertEqual(str(lieu), lieu.Nom_du_lieu_choisie)

   

