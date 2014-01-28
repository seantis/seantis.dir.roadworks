from unittest import TestCase
from os import path
from zope.interface import Invalid

from plone import api
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
        self.login('admin')

        directory = api.content.create(
            container=self.new_temporary_folder(),
            type='seantis.dir.roadworks.directory',
            title='directory'
        )
        item = api.content.create(
            container=directory,
            type='seantis.dir.roadworks.item',
            title='item'
        )

        view = View(item, self.portal.REQUEST)
        self.assertEqual([], view.details())

        item.road = u'Unter der Egg'
        self.assertEqual([(u'Road', u'Unter der Egg')], view.details())

    def test_details_attachment(self):
        self.login('admin')

        directory = api.content.create(
            container=self.new_temporary_folder(),
            type='seantis.dir.roadworks.directory',
            title='directory'
        )
        item = api.content.create(
            container=directory,
            type='seantis.dir.roadworks.item',
            title='item'
        )

        item.road = u'Unter der Egg'
        item.attachment = NamedFile('Dummy content', filename=u'test.txt')

        view = View(item, self.portal.REQUEST)
        attachment_detail = view.details()[1]
        self.assertEqual(u'Attachment', attachment_detail[0])
        self.assertTrue(u'test.txt (0 KB)' in attachment_detail[1])


class TestRoadworkMapMarker(IntegrationTestCase):

    def test_url(self):
        self.login('admin')

        directory = api.content.create(
            container=self.new_temporary_folder(),
            type='seantis.dir.roadworks.directory',
            title='directory'
        )
        item = api.content.create(
            container=directory,
            type='seantis.dir.roadworks.item',
            title='item'
        )

        marker = IMapMarker(item)
        url = marker.url('A')
        expected = \
            '++resource++seantis.dir.roadworks.images/construction-marker.png'
        self.assertIn(expected, url)
