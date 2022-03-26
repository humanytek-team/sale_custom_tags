{
    "name": "Sale Custom Tags",
    "version": "13.0.0.1.0",
    "author": "HomebrewSoft",
    "website": "https://homebrewsoft.dev",
    "license": "LGPL-3",
    "depends": [
        "sale",
        "crm",
        "sale_crm",
        "account",
    ],
    "data": [
        # security
        "security/group.xml",
        "security/ir.model.access.csv",
        # data
        # reports
        # views
        "views/account_move.xml",
        "views/sale_order.xml",
    ],
}
