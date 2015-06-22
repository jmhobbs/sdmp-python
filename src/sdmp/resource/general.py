from .base import Resource


class GeneralDocument (Resource):

    def __init__(self):
        super(GeneralDocument, self).__init__()
        self.document = {}


class UserInformationDocument (GeneralDocument):

    def __init__(self):
        super(UserInformationDocument, self).__init__()
        self.user_name = None
        self.user_about = None

class NodeInformationDocument (GeneralDocument):

    def __init__(self):
        super(NodeInformationDocument, self).__init__()
        self.node_name = None
        self.node_ips = []


class EncryptedContentDocument (GeneralDocument):

    def __init__(self):
        super(EncryptedContentDocument, self).__init__()
        self.encrypted_keys = []
        self.encrypted_data = []
