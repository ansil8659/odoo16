from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    credit_journal = fields.Boolean("credit")


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Boolean("Credit Limit")
    warn_amount = fields.Float("Warning Amount")
    block_amount = fields.Float("Blocking Amount")
    credit_amount = fields.Float("Credit", compute='_compute_credit_amount')

    # @api.onchange('credit_limit')
    @api.model
    @api.depends('credit_amount')
    def _compute_credit_amount(self):
        for data in self:
            print('hai',data)
            data.credit_amount = 0

            method = self.env['pos.payment.method'].search([('name', '=', 'Credit')])
            print(method)
            amount_id = self.env['pos.payment'].search([('payment_method_id', '=', method.id), ('pos_order_id.partner_id', '=', data.id)])   # main = 0
            print(amount_id)
            for rec in amount_id:
                print(rec.amount)
                data.credit_amount = (data.credit_amount + rec.amount)
            print(data.credit_amount)

    # def dynamic_update(self, id, amount):
    #     print(id,".....", amount)
    #     customer = self.env['res.partner'].search([('id', '=', id)])
    #     for rec in customer:
    #         customer.credit_amount += amount

