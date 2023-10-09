from odoo import models, fields

class ManageStaff(models.Model):
    _name= "manage.staff"
    _description= "This is management of office"


    name = fields.Char(string="Name", size=50)
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")





