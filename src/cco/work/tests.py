#! /usr/bin/python

"""
Tests for the 'cco.work' package.
"""

import os
import unittest, doctest
from zope import component
from zope.app.testing.setup import placefulSetUp, placefulTearDown

from loops.concept import Concept
from loops.setup import addAndConfigureObject
from loops.tests.setup import TestSite
from cco.work.interfaces import IProject
from cco.work.task import Project


def setupComponents(loopsRoot):
    component.provideAdapter(Project)


def setUp(self):
    site = placefulSetUp(True)
    t = TestSite(site)
    concepts, resources, views = t.setup()
    loopsRoot = site['loops']
    self.globs['loopsRoot'] = loopsRoot
    setupComponents(loopsRoot)
    addAndConfigureObject(concepts, Concept, 'project',
            title='Project', conceptType=concepts['type'],
            typeInterface=IProject)


def tearDown(self):
    placefulTearDown()


class Test(unittest.TestCase):
    "Basic tests."

    def testBasicStuff(self):
        pass


def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    return unittest.TestSuite((
        unittest.makeSuite(Test),
        doctest.DocFileSuite('README.md', optionflags=flags,
                     setUp=setUp, tearDown=tearDown),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
