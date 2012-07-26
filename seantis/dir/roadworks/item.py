from five import grok

from zope.schema import TextLine, Text
from zope.schema import URI
from zope.interface import alsoProvides
from plone.memoize import view
from plone.namedfile.field import NamedImage
from plone.autoform.interfaces import IFormFieldProvider
from plone.app.dexterity.behaviors.metadata import MetadataBase
from plone.app.dexterity.behaviors.metadata import DCFieldProperty
from collective.dexteritytextindexer import IDynamicTextIndexExtender
from plone.directives import form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from seantis.dir.base import core
from seantis.dir.base.item import IDirectoryItem
from seantis.dir.base.item import DirectoryItemViewletManager
from seantis.dir.base.interfaces import IFieldMapExtender
from seantis.dir.base.fieldmap import FieldMap
  
class IExtendedDirectoryItem(form.Schema):
    """Extends the seantis.dir.IDirectoryItem."""

alsoProvides(IExtendedDirectoryItem, IFormFieldProvider)


class ExtendedDirectoryItem(MetadataBase):
   pass


class DirectoryItemSearchableTextExtender(grok.Adapter):
    grok.context(IDirectoryItem)
    grok.name('IExtendedDirectoryItem')
    grok.provides(IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        """Extend the searchable text with a custom string"""
        # context = self.context
        # get = lambda ctx, attr: hasattr(ctx, attr) and unicode(getattr(ctx, attr)) or u''

        result = ''
        # result = ' '.join((
        #                  get(context, 'street'), 
        #             ))

        return result


class ExtendedDirectoryItemViewlet(grok.Viewlet):
    grok.context(IDirectoryItem)
    grok.name('seantis.dir.base.item.detail')
    grok.require('zope2.View')
    grok.viewletmanager(DirectoryItemViewletManager)

    template = grok.PageTemplateFile('templates/listitem.pt')


class View(core.View):
    """Default view of a seantis.dir.roadworks item."""
    grok.context(IDirectoryItem)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/item.pt')

class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of seantis.dir.base.item."""
    grok.context(FieldMap)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self):
        pass