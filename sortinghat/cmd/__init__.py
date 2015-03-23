# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2015 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#     Santiago Dueñas <sduenas@bitergia.com>
#

from sortinghat.cmd.add import Add
from sortinghat.cmd.affiliate import Affiliate
from sortinghat.cmd.config import Config
from sortinghat.cmd.enroll import Enroll
from sortinghat.cmd.export import Export
from sortinghat.cmd.init import Init
from sortinghat.cmd.load import Load
from sortinghat.cmd.log import Log
from sortinghat.cmd.merge import Merge
from sortinghat.cmd.move import Move
from sortinghat.cmd.organizations import Organizations
from sortinghat.cmd.remove import Remove
from sortinghat.cmd.show import Show
from sortinghat.cmd.unify import Unify
from sortinghat.cmd.withdraw import Withdraw


SORTINGHAT_COMMANDS = {
                       'add'       : Add,
                       'affiliate' : Affiliate,
                       'config'    : Config,
                       'enroll'    : Enroll,
                       'export'    : Export,
                       'init'      : Init,
                       'load'      : Load,
                       'log'       : Log,
                       'merge'     : Merge,
                       'mv'        : Move,
                       'orgs'      : Organizations,
                       'rm'        : Remove,
                       'show'      : Show,
                       'unify'     : Unify,
                       'withdraw'  : Withdraw,
                       }
