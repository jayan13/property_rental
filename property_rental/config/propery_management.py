from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Property Management"),
			"items": [
				{
				   "type": "doctype", 
				   "description": "Property", 
				   "name": "Property", 
				  },

				{
				   "type": "doctype", 
				   "description": "Property Unit", 
				   "name": "Property Unit", 
				  },
				{
				   "type": "doctype", 
				   "description": "Property Type", 
				   "name": "Property Type", 
				  },
				
            ]

        }
	]
