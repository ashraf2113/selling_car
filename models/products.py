from odoo import models, fields, api

class Products(models.Model):
    _name = "products"
    
    name=fields.Char("name")
  
    selling_price =fields.Float(digits=(0,5))
    postcode =fields.Float(digits=(0,5))
    expected_price =fields.Float(digits=(0,5))
    selling_date=fields.Date("selling_date")

    owner_id=fields.Many2one('owner')
    tag_ids=fields.Many2many('tag')

    state=fields.Selection([
        ("draft","Draft"),
        ("pending","Pending"),
        ("sold","Sold"),

    ], default="draft")

    _sql_constraints = [
        ('unique_name','unique("name")','This name is exist!')
    ]

    