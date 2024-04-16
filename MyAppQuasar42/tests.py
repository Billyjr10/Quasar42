from django.test import TestCase
from django.urls import reverse
import logging
from .models import MBContact, MBLieux, MBReservation
from .views import index, contact
import sentry_sdk

# Configuration du logger pour intégrer avec Sentry
logger = logging.getLogger(__name__)

# Test Views
class TestViews(TestCase):
    def test_index_view(self):
        try:
            response = self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')
        except AssertionError as e:
            logger.error(f"Test index_view failed: {e}", exc_info=True)
            sentry_sdk.capture_exception(e)
            raise

    def test_contact_view(self):
        try:
            response = self.client.get(reverse('contact'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'contact.html')
        except AssertionError as e:
            logger.error(f"Test contact_view failed: {e}", exc_info=True)
            sentry_sdk.capture_exception(e)
            raise

# Test Models
class TestModels(TestCase):
    def setUp(self):
        self.contact = MBContact.objects.create(
            name='Virgile Fouche', 
            email='virgile.fourche@example.com', 
            phone='123456789', 
            message='Hello'
        )
        self.lieu = MBLieux.objects.create(Nom_du_lieu_choisie='Terrain1')
        self.reservation = MBReservation.objects.create(
            Name='Alice', 
            Phone='987654321', 
            Email='alice@example.com', 
            Nom_du_lieu_choisie=self.lieu, 
            Date_choisie='2024-03-23', 
            Heure_choisie='10:00', 
            ref='ABC123'
        )

    def test_contact_creation(self):
        try:
            self.assertEqual(self.contact.name, 'Virgile Fouche')
            self.assertEqual(self.contact.email, 'virgile.fourche@example.com')
            self.assertEqual(self.contact.phone, '123456789')
            self.assertEqual(self.contact.message, 'Hello')
        except AssertionError as e:
            logger.error(f"Test contact_creation failed: {e}", exc_info=True)
            sentry_sdk.capture_exception(e)
            raise

# Test pour vérifier la remontée d'une erreur à Sentry
class SentryErrorTest(TestCase):
    def test_sentry_logging(self):
        try:
            self.assertEqual(1, 6, "Yes : Intentional error for Sentry")
        except AssertionError as e:
            sentry_sdk.capture_exception(e)
            raise e
    
