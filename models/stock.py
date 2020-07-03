# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _

class StockMove(models.Model):
    _inherit = 'stock.move'

    def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id, description):
        res = super(StockMove, self)._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id, description)
        if len(res) > 1:
            if self.picking_id and self.picking_id.cuenta_analitica_id:
                res[0][2]['analytic_account_id'] = self.picking_id.cuenta_analitica_id.id
                res[1][2]['analytic_account_id'] = self.picking_id.cuenta_analitica_id.id

            if self.inventory_id and self.inventory_id.cuenta_analitica_id:
                res[0][2]['analytic_account_id'] = self.inventory_id.cuenta_analitica_id.id
                res[1][2]['analytic_account_id'] = self.inventory_id.cuenta_analitica_id.id

            if self.env.context.get('analytic_account_id', False):
                a = self.env.context.get('analytic_account_id')
                if a.id:
                    res[0][2]['analytic_account_id'] = a.id
                    res[1][2]['analytic_account_id'] = a.id

        return res

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cuenta_analitica_id = fields.Many2one('account.analytic.account', 'Cuenta analítica')

class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    @api.model
    def _default_cuenta_analitica_id(self):
        user = self.env.user

        if 'default_analytic_account_id' in user.fields_get() and user.default_analytic_account_id:
            return user['default_analytic_account_id'].id
        else:
            return False

    cuenta_analitica_id = fields.Many2one('account.analytic.account', 'Cuenta analítica', default=_default_cuenta_analitica_id)
