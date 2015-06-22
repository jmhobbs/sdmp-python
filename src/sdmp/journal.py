from hashlib import sha256


class JournalEntry (object):

    def __init__(self, journal_line_number, resource_node_key_fingerprint, resource_identifier):
        self.journal_line_number = journal_line_number
        self.resource_node_key_fingerprint = resource_node_key_fingerprint
        self.resource_identifier = resource_identifier

    def __unicode__(self):
        return u"%s@%s/%s" % (self.journal_line_number,
                              self.resource_node_key_fingerprint,
                              self.resource_identifier)

    def __str__(self):
        return str(unicode(self))


class Journal (object):

    def __init__(self, node_fingerprint):
        self.node_fingerprint = node_fingerprint
        self.journal_entries = []

    def append_entry(self, resource_node_key_fingerprint, resource_identifier):
        if self.journal_entries:
            journal_line_number = sha256(unicode(self.journal_entries[-1])).hexdigest()
        else:
            journal_line_number = sha256(self.node_fingerprint).hexdigest()
        self.journal_entries.append(JournalEntry(journal_line_number, resource_node_key_fingerprint, resource_identifier))

    def entries(self, since):
        if since == self.node_fingerprint:
            return [unicode(e) for e in self.journal_entries]

        offset = 0
        found = False
        for entry in self.journal_entries:
            offset += 1
            if since == entry.journal_line_number:
                found = True
                break

        if not found:
            raise Exception("Journal Line Number Not Found: %s" % since)

        return [unicode(e) for e in self.journal_entries[offset:]]

    def dump(self):
        lines = [self.node_fingerprint]
        lines.extend(self.entries(self.node_fingerprint))
        return "\n".join(lines)
