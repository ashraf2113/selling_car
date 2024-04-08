from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Properties(models.Model):
    _name = "properties"
    
    phone = fields.Char("phone")
    date_availability = fields.Date(required=1)

    address = fields.Char(required=1 ,default="street",size=15)
    name = fields.Char(required=True)
    degree = fields.Integer("degree")
    education = fields.Char(required=1 ,default="street",size=15)
    description = fields.Text(required=1 ,default="street",size=15)
    having_car = fields.Boolean("having car")
    having_license = fields.Boolean("having license")
    expected_price =fields.Float(digits=(0,5))
    garden_orientation = fields.Selection([
        ('east', 'East'),
        ('west', 'West'),
        ('north', 'North'),
        ('south', 'South'),
    ], string="Garden Orientation",default='east')
    _sql_constraints = [
        ('unique_name','unique("name")','This name is exist!')
    ]

    @api.constrains("phone")
    def _check_phone_greater_zero(self):
        for rec in self:
            if rec.phone == 0:
                raise ValidationError("Please enter a valid number")
    
    # @api.model_create_multi(self,vals)
    # def create(self,vals):
    #     res=super(Properties,vals).create(vals)
    #     print("inside creat method")
    #     return res
    
    # @api.model
    # def _search(self, domain,offset=0, limit=None, order=None, access_rights_uid=None):
    #     res=super(Properties,vals)._search(domain,offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("inside search method")
    #     return res
    
    # def write(self,vals):
    #     res=super(Properties,vals).write(vals)
    #     print("inside write method")
    #     return res
    
    # def unlink(self,vals):
    #     res=super(Properties,vals).unlink()
    #     print("inside unlink method")
    #     return res


    