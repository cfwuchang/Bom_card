# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    'name': "Bom_card",
    'author': "Bom_card",
    'category': 'purchase',
    'summary': """Bom_card""",
    'website': 'http://www.asceticbs.com',
    'license': 'AGPL-3',
    'description': """Bom_card""",
    'version': '14.0.1.0',
    'depends': ['base', 'mail'],
    "data": [
        "security/ir.model.access.csv",
        "views/digest_views.xml",
        "report/digest_details_template.xml",
        "report/report.xml",
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
