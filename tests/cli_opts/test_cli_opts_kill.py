"""
This module is the test suite of the kill CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import pytest

from docker import client
from bowl.cli_opts import kill

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the kill CLI option.
    """
    def test_cli_opts_kill(self):
        args = Object()
        args.CONTAINER = "test"
        args.z = True
        a = kill.kill()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
