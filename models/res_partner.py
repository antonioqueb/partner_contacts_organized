# -*- coding: utf-8 -*-
from odoo import models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_contact_create_action(self, contact_type, form_title):
        """Retorna la acción para abrir el formulario de creación del tipo indicado."""
        self.ensure_one()
        ctx = {
            'default_parent_id': self.id,
            'default_type': contact_type,
            'default_lang': self.lang,
            'default_user_id': self.user_id.id,
        }
        if contact_type == 'contact':
            ctx.update({
                'default_street': self.street,
                'default_street2': self.street2,
                'default_city': self.city,
                'default_state_id': self.state_id.id,
                'default_zip': self.zip,
                'default_country_id': self.country_id.id,
            })
        return {
            'type': 'ir.actions.act_window',
            'name': form_title,
            'res_model': 'res.partner',
            'view_mode': 'form',
            'target': 'new',
            'context': ctx,
        }

    def action_create_contact(self):
        return self._get_contact_create_action('contact', _('Nuevo Contacto'))

    def action_create_delivery_address(self):
        return self._get_contact_create_action('delivery', _('Nueva Dirección de Entrega'))

    def action_create_invoice_address(self):
        return self._get_contact_create_action('invoice', _('Nueva Dirección de Factura'))
