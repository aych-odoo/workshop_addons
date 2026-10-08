from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(required=True)

    _unique_name = models.Constraint('UNIQUE(name)', 'Property type names must be unique.')
