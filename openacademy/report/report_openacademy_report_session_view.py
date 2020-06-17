# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models


class OpenacademySessionReport(models.AbstractModel):
    _name = 'report.openacademy.report_session_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name(
            'openacademy.report_session_view')
        prueba = ['hola', 'adios']
        docs = self.env['openacademy.session'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'prueba': prueba,
            'metodo': self.test_method,
        }

    @api.model
    def test_method(self, value):
        return 'The value is %s' % value
