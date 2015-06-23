# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from hashlib import sha256


class InvalidKeyException (Exception):
    pass


def load_private_key_from_file(private_key_path, private_key_passphrase=None):
    with open(private_key_path, 'rb') as key_handle:
        private_key = RSA.importKey(key_handle.read(), private_key_passphrase)
        if not private_key.has_private():
            raise InvalidKeyException("Key can not sign. Private key required.")
        if private_key.size() < 2047:
            raise InvalidKeyException("Key must be 2048 bits or larger.")
        return private_key


def fingerprint_key(key):
    return sha256(key.publickey().exportKey("DER")).hexdigest()
