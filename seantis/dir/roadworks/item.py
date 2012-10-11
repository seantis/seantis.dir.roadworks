from five import grok
from zope.schema import TextLine
from collective.dexteritytextindexer import searchable

from seantis.dir.base import item
from seantis.dir.base import core
from seantis.dir.base import utils
from seantis.dir.base.interfaces import IFieldMapExtender, IDirectoryItem, IMapMarker

from seantis.dir.roadworks.directory import IRoadworksDirectory
from seantis.dir.roadworks import _
  
class IRoadworksDirectoryItem(IDirectoryItem):
    """Extends the seantis.dir.IDirectoryItem."""

    searchable('project')
    project = TextLine(
        title=_(u'Project'),
        required=False
    )

    searchable('road')
    road = TextLine(
        title=_(u'Road'),
        required=False
    )

    searchable('section')
    section = TextLine(
        title=_(u'Section'),
        required=False
    )

    searchable('works')
    works = TextLine(
        title=_(u'Construction Works'),
        required=False
    )

    searchable('timespan')
    timespan = TextLine(
        title=_(u'Timespan'),
        required=False
    )

    searchable('obstacles')
    obstacles = TextLine(
        title=_(u'Obstacles'),
        required=False
    )

    searchable('closures')
    closures = TextLine(
        title=_(u'Closures'),
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

    def details(self):
        fields = sorted(IRoadworksDirectoryItem.names())
        
        def title(field):
            return utils.translate(
                self.context, self.request, IRoadworksDirectoryItem[field].title
            )

        titles = dict(zip(fields, map(title, fields)))
        order = sorted(titles.values())

        for field in sorted(fields, key=lambda f: order.index(titles[f])):
            if getattr(self.context, field):
                yield titles[field], getattr(self.context, field)

class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of seantis.dir.roadworks.item."""
    grok.context(IRoadworksDirectory)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self, itemmap):
        itemmap.typename = 'seantis.dir.roadworks.item'
        itemmap.interface = IRoadworksDirectoryItem

        extended = [
            'project', 
            'road',
            'section',
            'works',
            'timespan',
            'obstacles',
            'closures',
            'constructor',
            'contact'
        ]
        
        itemmap.add_fields(extended, len(itemmap))

class RoadworkMapMarker(grok.Adapter):

    grok.context(IRoadworksDirectoryItem)
    grok.implements(IMapMarker)

    def url(self, letter):
        """
        Returns URL to a general marker image.
        """
        baseurl = self.context.absolute_url()
        imagedir = "/++resource++seantis.dir.roadworks.images"
        image = "/construction-marker.png"
        return baseurl + imagedir + image
