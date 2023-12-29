from odoo import fields,api,models


class Creditos(models.Model):
    _name='ng.credito'

    name = fields.Char(string="Nombre")
    codigo = fields.Integer(string="Codigo del grupo")
    canal_id = fields.Many2one('dan.canal',  string="Canal")

    credito_global  = fields.Monetary('Credito global', currency_field="company_currency")

    company_currency = fields.Many2one("res.currency", string='Currency', compute="_compute_company_currency", readonly=True)

    def _compute_company_currency(self):
        return self.env.user.company_id.currency_id.id