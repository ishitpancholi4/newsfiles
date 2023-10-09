from odoo import models , fields


class OfficeStaff(models.Model):
    _name= "office.staff"
    _description = "This is management of office"



    name = fields.Char(string="Name", size=50)
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email",default='example@gmail.com')









