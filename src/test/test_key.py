# -*- coding: utf-8 -*-

import unittest
import sdmp.key
import os.path


class TestKey (unittest.TestCase):

    def test_small_key(self):
        self.assertRaises(sdmp.key.InvalidKeyException,
                          sdmp.key.load_private_key_from_file,
                          os.path.join(os.path.dirname(__file__), "keys", "private_key_512.pem")
                          )

    def test_public_key(self):
        self.assertRaises(sdmp.key.InvalidKeyException,
                          sdmp.key.load_private_key_from_file,
                          os.path.join(os.path.dirname(__file__), "keys", "public_key.pem")
                          )

    def test_valid_key(self):
        self.assertIsNotNone(sdmp.key.load_private_key_from_file(
            os.path.join(os.path.dirname(__file__), "keys", "private_key.pem")
        ))

    def test_fingerprint(self):
        key = sdmp.key.load_private_key_from_file(os.path.join(os.path.dirname(__file__), "keys", "private_key.pem"))
        # Test value derivation:
        #
        # $ openssl rsa -in private_key.pem -pubout -outform DER -out public_key_to_fingerprint.der
        # writing RSA key
        # $ openssl dgst -sha256 public_key_to_fingerprint.der
        # SHA256(public_key_to_fingerprint.der)= 0961ec2c63511f681e97f0d92e790ab579667493541963701bb44fd28e9c742d
        #
        self.assertEqual("0961ec2c63511f681e97f0d92e790ab579667493541963701bb44fd28e9c742d", sdmp.key.fingerprint_key(key))
