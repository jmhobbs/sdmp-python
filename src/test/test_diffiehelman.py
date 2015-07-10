# -*- coding: utf-8 -*-

import unittest
import sdmp.diffiehelman


class TestKey (unittest.TestCase):

    def test_sanity(self):
        alice = sdmp.diffiehelman.DiffieHelmanExchange()
        bob = sdmp.diffiehelman.DiffieHelmanExchange(alice.p, alice.g)
        self.assertEqual(alice.getSharedSecret(bob.publicKey),
                         bob.getSharedSecret(alice.publicKey))
