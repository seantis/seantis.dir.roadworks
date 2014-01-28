from zope.security.management import newInteraction, endInteraction

from seantis.plonetools.testing import TestCase
from seantis.dir.roadworks.testing import (
    INTEGRATION_TESTING,
    FUNCTIONAL_TESTING
)


# to use with integration where security interactions need to be done manually
class IntegrationTestCase(TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        newInteraction()

    def tearDown(self):
        endInteraction()
        super(IntegrationTestCase, self).tearDown()


# to use with the browser which does its own security interactions
class FunctionalTestCase(TestCase):
    layer = FUNCTIONAL_TESTING
