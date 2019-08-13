# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from datetime import datetime
from odoo.exceptions import UserError, ValidationError
import base64
from base64 import b64encode
import os
from reportlab.graphics import barcode
from fnmatch import fnmatch
import logging
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF_DATE


_logger = logging.getLogger(__name__)


class Hr_employee_code(models.Model):
    _name = 'hr.employee'
    _inherit  = 'hr.employee'

    code_ref = fields.Char(string = 'Internal reference', required=True)
    
    _sql_constraints = [
                     ('code_ref_unique', 
                      'unique(code_ref)',
                      _('Choose another value - it has to be unique!'))
    ]