{
    "name": "Partner Contacts Organized",
    "version": "19.0.1.0.0",
    "category": "Contacts",
    "summary": "Organiza contactos, direcciones de entrega y factura en secciones claras",
    "description": """
        Reemplaza la pestaña de contactos del partner con una vista organizada
        que separa contactos, direcciones de entrega y direcciones de factura
        con botones explícitos para crear cada tipo.
    """,
    "author": "Alphaqueb Consulting",
    "website": "https://alphaqueb.com",
    "depends": ["base", "contacts"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "partner_contacts_organized/static/src/css/partner_contacts.css",
        ],
    },
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
