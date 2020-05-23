# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields


class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    name = fields.Char()
    description = fields.Text()
    responsible_id = fields.Many2one(
        'res.users', ondelete='set null', index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
