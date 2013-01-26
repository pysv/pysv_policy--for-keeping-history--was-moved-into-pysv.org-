from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from zope.interface import implements
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema
    

visibility_options = SimpleVocabulary([
    SimpleTerm(value='Niemanden', title=u'Niemanden'),
    SimpleTerm(value='Vereinsmitglieder', title=u'Verseinsmitglieder'),
    SimpleTerm(value='Jeden', title=u'Jeden'),
    ])

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema and add
    some further
    """
    isVisibleFor = schema.Choice(
        title=u'label_isVisible',
        description=u'help_visibility',
        vocabulary = visibility_options,
        required=True,
    )