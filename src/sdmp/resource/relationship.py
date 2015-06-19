from .base import Resource


class RelationshipDocument (Resource):

    def __init__(self):
        super(Resource, self).__init__()
        self.sdmp_relationship_type = None


class ConnectionRelationshipDocument (RelationshipDocument):

    def __init__(self):
        super(RelationshipDocument, self).__init__()
        self.sdmp_relationship_type = "connection"
        self.sdmp_relationship_user = None


class HostRelationshipDocument (RelationshipDocument):

    def __init__(self):
        super(HostRelationshipDocument, self).__init__()
        self.sdmp_relationship_type = "host"
        self.sdmp_relationship_node = None


class PublisherRelationshipDocument (RelationshipDocument):

    def __init__(self):
        super(PublisherRelationshipDocument, self).__init__()
        self.sdmp_relationship_type = "publisher"
        self.sdmp_relationship_node = None
