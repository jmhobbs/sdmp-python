# -*- coding: utf-8 -*-

from .key import load_private_key_from_file, fingerprint_key

class Node (object):

    def __init__(self, private_key=None):
        self.private_key = private_key
        self.key_fingerprint = None
        if self.private_key:
            self.key_fingerprint = fingerprint_key(self.private_key)

    def load_private_key_from_file(self, private_key_path, private_key_passphrase=None):
        self.private_key = load_private_key_from_file(private_key_path, private_key_passphrase)
        self.key_fingerprint = fingerprint_key(self.private_key)
