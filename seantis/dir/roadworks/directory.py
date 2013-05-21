from five import grok
from plone.namedfile.field import NamedImage

from seantis.dir.base import directory
from seantis.dir.base.interfaces import IDirectory
from seantis.dir.roadworks import _


class IRoadworksDirectory(IDirectory):
    """Extends the seantis.dir.base.directory.IDirectory"""

    image = NamedImage(
        title=_(u'Image'),
        required=False,
        default=None
    )


class RoadworksDirectory(directory.Directory):
    pass


class ExtendedDirectoryViewlet(grok.Viewlet):
    grok.context(IRoadworksDirectory)
    grok.name('seantis.dir.roadworks.directory.detail')
    grok.require('zope2.View')
    grok.viewletmanager(directory.DirectoryViewletManager)

    template = grok.PageTemplateFile('templates/directorydetail.pt')


class View(directory.View):
    grok.context(IRoadworksDirectory)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/directory.pt')

    itemsperpage = 100
