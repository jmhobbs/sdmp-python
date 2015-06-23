# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from hashlib import sha256


class Node (object):

    def __init__(self, private_key=None):
        self.private_key = private_key
        self.private_key_fingerprint = None
        if self.private_key:
            self._update_fingerprint()

    def load_private_key_from_file(self, private_key_path, private_key_passphrase=None):
        with open(private_key_path, 'rb') as key_handle:
            private_key = RSA.importKey(key_handle.read(), private_key_passphrase)
            if not private_key.has_private():
                raise exceptions.InvalidKeyException("Key can not sign. Private key required.")
            if private_key.size() < 2047:
                raise exceptions.InvalidKeyException("Key must be 2048 bits or larger.")
            self.private_key = private_key
            self._update_fingerprint()

    def _update_fingerprint(self):
        self.private_key_fingerprint = sha256(self.private_key.publickey().exportKey("DER")).hexdigest()
