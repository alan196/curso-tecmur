# Copyright 2020, Tecmur
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields


class ClassName(models.Model):
    _name = 'openacademy.material'
    _description = 'OpenAcademy Materials'

    name = fields.Char(size=12, required=False)
    course_id = fields.Many2one(
        'openacademy.course', ondelete='cascade', required=True)
