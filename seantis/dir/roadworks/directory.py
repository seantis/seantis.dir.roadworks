from five import grok
from zope.interface import alsoProvides
from zope.interface import implements
from plone.namedfile.field import NamedImage
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from Products.CMFCore.utils import getToolByName

from seantis.dir.base import directory
from seantis.dir.base import core

from seantis.dir.roadworks import _

class IRoadworksDirectory(form.Schema):
    """Extends the seantis.dir.base.directory.IDirectory"""

    image = NamedImage(
            title=_(u'Image'),
            required=False
        )

alsoProvides(IRoadworksDirectory, IFormFieldProvider)

@core.ExtendedDirectory
class RoadworksDirectoryFactory(core.DirectoryMetadataBase):
    interface = IRoadworksDirectory

class RoadworksDirectory(directory.Directory):
    pass

class ExtendedDirectoryViewlet(grok.Viewlet):
    grok.context(directory.IDirectory)
    grok.name('seantis.dir.base.directory.detail')
    grok.require('zope2.View')
    grok.viewletmanager(directory.DirectoryViewletManager)

    template = grok.PageTemplateFile('templates/directorydetail.pt')