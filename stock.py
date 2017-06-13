# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
import openerp.addons.decimal_precision as dp

class stock_quant(osv.osv):
    _inherit = 'stock.quant'

    def _prepare_account_move_line(self, cr, uid, move, qty, cost, credit_account_id, debit_account_id, context=None):
        res = super(stock_quant, self)._prepare_account_move_line(cr, uid, move, qty, cost, credit_account_id, debit_account_id, context=context)
        if move.picking_id and move.picking_id.cuenta_analitica:
            res[0][2]['analytic_account_id'] = move.picking_id.cuenta_analitica.id
            res[1][2]['analytic_account_id'] = move.picking_id.cuenta_analitica.id
        return res

class stock_picking(osv.osv):
    _inherit = 'stock.picking'

    _columns = {
        'cuenta_analitica': fields.many2one('account.analytic.account', 'Cuenta analítica'),
    }
