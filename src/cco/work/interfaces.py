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
Interfaces for organizational stuff like persons and addresses.
"""

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface, Attribute
from zope import interface, component, schema

from cybertools.organize.interfaces import ITask
from loops.interfaces import ILoopsAdapter, IConceptSchema


_ = MessageFactory('cco.work')


# project and task management

class IProject(ILoopsAdapter):

    estimatedEffort = schema.Int(
                title=_(u'label_estimatedEffort'),
                description=_(u'desc_estimatedEffort'),
                required=False,)
    quotedEffort = schema.Int(
                title=_(u'label_quotedEffort'),
                description=_(u'desc_quotedEffort'),
                required=False,)
    actualEffort = schema.Int(
                title=_(u'label_actualEffort'),
                description=_(u'desc_actualEffort'),
                readonly=True)


class ITask(IConceptSchema, ITask, ILoopsAdapter):

    pass

