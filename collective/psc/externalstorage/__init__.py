from zope.interface import implements

from Products.Archetypes.atapi import AttributeStorage

from Products.PloneSoftwareCenter.storage.interfaces import IPSCFileStorage
from Products.ExternalStorage.ExternalStorage import ExternalStorage as _E

from collective.psc.externalstorage.browser.config import grab_utility

class ExternalStorage(_E):
    """adapts a release folder as a dummy storage
    """
    name = 'externalstorage'
    implements(IPSCFileStorage)

    def __init__(self, context):
        _E.__init__(self, archive=False, rename=False)
        storage = grab_utility(context)
        self.prefix = storage.path
        self.context = context

    def getName(self):
        return self.name

    def _checkStorage(self, instance):
        if not self.isInitialized(instance):
            self.initializeStorage(instance)

    def get(self, name, instance, **kwargs):
        self._checkStorage(instance)
        return _E.get(self, name, instance, **kwargs)

    def set(self, name, instance, value, **kwargs):
        self._checkStorage(instance)
        return _E.set(self, name, instance, value, **kwargs)

    def unset(self, name, instance, **kwargs):
        self._checkStorage(instance)
        return _E.unset(self, name, instance, **kwargs)

