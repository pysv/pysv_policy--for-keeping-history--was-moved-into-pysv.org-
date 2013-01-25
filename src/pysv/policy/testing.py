from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PysvPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import pysv.policy
        xmlconfig.file('configure.zcml',
                       pysv.policy,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pysv.policy:default')

PYSV_POLICY_FIXTURE = PysvPolicy()
PYSV_POLICY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PYSV_POLICY_FIXTURE, ),
                       name="PysvPolicy:Integration")