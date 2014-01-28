from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import quickInstallProduct

from plone.testing import z2
from Testing import ZopeTestCase


class TestLayer(PloneSandboxLayer):

    default_bases = (PLONE_FIXTURE,)

    class Session(dict):
        def set(self, key, value):
            self[key] = value

    def setUpZope(self, app, configurationContext):

        # Set up sessioning objects
        app.REQUEST['SESSION'] = self.Session()
        ZopeTestCase.utils.setupCoreSessions(app)

        import seantis.dir.roadworks
        self.loadZCML(package=seantis.dir.roadworks)

    def setUpPloneSite(self, portal):
        quickInstallProduct(portal, 'seantis.dir.roadworks')
        applyProfile(portal, 'seantis.dir.roadworks:default')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'seantis.dir.roadworks')


TESTFIXTURE = TestLayer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(TESTFIXTURE, ),
    name="Testfixture:Integration"
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TESTFIXTURE, ),
    name="Testfixture:Functional"
)
