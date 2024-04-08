from odoo import models, fields, api

class Owner(models.Model):
    _name = "owner"

    name = fields.Char(required=True)
    phone = fields.Char("phone")
    date_availability = fields.Date(required=1)

    address = fields.Char(required=1 ,default="street",size=15)
    having_car = fields.Boolean("having car")
    having_license = fields.Boolean("having license")

    products_ids=fields.One2many("products","owner_id")

    _sql_constraints = [
        ('unique_name','unique("name")','This name is exist!')
    ]




    