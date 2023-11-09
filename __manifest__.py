{
    'name': "Backend debranding",
    'version': '13.0.1.0.28',
    'author': 'NinasSofts',
    'license': 'LGPL-3',
    'category': 'Debranding',
    'images': ['images/web_debranding.png'],
    'website': 'https://www.dzitechnology.com',
    'price': 149.00,
    'currency': 'EUR',
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
            "/web_debranding/static/src/css/web.css",
            "/web_debranding/static/src/js/base.js",
            "/web_debranding/static/src/js/dialog.js",
            "/web_debranding/static/src/js/dashboard.js",
            "/web_debranding/static/src/js/field_upgrade.js",
            "/web_debranding/static/src/js/native_notifications.js",
            "/web_debranding/static/src/js/bot.js",
            "/web_debranding/static/src/js/user_menu.js",
        ],
    }
}
