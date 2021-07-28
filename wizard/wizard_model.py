# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_is_zero, pycompat
from odoo.addons import decimal_precision as dp
from datetime import date, timedelta
import os
import base64
import random
import string
from collections import defaultdict

class AccountMoveLineReconcileWizard(models.TransientModel):
    _name = 'account.move.line.reconcile.wizard'

    def btn_confirm(self):
        aml_ids = self.env.context.get('active_ids',[])
        if len(aml_ids) != 2:
            raise ValidationError('Deben seleccionarse por lo menos dos movimientos')
        amls = self.env['account.move.line']
        for aml in self.env['account.move.line'].browse(aml_ids):
            amls += aml
        amls.reconcile()
