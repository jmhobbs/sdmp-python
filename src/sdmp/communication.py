

class StatusCode (object):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408


STATUS_CODES = {
    StatusCode.BAD_REQUEST: "Bad request",
    StatusCode.NOT_FOUND: "Not found",
    StatusCode.REQUEST_TIMEOUT: "Request timeout"
}


class CommunicationDocument (object):

    def __init__(self):
        self.communication = {}


class NodeResponse (CommunicationDocument):

    def __init__(self, status_code, request=None):
        super(NodeResponse, self).__init__()
        self.communication["response"] = {"status": status_code}
        self.communication["description"] = STATUS_CODES[status_code]
        if request:
            self.communication["response"]["request"] = request


class JournalListRequest (CommunicationDocument):

    def __init__(self, since, limit=None):
        super(JournalListRequest, self).__init__()
        self.communication["synchronize"] = {"since": since}
        if limit:
            self.communication["synchronize"]["limit"] = limit


class JournalListResponse (CommunicationDocument):

    def __init__(self, journal, since, limit=None):
        super(JournalListResponse, self).__init__()
        self.communication["journal"] = {"since": since}
        self.communication["journal"]["entries"] = journal.entries(since, limit)


class ResourceRequest (CommunicationDocument):

    def __init__(self, user_key_fingerprint, resource_identifier):
        super(ResourceRequest, self).__init__()
        self.communication["request"] = {
            "author": user_key_fingerprint,
            "resource": resource_identifier
        }
