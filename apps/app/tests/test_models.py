# coding: utf-8
from datetime import datetime, timedelta
import unittest

from apps.utils.tests.base import MongoEngineTestCase
from ..models import *


class AlgorithmTests(unittest.TestCase):
    def test_(self):
        self.assertEquals(True, True)


class MyDocTests(MongoEngineTestCase):
    def test_(self):
        self.assertEquals(True, True)


