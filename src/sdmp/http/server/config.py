# -*- coding: utf-8 -*-


class BaseConfig(object):
    ENV = 'PRODUCTION'
    TESTING = False
    DEBUG = False


class TestConfig(BaseConfig):
    ENV = 'TESTING'
    TESTING = True
