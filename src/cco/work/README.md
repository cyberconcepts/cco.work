
cco.work - cyberconcepts.org: project and task management stuff
===============================================================

  >>> from zope.publisher.browser import TestRequest
  >>> from logging import getLogger
  >>> log = getLogger('cco.work')

  >>> from loops.setup import addAndConfigureObject, addObject
  >>> from loops.concept import Concept
  >>> from loops.common import adapted, baseObject

  >>> concepts = loopsRoot['concepts']
  >>> len(list(concepts.keys()))
  12

  >>> project = concepts['project']
  >>> task = concepts['task']

  >>> from loops.browser.node import NodeView
  >>> home = loopsRoot['views']['home']
  >>> homeView = NodeView(home, TestRequest())


Projects
--------

### Basic operations ###

We start with creating a project and assigning an estimated effort to it.

  >>> from loops.concept import Concept
  >>> from loops.setup import addAndConfigureObject

  >>> proj01 = adapted(addAndConfigureObject(concepts, Concept, 'project01', 
  ...             title=u'Project #1', conceptType=project))

  >>> proj01.estimatedEffort = 100

When counting all assoctioated tasks we get just 1, the project itself.

  >>> len(proj01.getAllTasks())
  1

We now add a task to the project so that we now count two tasks 
(including the project itself).

  >>> task01 = adapted(addAndConfigureObject(concepts, Concept, 'task01', 
  ...             title=u'Task #1', conceptType=task))
  >>> baseObject(task01).assignParent(baseObject(proj01))
  >>> len(proj01.getAllTasks())
  2

The actual effort for the project is 0.0 because there aren't any work items
assigned to any of the tasks.
  
  >>> proj01.actualEffort
  u'0:00'

So if we add work items the corresponding efforts are summed up.

  >>> task01.addWorkItem('4711', 'work', effort=15 * 3600)
  >>> proj01.actualEffort
  u'15:00'

  >>> task02 = adapted(addAndConfigureObject(concepts, Concept, 'task02', 
  ...             title=u'Task #2', conceptType=task))
  >>> baseObject(task02).assignParent(baseObject(proj01))
  >>> task02.addWorkItem('4711', 'work', effort=8 * 3600)
  >>> proj01.actualEffort
  u'23:00'
