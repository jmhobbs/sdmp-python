from collections import namedtuple
from hashlib import sha256


JournalEntry = namedtuple("JournalEntry", "resource_node_key_fingerprint, resource_identifier")


class Journal (object):

    def __init__(self, node_fingerprint):
        self.node_fingerprint = node_fingerprint
        self.journal_entries = []

    def append_entry(self, resource_node_key_fingerprint, resource_identifier):
        self.journal_entries.append(JournalEntry(resource_node_key_fingerprint, resource_identifier))

    def dump(self):
        lines = [self.node_fingerprint]

        for entry in self.journal_entries:
            journal_line_number = sha256(lines[len(lines)-1]).hexdigest()
            lines.append(journal_line_number + "@" +
                         entry.resource_node_key_fingerprint + "/" +
                         entry.resource_identifier)

        return "\n".join(lines)
