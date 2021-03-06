# Copyright YEAR(S), AUTHOR(S)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(
        "Instructor", default=False)

    session_ids = fields.Many2many(
        'openacademy.session',
        string='Attended Sessions', readonly=True)
