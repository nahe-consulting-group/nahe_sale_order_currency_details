from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_total_company_currency = fields.Monetary(compute='_compute_amount_total_company_currency', readonly=True, currency_field='company_id.currency_id')

    @api.depends('amount_total', 'pricelist_id.currency_id', 'company_id.currency_id')
    def _compute_amount_total_company_currency(self):
        for order in self:
            currency_rate = order.pricelist_id.currency_id.with_context(date=order.date_order).rate
            order.amount_total_company_currency = order.amount_total / currency_rate if currency_rate else 0
