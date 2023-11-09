{
    'name': "Odoo All Debranding",
    'version': '15.0',
    'author': 'Hammad Hussain Qureshi',
    'license': 'LGPL-3',
    'category': 'Debranding',
    'images': ['images/odoo_all_debrand.png'],
    'website': '',
    'depends': [
        'web',
        'im_livechat',
        'mail',
    ],
    'data': [
        'data.xml',
        # 'views.xml',
        'pre_install.xml',
    ],
    'qweb': [
        'static/src/xml/web.xml',
    ],
    "post_load": 'post_load',
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'assets': {
        'web.assets_backend': [
            "/odoo_all_debrand/static/src/css/web.css",
            "/odoo_all_debrand/static/src/js/base.js",
            "/odoo_all_debrand/static/src/js/dialog.js",
            "/odoo_all_debrand/static/src/js/dashboard.js",
            "/odoo_all_debrand/static/src/js/field_upgrade.js",
            "/odoo_all_debrand/static/src/js/native_notifications.js",
            "/odoo_all_debrand/static/src/js/bot.js",
            "/odoo_all_debrand/static/src/js/user_menu.js",
        ],
    }
}
