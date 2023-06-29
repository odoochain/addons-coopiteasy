# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Point of Sale Customer Wallet",
    "summary": """
        Enable usage of the Customer Wallet in the Point of Sale.""",
    "version": "12.0.2.1.0",
    "category": "Point of Sale",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC,GRAP",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "point_of_sale",
        "account_customer_wallet",
        "base_suspend_security",
    ],
    "excludes": [],
    "data": [
        "templates/assets.xml",
    ],
    "demo": [
        "demo/account_journal_demo.xml",
        "demo/product_product_demo.xml",
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],
}
