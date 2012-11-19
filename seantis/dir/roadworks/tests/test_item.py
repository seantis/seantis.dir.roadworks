from unittest import TestCase
from os import path
from zope.interface import Invalid
from plone.namedfile import NamedFile
from plone.namedfile import NamedImage
from seantis.dir.base.interfaces import IMapMarker
from seantis.dir.roadworks.item import validate_image
from seantis.dir.roadworks.item import View
from seantis.dir.roadworks.tests import IntegrationTestCase

class TestImageValidator(TestCase):

    def test_validate_image(self):
        result = validate_image(None)
        self.assertEqual(None, result)

        image = NamedFile('dummy test data', filename=u'test.txt')
        self.assertRaises(Invalid, validate_image, image)

        image_path = path.join(path.dirname(__file__), 'data', 'test.png')
        image = open(image_path)
        image_data = image.read()
        image.close()
        image = NamedImage(image_data, filename=u'test.png')
        self.assertEqual(None, result)

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
