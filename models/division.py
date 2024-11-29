from odoo import fields, models


class Division(models.Model):
    _name = 'help.division'
    _description = 'Division'

    name = fields.Char(string='Helpdesk Division', required=True, help="Name of Division")