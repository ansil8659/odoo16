from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteProduct(WebsiteSale):
    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=True)
    def product(self, product, category='', search='', **kwargs):
        res = super(WebsiteProduct, self).product(product, category='', search='', **kwargs)
        warehouse = request.env['stock.warehouse'].search([])
        print("llllllllllllllllll")
        for rec in warehouse:
            print(rec.name, "qwertyuiop")
        stock = request.env['stock.quant'].search([('location_id.usage', '=', 'internal')])
        values = {}
        print("uytresxcvbnm,.")
        values.update({
            'stock': stock
        })
        print(values)
        # return request.render("website_product_check.website_sale_product_check", values)
        # lists = []
        # for i in stock:
        #     # print(i.product_id.name, "1234567890")
        #     # print(i.location_id.name, "9999999999")
        #     print(i.warehouse_id.name, "9999999999")
        #     print(i.product_id.name, "9999999999")
        #     lists.append(i.product_id)
        # print(lists)
        # location = request.env['stock.location'].search([('usage', '=', 'internal')])
        # for data in location:
        #     print(data.warehouse_id.name, "999999")
        # print(product)
        # product = request.env['product.product'].
        return res

