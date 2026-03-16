from django.test import SimpleTestCase, Client


class HomePageTestCase(SimpleTestCase):
    """Test de la page d'accueil."""

    def test_home_page_does_not_contain_badr(self):
        """
        Ce test échoue si le mot 'Badr' apparaît dans le HTML de la page d'accueil.
        """
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf-8')
        self.assertNotIn(
            'Badr',
            html,
            "Le mot 'Badr' ne doit pas apparaître dans le HTML de la page d'accueil."
        )
