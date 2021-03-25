from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    iface_self_service = fields.Boolean(
        string="Is Self-Service", help="Use that POS as self-service point"
    )
    label_offset_x = fields.Integer(
        string="Label Offset X",
        required=True,
        default=320,
        help="Origin point of the contents in the label, X coordinate.",
    )
    label_offset_y = fields.Integer(
        string="Label Offset Y",
        required=True,
        default=40,
        help="Origin point of the contents in the label, Y coordinate.",
    )
    label_height = fields.Integer(
        string="Label Height",
        required=True,
        default=2,
        help="ZPL ^BY command argument",
    )
    label_width = fields.Integer(
        string="Label Width",
        required=True,
        default=100,
        help="ZPL ^BY command argument",
    )
    printer_name = fields.Char(
        string="Printer Name", help="Find in CUPS at localhost:631/printers"
    )
