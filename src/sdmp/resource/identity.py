from .base import Resource


class IdentityDocument (Resource):

    def __init__(self):
        super(IdentityDocument, self).__init__()
        self.sdmp_identity_type = None
        self.sdmp_identity_expires = None
        self.sdmp_identity_key = None


class NodeIdentityDocument (IdentityDocument):

    def __init__(self):
        super(UserIdentityDocument, self).__init__()
        self.sdmp_identity_type = "node"


class UserIdentityDocument (IdentityDocument):

    def __init__(self):
        super(UserIdentityDocument, self).__init__()
        self.sdmp_identity_type = "user"
