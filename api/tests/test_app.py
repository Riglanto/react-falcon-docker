from falcon import testing
import app


class TestApp(testing.TestCase):
    def setUp(self):
        super(TestApp, self).setUp()
        self.app = app.create()

    def test_get_message(self):
        doc = {u'message': u'Hello world!'}

        result = self.simulate_get('/data')
        json = result.json

        self.assertEqual(len(json), 219)
        self.assertEqual(json[0], {'date': '02.12.13', 'yield': 92.1})
        self.assertEqual(json[-1], {'date': '21.10.14', 'yield': 92.6})
