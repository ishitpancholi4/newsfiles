from odoo import models, fields


class SalesOrder(models.Model):
    _inherit = 'sale.order'
    zipcode = fields.Integer(string="Zipcode")
