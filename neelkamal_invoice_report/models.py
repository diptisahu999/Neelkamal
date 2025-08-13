from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'
    

    x_pan_no = fields.Char(string="PAN No")
    x_msme_no = fields.Char(string="MSME No")
    # custom_qr_code = fields.Image(string="QR Code")

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_challan_no = fields.Char(string="Challan No")
    x_challan_date = fields.Date(string="Challan Date")
    x_eway_bill_no = fields.Char(string="Eway Bill No")
    x_vehicle_no = fields.Char(string="Vehicle No")
    x_transport_name = fields.Char(string="Transport Name")
    x_lr_no = fields.Char(string="L.R. No")
    x_irn_no = fields.Char(string="IRN")
    x_ack_no = fields.Char(string="Ack No")
    x_ack_date = fields.Datetime(string="Ack Date")
    # x_qr_code = fields.Char(string="QR Code")  # Added QR code field
    x_report_footer_info = fields.Text(string="Report Footer Info")

    amount_total_in_words = fields.Char(string="Total Amount in Words", compute='_compute_amount_total_in_words', store=True)
    x_meters = fields.Float(string="Meters")
    x_custom_logo = fields.Binary(string="Custom Logo")
    x_terms_conditions = fields.Text(string="Terms & Conditions")

    # Bank and PO details
    # x_po_no = fields.Char(string="PO No.")
    x_bank_details = fields.Char(string="Bank Details")
    x_account_no = fields.Char(string="Account No")
    x_ifsc_code = fields.Char(string="IFSC Code")

    # Financial details
    x_taxable_value = fields.Float(string="Taxable Value")
    x_igst_rate = fields.Float(string="IGST Rate")
    x_igst_amount = fields.Monetary(string="IGST Amount", currency_field="currency_id")

    @api.depends('amount_total', 'x_igst_rate')
    def _compute_x_igst_amount(self):
        for rec in self:
            rec.x_igst_amount = (rec.amount_total * rec.x_igst_rate) / 100 if rec.x_igst_rate else 0.0

    received_by = fields.Char(string="Received By")
    prepared_by = fields.Char(string="Prepared By")
    authorized_signatory = fields.Char(string="Authorized Signatory")

    # Pehle ke fields (Transport wale)
    x_transport_name = fields.Char(string="Transport")
    x_vehicle_no = fields.Char(string="Vehicle No.")
    x_lr_no = fields.Char(string="L.R. No.")
    x_eway_bill_no = fields.Char(string="Eway Bill No.")

    x_terms_and_conditions = fields.Html(
        string="Terms and Conditions",
        default="""
    <strong>TERMS &amp; CONDITIONS :</strong><br/>
    (1) PAYMENT TO BE MADE BY PAYEES A/C CHEQUE, DRAFT TO NEFT/RTGS/IMPS ONLY.<br/>
    (2) KINDLY CHECK THE FABRIC FOR AZO FREE, QUALITY DEFECTS, COLOUR FASTNESS, COLOUR VARIATION BEFORE USING THE FABRICS, WE ARE NOT RESPONSIBLE FOR ANY CLAIMS.<br/>
    (3) WE ARE NOT RESPONSIBLE FOR ANY LOSS OR DAMAGES DURING TRANSIT. THE GOODS ARE DESPATCHED AT BUYER'S RISK.<br/>
    (4) ANY COMPLAIN EITHER OF GOODS OR INVOICE MUST BE CLEARED WITHIN TWO DAYS.<br/>
    (5) THE SALE IS UNDERSTOOD TO HAVE BEEN MADE AFTER DUE CONSIDERATION OF THE QUALITY OF GOODS AND PREVAILING RATES.<br/>
    (6) INTEREST @2.5% P.M. WILL BE CHARGED AFTER DUE DATE OF BILL.<br/>
    (7) SUBJECT TO SURAT JURISDICTION.
    """
    )

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_total_in_words(self):
        for record in self:
            if record.currency_id:
                record.amount_total_in_words = record.currency_id.amount_to_text(record.amount_total)
            else:
                record.amount_total_in_words = ''

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Add this field, copied from your account.move model
    x_terms_and_conditions = fields.Html(
        string="Terms and Conditions",
        default="""
    <strong>TERMS &amp; CONDITIONS :</strong><br/>
    (1) PAYMENT TO BE MADE BY PAYEES A/C CHEQUE, DRAFT TO NEFT/RTGS/IMPS ONLY.<br/>
    (2) KINDLY CHECK THE FABRIC FOR AZO FREE, QUALITY DEFECTS, COLOUR FASTNESS, COLOUR VARIATION BEFORE USING THE FABRICS, WE ARE NOT RESPONSIBLE FOR ANY CLAIMS.<br/>
    (3) WE ARE NOT RESPONSIBLE FOR ANY LOSS OR DAMAGES DURING TRANSIT. THE GOODS ARE DESPATCHED AT BUYER'S RISK.<br/>
    (4) ANY COMPLAIN EITHER OF GOODS OR INVOICE MUST BE CLEARED WITHIN TWO DAYS.<br/>
    (5) THE SALE IS UNDERSTOOD TO HAVE BEEN MADE AFTER DUE CONSIDERATION OF THE QUALITY OF GOODS AND PREVAILING RATES.<br/>
    (6) INTEREST @2.5% P.M. WILL BE CHARGED AFTER DUE DATE OF BILL.<br/>
    (7) SUBJECT TO SURAT JURISDICTION.
    """
    )

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_mtr = fields.Float(string="MTR")

