# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner_meal(models.Model):
    _name = "partner.meal"
    _description = "meal group for partners"

    meal_name = fields.Selection([
        ('breakfast', 'وجبة الفطار'),
        ('lunch', 'وجبة الغداء'),
        ('dinner', 'وجبة العشاء')],
        string='اسم الوجبة'
    )
    partner_id = fields.Many2one('res.partner', string='اسم العميل')
    meal_datetime = fields.Datetime('وقت الوجبة')
    meal_note = fields.Text('ملاحظات')
    item_ids = fields.One2many('partner.meals.items', 'meal_id')
    total_price = fields.Float(string='Total Meal price', compute='_total_price', readonly=True, store=True)

    @api.depends('item_ids.meal_item_price')
    def _total_price(self):
        finalprice = 0
        for record in self:
            for field in record.item_ids:
                finalprice += field.meal_item_price
            record.total_price = finalprice


class partners_meals_items(models.Model):
    _name = "partner.meals.items"
    _description = "partner meals items"

    product_id = fields.Many2one('product.template', 'عنصر الوجبة')
    meal_id = fields.Many2one('partner.meal')
    meals_numbers = fields.Integer('عدد عناصر الوجبة')
    product_price = fields.Float(related='product_id.list_price', string='سعر عنصر الوجبة', readonly=False, store=False)
    calories = fields.Integer(related='product_id.calories', string='عدد السعرات الحرارية')
    weight = fields.Integer(related='product_id.product_weight', string='وزن الوجبة')
    meal_item_price = fields.Float(compute="_calcprice", string="سعر عناصر الوجبة", store=True)

    @api.depends('product_price', 'meals_numbers')
    def _calcprice(self):
        for record in self:
            record.meal_item_price = record.product_price * record.meals_numbers


class test_field_module(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    _description = "test Module"

    product_weight = fields.Integer('وزن الوجبة')
    calories = fields.Integer('عدد السعرات الحرارية')
    expiry_date = fields.Date('تاريخ انتهاء الصلاحية')



# class my_meal(models.Model):
#     _name = 'my_meal.my_meal'
#     _description = 'my_meal.my_meal'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
