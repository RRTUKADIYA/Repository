from odoo import fields , models, api



class CustomerSaleRelEpt(models.Model):
    
    _name = "customer.sale.rel.ept"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    
    @api.depends('sale_order')
    def _set_on_onchange(self):
        
        if not self.sale_order:
            return

        for order in self:
            self.name = self.sale_order.name
            self.customer = self.sale_order.partner_id
            self.warehouse = self.sale_order.warehouse_id
            self.name = self.sale_order.name
            
            
            if self.sale_order.invoice_ids.id == False:
                print "No invoice"
                self.invoice_paid_amount = 0.0
                self.invoice_remaining_amount=self.sale_order.amount_total
            else:
                print "Invoice Created"
                for inv in self.sale_order.invoice_ids:
                    self.invoice_paid_amount = inv.amount_total - inv.residual
                    self.invoice_remaining_amount=inv.residual

        order.update({
                'customer': self.customer,
                'warehouse':self.warehouse,
                'invoice_paid_amount':self.invoice_paid_amount,
                'invoice_remaining_amount':self.invoice_remaining_amount
               
            })

       
    
    name = fields.Char("Sale_order")
    date = fields.Date(string='Date', required=True , default=fields.Date.context_today)
    sale_order = fields.Many2one('sale.order', string="Sales Order" ,domain=[('state', 'in', ['sale','done','cancle'])])
    customer = fields.Many2one('res.partner', string='Customer', store=True, readonly=True, compute='_set_on_onchange', track_visibility='always')
    warehouse = fields.Many2one('stock.warehouse', string="Warehouse", store=True, readonly=True, compute='_set_on_onchange', track_visibility='always')
    invoice_paid_amount = fields.Float(String="Paid Amount", store=True, readonly=True, compute='_set_on_onchange', track_visibility='always')
    invoice_remaining_amount = fields.Float(String="Paid Reemaining",  store=True, readonly=True, compute='_set_on_onchange', track_visibility='always') 
    products = fields.Many2many('sale.order.line', string='Order Lines')
    '''
    @api.multi
    @api.onchange('sale_order')
    def sale_onder_on_change(self):
        if not self.sale_order:
            return
        
        self.customer = self.sale_order.partner_id
        self.warehouse = self.sale_order.warehouse_id
        self.name = self.sale_order.name
       
        if self.sale_order.invoice_ids.id == False:
            print "No invoice"
            self.invoice_paid_amount = 0.0
            self.invoice_remaining_amount=self.sale_order.amount_total
        else:
            print "Invoice Created"
            for inv in self.sale_order.invoice_ids:
                self.invoice_paid_amount = inv.amount_total - inv.residual
                self.invoice_remaining_amount=inv.residual
    '''
    def getProducts(self):
        if not self.sale_order:
            return
        
        self.products = self.sale_order.order_line
        self.name = self.sale_order.name

