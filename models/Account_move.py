from odoo import models, api, fields


class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals):
        order_id = vals.get('invoice_origin')

        print('------------------------CREATE DE ACCOUNT MOVE---------------------------------')
        print(order_id)

        if order_id:
            order = self.env['sale.order'].search([('name', '=', order_id)], limit=1)
            print('----------CANAL ID------------')
            diario = order.canal_id.diario_factura_id.id
            vals['journal_id'] = diario

            print('-------------VALOR JOURNAL .-------------')
            # print(vals['journal_id'] )
        return super(AccountMove, self).create(vals)