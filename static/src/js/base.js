odoo.define('odoo_all_debrand.base', function(require) {
    var WebClient = require('web.WebClient');
    var core = require('web.core');

    var _t = core._t;

    WebClient.include({
        init: function(parent) {
            this._super.apply(this, arguments);
            var self = this;
            this.set('title_part', {"zopenerp": ''});
            odoo.debranding_new_name = '';
            odoo.debranding_new_website = '';
            odoo.debranding_new_title = '';

            self._rpc({
                model: "ir.config_parameter",
                method: 'get_debranding_parameters',
            }, {
                shadow: true
            }).then(function(result){
                odoo.debranding_new_name = result['odoo_all_debrand.new_name'];
                odoo.debranding_new_website = result['odoo_all_debrand.new_website'];
                odoo.debranding_new_title = result['odoo_all_debrand.new_title'];
                self.set('title_part', {"zopenerp": odoo.debranding_new_title});

            });
        }
    });

});
