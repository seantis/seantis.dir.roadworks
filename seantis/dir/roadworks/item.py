from five import grok
from zope.schema import TextLine
from collective.dexteritytextindexer import searchable

from seantis.dir.base import item
from seantis.dir.base import core
from seantis.dir.base.interfaces import IFieldMapExtender
from seantis.dir.base.fieldmap import FieldMap

from seantis.dir.roadworks import _
  
class IRoadworksDirectoryItem(item.IDirectoryItem):
    """Extends the seantis.dir.IDirectoryItem."""

    searchable('road')
    road = TextLine(
        title=_(u'Road'),
        required=False
    )

    searchable('works')
    works = TextLine(
        title=_(u'Construction Works'),
        required=False
    )

    searchable('until')
    until = TextLine(
        title=_(u'Until'),
        required=False
    )

    searchable('obstacle')
    obstacle = TextLine(
        title=_(u'Obstacle'),
        required=False
    )

    searchable('constructor')
    constructor = TextLine(
        title=_(u'Constructor'),
        required=False
    )

    searchable('contact')
    contact = TextLine(
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
    grok.context(IRoadworksDirectoryItem)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self):
        itemmap = self.context
        itemmap.interface = IRoadworksDirectoryItem

        extended = ['road', 'works', 'until',
                    'obstacle', 'constructor', 'contact']
        
        itemmap.add_fields(extended, len(itemmap))