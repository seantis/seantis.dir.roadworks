from five import grok
from zope.interface import alsoProvides
from plone.namedfile.field import NamedImage
from plone.autoform.interfaces import IFormFieldProvider
from plone.app.dexterity.behaviors.metadata import MetadataBase
from plone.app.dexterity.behaviors.metadata import DCFieldProperty
from plone.directives import form

from seantis.dir.base.directory import IDirectory
from seantis.dir.base.directory import DirectoryViewletManager

class IExtendedDirectory(form.Schema):
    """Extends the seantis.dir.base.directory.IDirectory"""
    pass

alsoProvides(IExtendedDirectory, IFormFieldProvider)

class ExtendedDirectory(MetadataBase):
    pass

class ExtendedDirectoryViewlet(grok.Viewlet):
    grok.context(IDirectory)
    grok.name('seantis.dir.base.directory.detail')
    grok.require('zope2.View')
    grok.viewletmanager(DirectoryViewletManager)

    template = grok.PageTemplateFile('templates/directorydetail.pt')
