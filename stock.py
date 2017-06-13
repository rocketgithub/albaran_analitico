# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id):
        res = super(stock_quant, self)._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id)
        if self.picking_id and self.picking_id.cuenta_analitica:
            res[0][2]['analytic_account_id'] = self.picking_id.cuenta_analitica.id
            res[1][2]['analytic_account_id'] = self.picking_id.cuenta_analitica.id
        return res

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cuenta_analitica = fields.Many2one('account.analytic.account', 'Cuenta analítica'),
