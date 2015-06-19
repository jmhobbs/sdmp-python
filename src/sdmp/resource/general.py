from .base import Resource


class GeneralDocument (Resource):

    def __init__(self):
        super(GeneralDocument, self).__init__()


class UserInformationDocument (GeneralDocument):

    def __init__(self):
        super(UserInformationDocument, self).__init__()
        self.user_name = None
        self.user_about = None
