from seantis.dir.roadworks.item import IRoadworksDirectoryItem
from seantis.dir.base.upgrades import add_behavior_to_item


def upgrade_to_1000(context):

    add_behavior_to_item(
        context, 'seantis.dir.roadworks', IRoadworksDirectoryItem
    )
