# -*- coding:utf-8 -*-
#
#
#    Copyright (C) 2020 'Gerchev Technologies PLC'.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
     # Module Information
    'name': 'Vehicle Fuel Log Group by Date',
    'category': 'Managing vehicles and contracts',
    'sequence': 1,
    'version': '13.0.0.2',
    'license': 'LGPL-3',
    'summary': """Allow grouping fuel log entries by date
    """,
    'description':"""
	Group Fuel Log Entries by Date
	==============================
    """,
    # Website
    'author': 'Gerchev Technologies PLC',
    'website': 'http://gerchev.com',
    # Dependencies
    'depends': [
        'fleet',
    ],
    # Data 
    'data': [
        'views/fleet_view.xml',
    ],

    # Technical
    'demo': [ ],
    'installable': True,
    'active': False,
    'application': True,

}
