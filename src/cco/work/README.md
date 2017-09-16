
cco.work - cyberconcepts.org: project and task management stuff
===============================================================

  >>> from zope.publisher.browser import TestRequest
  >>> from logging import getLogger
  >>> log = getLogger('cco.work')

  >>> from loops.setup import addAndConfigureObject, addObject
  >>> from loops.concept import Concept
  >>> from loops.common import adapted

  >>> concepts = loopsRoot['concepts']
  >>> len(list(concepts.keys()))
  11

  >>> project = concepts['project']

  >>> from loops.browser.node import NodeView
  >>> home = loopsRoot['views']['home']
  >>> homeView = NodeView(home, TestRequest())


Projects
--------

### Basic operations ###

  >>> from loops.concept import Concept
  >>> from loops.setup import addAndConfigureObject

  >>> proj01 = adapted(addAndConfigureObject(concepts, Concept, 'project01', 
  ...             title=u'Project #1', conceptType=project))

  >>> proj01.estimatedEffort = 100

  >>> len(proj01.getAllTasks())
  1
  
  >>> proj01.actualEffort
  0
