from seantis.dir.base.setuphandlers import get_fti, add_behavior

def installBehavior(context):
    """Registers behaviors for seantis.dir.base.item."""

    fti = get_fti('seantis.dir.base.item')
    add_behavior(fti, 'seantis.dir.roadworks.item.IRoadworksDirectoryItem')

    fti = get_fti('seantis.dir.base.directory')
    add_behavior(fti, 'seantis.dir.roadworks.directory.IRoadworksDirectory')