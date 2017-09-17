#! /usr/bin/python

"""
Tests for the 'cco.work' package.
"""

import os
import unittest, doctest
from zope import component
from zope.app.testing.setup import placefulSetUp, placefulTearDown

from cybertools.organize.work import workItemStates
from cybertools.tracking.btree import TrackingStorage
from loops.concept import Concept
from loops.organize.work.base import WorkItem, WorkItems
from loops.setup import addAndConfigureObject
from loops.tests.setup import TestSite
from cco.work.interfaces import IProject, ITask
from cco.work.task import Project, Task


def setupComponents(loopsRoot):
    component.provideAdapter(WorkItems)
    component.provideUtility(workItemStates(), name='organize.workItemStates')
    component.provideAdapter(Project)
    component.provideAdapter(Task)


def setUp(self):
    site = placefulSetUp(True)
    t = TestSite(site)
    concepts, resources, views = t.setup()
    loopsRoot = site['loops']
    self.globs['loopsRoot'] = loopsRoot
    setupComponents(loopsRoot)
    records = loopsRoot.getRecordManager()
    if 'work' not in records:
        records['work'] = TrackingStorage(trackFactory=WorkItem)
    addAndConfigureObject(concepts, Concept, 'project',
            title='Project', conceptType=concepts['type'],
            typeInterface=IProject)
    addAndConfigureObject(concepts, Concept, 'task',
            title='Task', conceptType=concepts['type'],
            typeInterface=ITask)


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
