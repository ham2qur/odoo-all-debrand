from odoo import models, api
from odoo.tools.translate import _

PARAMS = [
    ('odoo_all_debrand.new_name', _('Software')),
    ('odoo_all_debrand.new_title', _('Software')),
    ('odoo_all_debrand.new_website', 'example.com'),
    ('odoo_all_debrand.new_documentation_website', ''),
    ('odoo_all_debrand.favicon_url', ''),
    ('odoo_all_debrand.send_publisher_warranty_url', '0'),
    ('odoo_all_debrand.icon_url', ''),
    ('odoo_all_debrand.apple_touch_icon_url', ''),

]


def get_debranding_parameters_env(env):
    res = {}
    for param, default in PARAMS:
        value = env['ir.config_parameter'].sudo().get_param(param, default)
        res[param] = value.strip()
    return res


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_debranding_parameters(self):
        return get_debranding_parameters_env(self.env)

    @api.model
    def create_debranding_parameters(self):
        for param, default in PARAMS:
            if not self.env['ir.config_parameter'].sudo().get_param(param):
                self.env['ir.config_parameter'].sudo().set_param(param, default or ' ')
