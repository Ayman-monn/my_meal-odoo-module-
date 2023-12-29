# -*- coding: utf-8 -*-
# from odoo import http


# class MyMeal(http.Controller):
#     @http.route('/my_meal/my_meal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_meal/my_meal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_meal.listing', {
#             'root': '/my_meal/my_meal',
#             'objects': http.request.env['my_meal.my_meal'].search([]),
#         })

#     @http.route('/my_meal/my_meal/objects/<model("my_meal.my_meal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_meal.object', {
#             'object': obj
#         })
