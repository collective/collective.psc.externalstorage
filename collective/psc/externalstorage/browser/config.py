from zope.formlib import form
from zope.component import getUtility
from zope.i18nmessageid import MessageFactory
from Products.Five.formlib import formbase

from collective.psc.externalstorage.interfaces import IESConfiguration

_ = MessageFactory('collective_psc_externalstorage')

class ESConfigurationForm(formbase.EditFormBase):

    form_fields = form.Fields(IESConfiguration)
    label = _(u"Settings for External storage")

def grab_utility(context):
    return getUtility(IESConfiguration)

