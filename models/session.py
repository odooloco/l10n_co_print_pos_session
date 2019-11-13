# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
#                                                                             #
# Part of Odoo. See LICENSE file for full copyright and licensing details.    #
#                                                                             #
#                                                                             #
# Copyright (C) 2016  Dominic Krimmer                                         #
#                     Luis Alfredo da Silva (luis.adasilvaf@gmail.com)        #
#                     Diego Carvajal, diegoivanc@gmail.com                    #
#                                                                             #
# Co-Authors    Odoo LoCo                                                     #
#               Localización funcional de Odoo para Colombia                  #
#                                                                             #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################


import logging
import time

import odoo.addons.decimal_precision as dp
from odoo import tools, models, SUPERUSER_ID
from odoo import fields, api
from odoo.tools import float_is_zero
from odoo.tools.translate import _
from odoo.exceptions import UserError
from datetime import datetime

from uuid import getnode as get_mac
from odoo import api, fields as Fields
import locale
from odoo.tools.misc import formatLang
from odoo.osv import osv

_logger = logging.getLogger(__name__)

class pos_session(models.Model):
    _inherit = 'pos.session'

    @api.one
    def first_orden(self):
        res = {}
        _order_first = False
        i = -1
        if self.order_ids:
            for order in self.order_ids:
                if self.order_ids[i].type != 'out_refund':
                    _order_first = self.order_ids[i].name
                    break
                else:
                    i = i - 1

        return _order_first

    @api.one
    def ultima_orden(self):
        res = {}
        _order_end = False
        i = 0
        if self.order_ids:
            for order in self.order_ids:
                _logger.info(self.order_ids[i])
                if self.order_ids[i].type != 'out_refund':
                    _order_end = self.order_ids[i].name
                    break
                else:
                    i = i + 1

        return _order_end