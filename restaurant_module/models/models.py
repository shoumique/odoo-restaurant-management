


from odoo import models, fields
# from typing_extensions import Required


class RestaurantMenu(models.Model):
    _name = 'restaurant.menu'
    _description = 'restaurant menu'
 
    item = fields.Selection([
        ('breakfast','Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks')
    ], required=True)
    value = fields.Integer(string='Quantity', store=True)
    food = fields.Selection([
        ('burger','Burger'),
        ('pasta', 'Pasta'),
        ('pizza', 'Pizza')
    ], required=True)
    description = fields.Text(string='Note')
    image= fields.Binary(string='Image')
    addon_list_ids = fields.Many2many('restaurant.addon', 'menu_addon_relation', 'restaurant_menu_id', 'addon_id', string='Addons List')
    def action_url(self):
        return {
            'type':'ir.actions.act_url',
            'target': 'self',
            'url': 'http://localhost:8015/web#action=386&model=pos.config&view_type=kanban&cids=1&menu_id=231' ,
        }
    def update_invoice_print(self):
        for record in self:
            if record.food == 'new':
                record.food = 'menu_accepted'
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
class Employee(models.Model):

    _inherit = "hr.employee"

    name=fields.Char(string='Employee')


class Addons(models.Model):
    _name = 'restaurant.addon'
    
    name=fields.Char(string='Addon Name')

class kitchen(models.Model):
    _name='restaurant.kitchen'

    chef=fields.Many2many('restaurant.menu','food_menu',string='Order')    
