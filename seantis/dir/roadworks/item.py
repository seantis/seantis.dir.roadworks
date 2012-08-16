from five import grok
from zope.schema import Text
from collective.dexteritytextindexer import searchable

from seantis.dir.base import item
from seantis.dir.base import core
from seantis.dir.base.interfaces import IFieldMapExtender

from seantis.dir.roadworks.directory import IRoadworksDirectory
from seantis.dir.roadworks import _
  
class IRoadworksDirectoryItem(item.IDirectoryItem):
    """Extends the seantis.dir.IDirectoryItem."""

    searchable('project')
    project = Text(
        title=_(u'Project'),
        required=False
    )

    searchable('road')
    road = Text(
        title=_(u'Road'),
        required=False
    )

    searchable('section')
    section = Text(
        title=_(u'Section'),
        required=False
    )

    searchable('works')
    works = Text(
        title=_(u'Construction Works'),
        required=False
    )

    searchable('timespan')
    timespan = Text(
        title=_(u'Timespan'),
        required=False
    )

    searchable('obstacles')
    obstacles = Text(
        title=_(u'Obstacles'),
        required=False
    )

    searchable('closures')
    closures = Text(
        title=_(u'Closures'),
        required=False
    )

    searchable('constructor')
    constructor = Text(
        title=_(u'Constructor'),
        required=False
    )

    searchable('contact')
    contact = Text(
        title=_(u'Contact'),
        required=False
    )

class RoadworksDirectoryItem(item.DirectoryItem):
    pass

class RoadworksDirectoryItemViewlet(grok.Viewlet):
    grok.context(IRoadworksDirectoryItem)
    grok.name('seantis.dir.roadworks.item.detail')
    grok.require('zope2.View')
    grok.viewletmanager(item.DirectoryItemViewletManager)

    template = grok.PageTemplateFile('templates/listitem.pt')

class View(core.View):
    """Default view of a seantis.dir.roadworks item."""
    grok.context(IRoadworksDirectoryItem)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/item.pt')

class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of seantis.dir.facilty.item."""
    grok.context(IRoadworksDirectory)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self, itemmap):
        itemmap.typename = 'seantis.dir.roadworks.item'
        itemmap.interface = IRoadworksDirectoryItem

        extended = ['road', 'works', 'until',
                    'obstacle', 'constructor', 'contact']
        
        itemmap.add_fields(extended, len(itemmap))