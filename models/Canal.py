from odoo import models, fields, api

class CalanVenta(models.Model):
    _name = 'dan.canal'

    name = fields.Char(string="Nombre", required =True)
    codigo = fields.Char(string="Codigo", readonly=True)
    deposito_id = fields.Many2one('stock.warehouse', string='Deposito')
    diario_factura_id = fields.Many2one('account.journal', string='Diario de Factura')


    @api.model
    def create(self, vals):

        vals['codigo'] = self.env['ir.sequence'].next_by_code('code_canal') or '/'

        return super(CalanVenta, self).create(vals)

