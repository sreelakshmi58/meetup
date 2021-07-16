from odoo import api, fields, models

class MeetupRegistration(models.Model):
    _name = "meetup.registration"
    description = "meeting details"

    name = fields.Char(string="Meetup Name")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    contact_ids = fields.Many2many('res.partner', string="Contacts")

