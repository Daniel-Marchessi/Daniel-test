from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    canal_id = fields.Many2one('dan.canal',  string="Canal")

    @api.onchange('canal_id')
    def _onchange_canal_venta(self):
        print('-----------------------------------------------------')
        if self.canal_id:
            self.warehouse_id = self.canal_id.deposito_id
            print('-----------------------------------------------------')
            print(self.warehouse_id)
