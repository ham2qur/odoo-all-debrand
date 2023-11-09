from . import models
from . import controllers

from odoo import SUPERUSER_ID, api

MODULE = '_odoo_all_debrand'


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.model.data']._module_data_uninstall([MODULE])


def post_load():

    from . import fields
