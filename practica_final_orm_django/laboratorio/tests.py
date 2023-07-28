from django.test import TestCase, Client
from django.urls import reverse
from .models import Laboratorio

class LaboratorioViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba para el laboratorio
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio de Prueba', ciudad='Ciudad de Prueba', pais='País de Prueba')

    # Verificar que los datos en la base de datos coinciden con los creados en setUpTestData
    def test_model_content(self):     
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio de Prueba')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad de Prueba')
        self.assertEqual(self.laboratorio.pais, 'País de Prueba')

    def test_url_laboratorio(self):
        # Obtener la URL para la vista de laboratorio
        url = reverse('detalle/')

        # Verificar que se devuelve una respuesta HTTP 200
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vista_laboratorio(self):
        # Obtener la URL para la vista de laboratorio usando reverse
        url = reverse('detalle')

        # Enviar una solicitud GET a la URL y verificar la respuesta
        response = self.client.get(url)

        # Verificar que se usa la plantilla correcta
        self.assertTemplateUsed(response, 'detalle_laboratorio.html')

        # Verificar que el contenido HTML coincide con lo esperado
        self.assertContains(response, 'Contenido esperado en la página')

