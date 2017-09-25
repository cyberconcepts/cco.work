#
#  Copyright (c) 2016 Helmut Merz helmutm@cy55.de
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
Report class(es) for the cco.work package.
"""

from cybertools.util.jeep import Jeep
from loops.expert.field import Field, DecimalField, TargetField, UrlField
from loops.expert.report import ReportInstance
from loops.organize.work.report import DurationField


task = UrlField('title', u'Task',
                executionSteps=['sort', 'output'])
estimatedEffort = DecimalField('estimatedEffort', u'Estimated Effort',
                executionSteps=['output'])
actualEffort = DecimalField('actualEffort', u'Actual Effort',
                executionSteps=['output'])


class TasksOverview(ReportInstance):

    type = 'cco.work.tasks_overview'
    label = u'Tasks Overview'

    fields = Jeep((task,))
    defaultOutputFields = fields
    defaultSortCriteria = (task,)

    def selectObjects(self, parts):
        return []