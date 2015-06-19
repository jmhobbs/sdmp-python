

class Resource (object):

    def __init__(self):
        self.sdmp_version = None
        self.sdmp_publisher = None
        self.sdmp_created = None
        self.sdmp_updates = None

    @property
    def message_digest(self):
        raise NotImplemented()


