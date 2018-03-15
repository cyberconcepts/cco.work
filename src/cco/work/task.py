#
#  Copyright (c) 2017 Helmut Merz helmutm@cy55.de
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

"""
Implementation of cco.work concepts.
"""

from zope.cachedescriptors.property import Lazy
from zope.interface import implements

from cybertools.organize.interfaces import IWorkItems
from loops.common import AdapterBase, adapted, baseObject
from loops.type import TypeInterfaceSourceList
from loops import util
from cco.work.interfaces import IProject, ITask


TypeInterfaceSourceList.typeInterfaces += (IProject, ITask)


class TaskBase(AdapterBase):

    start = end = None

    defaultStates = ['done', 'done_x', 'finished', 'finished_x']

    @property
    def actualEffort(self):
        result = 0.0
        for t in self.getAllTasks():
            for wi in t.getWorkItems():
                result += wi.effort
        return result

    def getSubTasks(self):
        result = []
        for c in baseObject(self).getChildren():
            obj = adapted(c)
            if IProject.providedBy(obj) or ITask.providedBy(obj):
                result.append(obj)
        return result

    def getAllTasks(self):
        if self.__is_dummy__:
            return []
        result = set([self])
        for t1 in self.getSubTasks():
            if t1 not in result:
                for t2 in t1.getAllTasks():
                    if t2 not in result:
                        result.add(t2)
        return result

    @Lazy
    def workItems(self):
        rm = self.getLoopsRoot().getRecordManager()
        return IWorkItems(rm['work'])

    def addWorkItem(self, party, action='plan', **kw):
        wi = self.workItems.add(util.getUidForObject(baseObject(self)), party)
        wi.doAction(action, party, **kw)

    def getWorkItems(self, crit={}):
        kw = dict(task=util.getUidForObject(baseObject(self)), 
                  state=crit.get('states') or self.defaultStates)
        return self.workItems.query(**kw)


class Project(TaskBase):
    """ Adapter for concepts of a project type
        with additional fields for planning/controlling.
    """

    implements(IProject)

    _adapterAttributes = AdapterBase._adapterAttributes + (
            'estimatedEffort', 'chargedEffort', 'actualEffort',)
    _contextAttributes = list(IProject)

    @property
    def estimatedEffort(self):
        return sum(float(t.estimatedEffort or 0.0) for t in self.getSubTasks())

    @property
    def chargedEffort(self):
        return sum(float(t.chargedEffort or 0.0) for t in self.getSubTasks())


class Task(TaskBase):
    """ Adapter for concepts of a task type
        with additional fields for planning/controlling.
    """

    implements(ITask)

    #estimatedEffort = chargedEffort = 0.0

    _adapterAttributes = AdapterBase._adapterAttributes + ('actualEffort',)
    _contextAttributes = list(ITask)

