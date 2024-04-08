from odoo import models, fields, api

class Tag(models.Model):
    _name = "tag"

    name = fields.Char(required=True)


    _sql_constraints = [
        ('unique_name','unique("name")','This name is exist!')
    ]




    