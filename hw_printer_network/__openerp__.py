{
    "name": """Hardware Network Printer""",
    "summary": """Hardware Driver for Network Printers""",
    "category": "Point of Sale",
    "images": [],
    "version": "12.0.2.0.1",
    "application": False,

    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "apps@it-projects.info",
    "website": "https://apps.odoo.com/apps/modules/12.0/hw_printer_network/",
    "license": "LGPL-3",
    "price": 59.00,
    "currency": "EUR",

    "depends": [
        "hw_escpos",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
    ],
    "qweb": [
    ],
    "demo": [],

    "post_load": "post_load",
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
