# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _

class StockMove(models.Model):
    _inherit = 'stock.move'

    def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id, svl_id, description):
        res = super(StockMove, self)._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id, svl_id, description)
        if len(res) > 1:
            if self.picking_id and self.picking_id.cuenta_analitica_id:
                res[0][2]['analytic_distribution'] = dict([(str(self.picking_id.cuenta_analitica_id.id), 100),])
                res[1][2]['analytic_distribution'] = dict([(str(self.picking_id.cuenta_analitica_id.id), 100),])

            if self.env.context.get('analytic_account_id', False):
                a = self.env.context.get('analytic_account_id')
                if a.id:
                    res[0][2]['analytic_distribution'] = dict([(str(a.id), 100),])
                    res[1][2]['analytic_distribution'] = dict([(str(a.id), 100),])

        return res

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cuenta_analitica_id = fields.Many2one('account.analytic.account', 'Cuenta analítica')
