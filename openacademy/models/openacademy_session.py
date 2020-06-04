# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one(
        'res.partner', domain=[
            '|',
            ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher")]
    )
    course_id = fields.Many2one(
        'openacademy.course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(compute='_compute_taken_seats')
    active = fields.Boolean(default=True)
    end_date = fields.Date(
        compute='_compute_end_date', inverse='_inverse_end_date', store=True)

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for rec in self:
            if not rec.seats:
                rec.taken_seats = 0.0
            else:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats

    @api.onchange('seats', 'attendee_ids')
    def _onchange_verify_valid_seats(self):
        if self.seats < 0:
            self.seats = 0
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': (
                        "The number of available seats may not be negative"),
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for rec in self:
            if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
                raise ValidationError(
                    "A session's instructor can't be an attendee")

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.duration):
                rec.end_date = rec.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=rec.duration, seconds=-1)
            rec.end_date = rec.start_date + duration

    def _inverse_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.end_date):
                continue

            # Compute the difference between dates, but:
            # Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            rec.duration = (rec.end_date - rec.start_date).days + 1
