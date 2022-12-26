from datetime import timedelta
from odoo.http import request
from odoo import models, api, fields


class PosDashboard(models.Model):
    _inherit = 'project.project'


    @api.model
    def get_tiles_data(self, fetch_data):

        uid = request.session.uid
        today = fields.date.today()
        last_week = today - timedelta(days=7)
        last_month = today - timedelta(days=30)
        if fetch_data is None or fetch_data == 'week':
            if self.env.user.has_group('stock.group_stock_manager'):

                #    stock outgoing   #
                prdct_outgoing = self.env['product.product'].search([])
                out = []
                for rec in prdct_outgoing:
                    if rec.outgoing_qty != 0:
                        outgoing = f"{rec.name}: {rec.outgoing_qty}"
                        out.append(outgoing)
                formatted_out = "('" + ','.join(out) + ")"

                #    stock incoming   #
                prdct_incoming = self.env['product.product'].search([])
                incmg = []
                for data in prdct_incoming:
                    if data.incoming_qty != 0:
                        incoming = f"{data.name}: {data.incoming_qty}"
                        incmg.append(incoming)
                formatted_in = "('" + ','.join(incmg) + ")"

                #    internal transfer   #
                picking_type = self.env['stock.picking.type'].search(
                    [('code', '=', "internal"), ('name', '=', "Internal Transfers")])
                internal_t = []
                for j in picking_type:
                    internal = self.env['stock.picking'].search(
                        [('picking_type_id', '=', j.id), ('create_date', '>=', last_week), ('create_date', '<=', today)])
                    for k in internal:
                        intrnl_prdct = self.env['stock.move'].search(
                            [('picking_type_id', '=', j.id), ('picking_id', '=', k.id), ('state', '=', 'done')])
                        for l in intrnl_prdct:
                            internals = f"{l.product_id.name}: {l.product_qty}"
                            internal_t.append(internals)
                formatted_internal = "('" + ','.join(internal_t) + ")"

                #    location stock info   #
                location = self.env['stock.location'].search([('usage', '=', 'internal')])
                total = 0
                loc_stock = []
                for m in location:
                    loc_stock_info = self.env['stock.quant'].search([('location_id', '=', m.id)])
                    for i in loc_stock_info:
                        total = total + i.quantity
                    if total > 0:
                        stock_info_loc = f"{m.name}: {total}"
                        loc_stock.append(stock_info_loc)
                formatted_loc_stock = "('" + ','.join(loc_stock) + ")"

                #    Group based on picking type   #
                picking_types = self.env['stock.picking.type'].search([])
                pick_type = []
                for p_type in picking_types:
                    grp_picking = self.env['stock.picking'].search_count(
                        [('picking_type_id', '=', p_type.id), ('create_date', '>=', last_week),
                         ('create_date', '<=', today)])
                    if grp_picking > 0:
                        pick_types = f"{p_type.name}: {grp_picking}"
                        pick_type.append(pick_types)
                formatted_pick_type = "('" + ','.join(pick_type) + ")"

                #    product average cost   #
                product = self.env['product.template'].search([])
                avg_cost = []
                for rec in product:
                    if rec.standard_price != 0:
                        avg_cost.append((rec.name, rec.standard_price))
                return {
                    'out': formatted_out,
                    'incmg': formatted_in,
                    'pick_type': formatted_pick_type,
                    'internal': formatted_internal,
                    'loc_stock_info': formatted_loc_stock,
                    'avg_cost': avg_cost,
                }
            else:

                #    stock outgoing   #
                prdct_outgoing = self.env['product.product'].search([])
                out = []
                for rec in prdct_outgoing:
                    if rec.outgoing_qty != 0:
                        outgoing = f"{rec.name}: {rec.outgoing_qty}"
                        out.append(outgoing)
                formatted_out = "('" + ','.join(out) + ")"

                #    stock incoming   #
                prdct_incoming = self.env['product.product'].search([])
                incmg = []
                for data in prdct_incoming:
                    if data.incoming_qty != 0:
                        incoming = f"{data.name}: {data.incoming_qty}"
                        incmg.append(incoming)
                formatted_in = "('" + ','.join(incmg) + ")"

                #    internal transfer   #
                picking_type = self.env['stock.picking.type'].search(
                    [('code', '=', "internal"), ('name', '=', "Internal Transfers")])
                internal_t = []
                for j in picking_type:
                    internal = self.env['stock.picking'].search(
                        [('picking_type_id', '=', j.id), ('user_id', '=', request.session.uid),
                         ('create_date', '>=', last_week), ('create_date', '<=', today)])
                    for k in internal:
                        intrnl_prdct = self.env['stock.move'].search(
                            [('picking_type_id', '=', j.id), ('picking_id', '=', k.id), ('state', '=', 'done')])
                        for l in intrnl_prdct:
                            internals = f"{l.product_id.name}: {l.product_qty}"
                            internal_t.append(internals)
                formatted_internal = "('" + ','.join(internal_t) + ")"

                #    location stock info   #
                location = self.env['stock.location'].search([('usage', '=', 'internal')])
                total = 0
                loc_stock = []
                for m in location:
                    loc_stock_info = self.env['stock.quant'].search([('location_id', '=', m.id)])
                    for i in loc_stock_info:
                        total = total + i.quantity
                    if total > 0:
                        stock_info_loc = f"{m.name}: {total}"
                        loc_stock.append(stock_info_loc)
                formatted_loc_stock = "('" + ','.join(loc_stock) + ")"

                #    Group based on picking type   #
                picking_types = self.env['stock.picking.type'].search([])
                pick_type = []
                for p_type in picking_types:
                    grp_picking = self.env['stock.picking'].search_count(
                        [('picking_type_id', '=', p_type.id), ('user_id', '=', request.session.uid),
                         ('create_date', '>=', last_week), ('create_date', '<=', today)])
                    if grp_picking > 0:
                        pick_types = f"{p_type.name}: {grp_picking}"
                        pick_type.append(pick_types)
                formatted_pick_type = "('" + ','.join(pick_type) + ")"

                #    product average cost   #
                product = self.env['product.template'].search([])
                avg_cost = []
                avg_cost.clear()
                for rec in product:
                    if rec.standard_price != 0:
                        avg_cost.append((rec.name, rec.standard_price))
                return {
                    'out': formatted_out,
                    'incmg': formatted_in,
                    'pick_type': formatted_pick_type,
                    'internal': formatted_internal,
                    'loc_stock_info': formatted_loc_stock,
                    'avg_cost': avg_cost,
                }
        else:
            if self.env.user.has_group('stock.group_stock_manager'):

                #    stock outgoing   #
                prdct_outgoing = self.env['product.product'].search([])
                out = []
                for rec in prdct_outgoing:
                    if rec.outgoing_qty != 0:
                        outgoing = f"{rec.name}: {rec.outgoing_qty}"
                        out.append(outgoing)
                formatted_out = "('" + ','.join(out) + ")"

                #    stock incoming   #
                prdct_incoming = self.env['product.product'].search([])
                incmg = []
                for data in prdct_incoming:
                    if data.incoming_qty != 0:
                        incoming = f"{data.name}: {data.incoming_qty}"
                        incmg.append(incoming)
                formatted_in = "('" + ','.join(incmg) + ")"

                #    internal transfer   #
                picking_type = self.env['stock.picking.type'].search(
                    [('code', '=', "internal"), ('name', '=', "Internal Transfers")])
                internal_t = []
                for j in picking_type:
                    internal = self.env['stock.picking'].search(
                        [('picking_type_id', '=', j.id), ('create_date', '>=', last_month), ('create_date', '<=', today)])
                    for k in internal:
                        intrnl_prdct = self.env['stock.move'].search(
                            [('picking_type_id', '=', j.id), ('picking_id', '=', k.id), ('state', '=', 'done')])
                        for l in intrnl_prdct:
                            internals = f"{l.product_id.name}: {l.product_qty}"
                            internal_t.append(internals)
                formatted_internal = "('" + ','.join(internal_t) + ")"

                #    location stock info   #
                location = self.env['stock.location'].search([('usage', '=', 'internal')])
                total = 0
                loc_stock = []
                for m in location:
                    loc_stock_info = self.env['stock.quant'].search([('location_id', '=', m.id)])
                    for i in loc_stock_info:
                        total = total + i.quantity
                    if total > 0:
                        stock_info_loc = f"{m.name}: {total}"
                        loc_stock.append(stock_info_loc)
                formatted_loc_stock = "('" + ','.join(loc_stock) + ")"

                #    Group based on picking type   #
                picking_types = self.env['stock.picking.type'].search([])
                pick_type = []
                for p_type in picking_types:
                    grp_picking = self.env['stock.picking'].search_count(
                        [('picking_type_id', '=', p_type.id), ('create_date', '>=', last_month),
                         ('create_date', '<=', today)])
                    if grp_picking > 0:
                        pick_types = f"{p_type.name}: {grp_picking}"
                        pick_type.append(pick_types)
                formatted_pick_type = "('" + ','.join(pick_type) + ")"

                #    product average cost   #
                product = self.env['product.template'].search([])
                avg_cost = []
                for rec in product:
                    if rec.standard_price != 0:
                        avg_cost.append((rec.name, rec.standard_price))
                data = {
                    'out': formatted_out,
                    'incmg': formatted_in,
                    'pick_type': formatted_pick_type,
                    'internal': formatted_internal,
                    'loc_stock_info': formatted_loc_stock,
                    'avg_cost': avg_cost,
                }
            else:

                #    stock outgoing   #
                prdct_outgoing = self.env['product.product'].search([])
                out = []
                for rec in prdct_outgoing:
                    if rec.outgoing_qty != 0:
                        outgoing = f"{rec.name}: {rec.outgoing_qty}"
                        out.append(outgoing)
                formatted_out = "('" + ','.join(out) + ")"

                #    stock incoming   #
                prdct_incoming = self.env['product.product'].search([])
                incmg = []
                for data in prdct_incoming:
                    if data.incoming_qty != 0:
                        incoming = f"{data.name}: {data.incoming_qty}"
                        incmg.append(incoming)
                formatted_in = "('" + ','.join(incmg) + ")"

                #    internal transfer   #
                picking_type = self.env['stock.picking.type'].search(
                    [('code', '=', "internal"), ('name', '=', "Internal Transfers")])
                internal_t = []
                for j in picking_type:
                    internal = self.env['stock.picking'].search(
                        [('picking_type_id', '=', j.id), ('user_id', '=', request.session.uid),
                         ('create_date', '>=', last_month), ('create_date', '<=', today)])
                    for k in internal:
                        intrnl_prdct = self.env['stock.move'].search(
                            [('picking_type_id', '=', j.id), ('picking_id', '=', k.id), ('state', '=', 'done')])
                        for l in intrnl_prdct:
                            internals = f"{l.product_id.name}: {l.product_qty}"
                            internal_t.append(internals)
                formatted_internal = "('" + ','.join(internal_t) + ")"

                #    location stock info   #
                location = self.env['stock.location'].search([('usage', '=', 'internal')])
                total = 0
                loc_stock = []
                for m in location:
                    loc_stock_info = self.env['stock.quant'].search([('location_id', '=', m.id)])
                    for i in loc_stock_info:
                        total = total + i.quantity
                    if total > 0:
                        stock_info_loc = f"{m.name}: {total}"
                        loc_stock.append(stock_info_loc)
                formatted_loc_stock = "('" + ','.join(loc_stock) + ")"

                #    Group based on picking type   #
                picking_types = self.env['stock.picking.type'].search([])
                pick_type = []
                for p_type in picking_types:
                    grp_picking = self.env['stock.picking'].search_count(
                        [('picking_type_id', '=', p_type.id), ('user_id', '=', request.session.uid),
                         ('create_date', '>=', last_month), ('create_date', '<=', today)])
                    if grp_picking > 0:
                        pick_types = f"{p_type.name}: {grp_picking}"
                        pick_type.append(pick_types)
                formatted_pick_type = "('" + ','.join(pick_type) + ")"

                #    product average cost   #
                product = self.env['product.template'].search([])
                avg_cost = []
                avg_cost.clear()
                for rec in product:
                    if rec.standard_price != 0:
                        avg_cost.append((rec.name, rec.standard_price))
                data = {
                    'out': formatted_out,
                    'incmg': formatted_in,
                    'pick_type': formatted_pick_type,
                    'internal': formatted_internal,
                    'loc_stock_info': formatted_loc_stock,
                    'avg_cost': avg_cost,
                }
        return data
