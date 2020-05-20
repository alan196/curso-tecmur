# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields


class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    name = fields.Char()
    description = fields.Text()
