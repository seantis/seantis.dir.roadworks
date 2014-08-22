from Products.CMFCore.utils import getToolByName

from seantis.dir.roadworks.directory import IRoadworksDirectory
from seantis.dir.roadworks.item import IRoadworksDirectoryItem
from seantis.dir.base.upgrades import (
    add_behavior_to_item,
    reset_images_and_attachments
)


def upgrade_to_1000(context):

    # add the new index first as the next step also does a reindex of all items
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-seantis.dir.roadworks:default', 'catalog'
    )

    reset_images_and_attachments(
        context, (IRoadworksDirectory, IRoadworksDirectoryItem)
    )

    add_behavior_to_item(
        context, 'seantis.dir.roadworks', IRoadworksDirectoryItem
    )


def upgrade_1000_to_1001(context):
    # add collective.geo.behaviour
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(
        'profile-collective.geo.behaviour:default'
    )

    add_behavior_to_item(
        context, 'seantis.dir.roadworks', IRoadworksDirectoryItem
    )

    # update css and js
    getToolByName(context, 'portal_css').cookResources()
    getToolByName(context, 'portal_javascripts').cookResources()


def upgrade_1001_to_1002(context):
    # update types
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-seantis.dir.roadworks:default', 'typeinfo'
    )
