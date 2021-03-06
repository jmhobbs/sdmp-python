import unittest
from sdmp.journal import Journal

expected_journal_1 = """NODE_KEY_FINGERPRINT
95415d7306a28cdcee190d93b1b095a0618b8538f30970676fdb67a8e7fb13ea@RESOURCE_NODE_KEY_FINGERPRINT_1/RESOURCE_IDENTIFIER_1
3d6798c1ed9c69a463c211b220645c781d34621b7add8911c10f95a9bcd6c09e@RESOURCE_NODE_KEY_FINGERPRINT_1/RESOURCE_IDENTIFIER_2
1b790430234a835a222d07a2636f88e202c20ada5e6f6610830993131797acaa@RESOURCE_NODE_KEY_FINGERPRINT_3/RESOURCE_IDENTIFIER_3"""

expected_journal_2 = """7a5179eecc0fe18760ba615f92603372ae3fe302860098a019e15927551fee3b
1467d232075b693bd528521179679ec07a083e4f0076ecd2af61607d6b5b2b38@d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75/ad700edf9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743
7f6b5d882777fa3620c2a0c86c31537b30cbfaa55f09fb948c9ed491e0968fce@d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75/9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743ad700edf"""


class TestJournal (unittest.TestCase):

    def test_sanity(self):
        """Check against provided test vectors and our own."""
        journal = Journal("7a5179eecc0fe18760ba615f92603372ae3fe302860098a019e15927551fee3b")
        journal.append_entry("d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75", "ad700edf9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743")
        journal.append_entry("d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75", "9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743ad700edf")
        self.assertEqual(expected_journal_2, journal.dump())

        journal = Journal("NODE_KEY_FINGERPRINT")
        journal.append_entry("RESOURCE_NODE_KEY_FINGERPRINT_1", "RESOURCE_IDENTIFIER_1")
        journal.append_entry("RESOURCE_NODE_KEY_FINGERPRINT_1", "RESOURCE_IDENTIFIER_2")
        journal.append_entry("RESOURCE_NODE_KEY_FINGERPRINT_3", "RESOURCE_IDENTIFIER_3")
        self.assertEqual(expected_journal_1, journal.dump())

    def test_entries(self):
        journal = Journal("7a5179eecc0fe18760ba615f92603372ae3fe302860098a019e15927551fee3b")
        journal.append_entry("d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75", "ad700edf9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743")
        journal.append_entry("d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75", "9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743ad700edf")

        journal_lines = [
            u"7a5179eecc0fe18760ba615f92603372ae3fe302860098a019e15927551fee3b",
            u"1467d232075b693bd528521179679ec07a083e4f0076ecd2af61607d6b5b2b38@d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75/ad700edf9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743",
            u"7f6b5d882777fa3620c2a0c86c31537b30cbfaa55f09fb948c9ed491e0968fce@d341ba4104e7c004c2fe56d65636b945b57550081711a1d306a9f41d2b440c75/9094f10db2f4e56185645fd3630bbbab832d6f659dad08f0d9f43743ad700edf"
        ]

        entries = journal.entries("7a5179eecc0fe18760ba615f92603372ae3fe302860098a019e15927551fee3b")
        self.assertEqual(entries, journal_lines[1:])

        entries = journal.entries("1467d232075b693bd528521179679ec07a083e4f0076ecd2af61607d6b5b2b38")
        self.assertEqual(entries, journal_lines[2:])

        entries = journal.entries("7f6b5d882777fa3620c2a0c86c31537b30cbfaa55f09fb948c9ed491e0968fce")
        self.assertEqual(entries, [])
