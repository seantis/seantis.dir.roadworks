from seantis.dir.roadworks.tests.layer import Layer
from Products.PloneTestCase.ptc import PloneTestCase


class IntegrationTestCase(PloneTestCase):
    layer = Layer

    def add_directory(self, name='Directory'):
        self.folder.invokeFactory('seantis.dir.roadworks.directory', name)
        return self.folder[name]

    def add_item(self, directory, name='DirectoryItem'):
        directory.invokeFactory('seantis.dir.roadworks.item', name)
        return directory[name]
