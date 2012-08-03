from five import grok

from zope.schema import TextLine, Text
from zope.interface import alsoProvides, implements, Interface
from plone.namedfile.field import NamedImage
from plone.autoform.interfaces import IFormFieldProvider
from collective.dexteritytextindexer import IDynamicTextIndexExtender
from plone.directives import form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.interfaces import IAboveContentBody

from seantis.dir.base import item
from seantis.dir.base import core
from seantis.dir.base.interfaces import IFieldMapExtender
from seantis.dir.base.fieldmap import FieldMap

from seantis.dir.roadworks import _
  
class IRoadworksDirectoryItem(form.Schema):
    """Extends the seantis.dir.IDirectoryItem."""

    road = TextLine(
        title=_(u'Road'),
        required=False
    )

    works = TextLine(
        title=_(u'Construction Works'),
        required=False
    )

    until = TextLine(
        title=_(u'Until'),
        required=False
    )

    obstacle = TextLine(
        title=_(u'Obstacle'),
        required=False
    )

    constructor = TextLine(
        title=_(u'Constructor'),
        required=False
    )

    contact = TextLine(
        title=_(u'Contact'),
        required=False
    )

alsoProvides(IRoadworksDirectoryItem, IFormFieldProvider)

@core.ExtendedDirectory
class RoadworksDirectoryItemFactory(core.DirectoryMetadataBase):
    interface = IRoadworksDirectoryItem

class RoadworksDirectoryItem(item.DirectoryItem):
    pass

class DirectoryItemSearchableTextExtender(grok.Adapter):
    grok.context(item.IDirectoryItem)
    grok.name('IFacilityDirectoryItem')
    grok.provides(IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        """Extend the searchable text with a custom string"""
        context = self.context
        get = lambda ctx, attr: hasattr(ctx, attr) and unicode(getattr(ctx, attr)) or u''

        result = ' '.join((
                         get(context, 'road'),
                         get(context, 'works'),
                         get(context, 'until'),
                         get(context, 'obstacle'),
                         get(context, 'constructor'),
                         get(context, 'contact'),
                    ))

        return result

class ExtendedDirectoryItemViewlet(grok.Viewlet):
    grok.context(item.IDirectoryItem)
    grok.name('seantis.dir.base.item.detail')
    grok.require('zope2.View')
    grok.viewletmanager(item.DirectoryItemViewletManager)

    template = grok.PageTemplateFile('templates/listitem.pt')

class View(core.View):
    """Default view of a seantis.dir.contacts item."""
    grok.context(item.IDirectoryItem)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/item.pt')

class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of seantis.dir.facilty.item."""
    grok.context(FieldMap)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self):
        itemmap = self.context
        itemmap.interface = IRoadworksDirectoryItem

        extended = ['road', 'works', 'until',
                    'obstacle', 'constructor', 'contact']
        
        itemmap.add_fields(extended, len(itemmap))