from seantis.dir.base.interfaces import IMapMarker
from seantis.dir.roadworks.item import View
from seantis.dir.roadworks.tests import IntegrationTestCase

class TestView(IntegrationTestCase):

    def test_details(self):
        directory = self.add_directory()
        item = self.add_item(directory)

        view = View(item, self.portal.REQUEST)
        details = [detail for detail in view.details()]
        self.assertEqual([], details)

        item.road = u'Unter der Egg'
        details = [detail for detail in view.details()]
        self.assertEqual([(u'Road', u'Unter der Egg')], details)

class TestRoadworkMapMarker(IntegrationTestCase):

    def test_url(self):
        directory = self.add_directory()
        item = self.add_item(directory)

        marker = IMapMarker(item)
        url = marker.url('A')
        expected = '++resource++seantis.dir.roadworks.images/construction-marker.png'
        self.assertIn(expected, url)
