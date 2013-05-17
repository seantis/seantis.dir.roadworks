import imghdr
from five import grok
from zope.schema import TextLine
from zope.schema.interfaces import IText
from zope.interface import Invalid
from plone.namedfile.field import NamedFile
from plone.namedfile.field import NamedImage
from plone.directives import form
from collective.dexteritytextindexer import searchable

from seantis.dir.base import item
from seantis.dir.base import core
from seantis.dir.base import utils
from seantis.dir.base.interfaces import (
    IFieldMapExtender, IDirectoryItem, IMapMarker
)

from seantis.dir.roadworks.directory import IRoadworksDirectory
from seantis.dir.roadworks import _


class IRoadworksDirectoryItem(IDirectoryItem):
    """Extends the seantis.dir.IDirectoryItem."""

    searchable('project')
    project = TextLine(
        title=_(u'Project'),
        required=False
    )

    searchable('section')
    section = TextLine(
        title=_(u'Section'),
        required=False
    )

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

    image = NamedImage(
        title=_(u'Image'),
        required=False,
        default=None
    )

    attachment = NamedFile(
        title=_(u'Attachment'),
        required=False
    )


# Ensure that the uploaded image at least has an image header.
@form.validator(field=IRoadworksDirectoryItem['image'])
def validate_image(value):
    if not value:
        return

    if not imghdr.what(value.filename, value.data):
        raise Invalid(_(u'Unknown image format'))


class RoadworksDirectoryItem(item.DirectoryItem):
    pass


class View(core.View):
    """Default view of a seantis.dir.roadworks item."""
    grok.context(IRoadworksDirectoryItem)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/item.pt')

    def details(self):
        fields = IRoadworksDirectoryItem.names()

        def title(field):
            return utils.translate(
                self.context, self.request,
                IRoadworksDirectoryItem[field].title
            )

        titles = dict(zip(fields, map(title, fields)))

        items = []
        order = lambda f: IRoadworksDirectoryItem.get(f).order
        for field in sorted(fields, key=order):
            # Show only fields whose string representation makes sense.
            if (IText.providedBy(IRoadworksDirectoryItem[field]) and
                    getattr(self.context, field)):
                items.append((titles[field], getattr(self.context, field)))

        if self.context.attachment:
            attachment = self.context.attachment
            link = '<a href="%s/@@download/attachment">%s (%s KB)</a>' % (
                self.context.absolute_url(),
                attachment.filename,
                attachment.getSize() / 1024
            )
            items.append((titles['attachment'], link))

        return items


class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of
    seantis.dir.roadworks.item.

    """
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
