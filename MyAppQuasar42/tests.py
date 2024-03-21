# Import des modules nécessaires pour les tests
from django.test import TestCase
from django.urls import reverse
from .models import MBContact, MBLieux, MBReservation
from .views import index, contact

#Test Views
class TestViews(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
#Test Models
class TestModels(TestCase):
    def setUp(self):
       
        self.contact = MBContact.objects.create(name='Virgile Fouche', email='virgile.fourche@example.com', phone='123456789', message='Hello')
        self.lieu = MBLieux.objects.create(Nom_du_lieu_choisie='Terrain1')
        self.reservation = MBReservation.objects.create(Name='Alice', Phone='987654321', Email='alice@example.com', Nom_du_lieu_choisie=self.lieu, Date_choisie='2024-03-23', Heure_choisie='10:00', ref='ABC123')

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, 'Virgile Fouche')
        self.assertEqual(self.contact.email, 'virgile.fourche@example.com')
        self.assertEqual(self.contact.phone, '123456789')
        self.assertEqual(self.contact.message, 'Hello')

    def test_lieu_creation(self):
        self.assertEqual(self.lieu.Nom_du_lieu_choisie, 'Terrain1')

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.Name, 'Alice')
        self.assertEqual(self.reservation.Phone, '987654321')
        self.assertEqual(self.reservation.Email, 'alice@example.com')
        self.assertEqual(self.reservation.Nom_du_lieu_choisie, self.lieu)
        self.assertEqual(self.reservation.Date_choisie, '2024-03-23')
        self.assertEqual(self.reservation.Heure_choisie, '10:00')
        self.assertEqual(self.reservation.ref, 'ABC123')
