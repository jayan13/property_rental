# Copyright (c) 2022, alantechnologies and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import nowdate
from frappe.model.document import Document
from erpnext.projects.doctype.project.project import Project

class PropertyMaintenance(Document):

	def on_trash(self):
		pjt=frappe.get_doc("Project", self.project)
		pjt.delete()

	def after_insert(self):
		project = frappe.new_doc("Project")
		project.project_name=self.name+'-'+self.maintenance_title
		project.project_type="Property Maintenance"
		project.expected_start_date=self.start_date
		project.expected_end_date=self.end_date
		project.company=self.company
		project.estimated_costing=self.estimated_costing
		project.cost_center=self.cost_center
		project.notes=self.note
		project.insert(ignore_permissions=True)
		self.project=project.name		
		self.save()

	def on_update(self):
		pjt=frappe.get_doc("Project", self.project)
		if pjt.status!=self.status:
			pjt.status=	self.status
			if self.status=='Completed':
				pjt.expected_end_date=nowdate()
			else:
				pjt.expected_end_date=self.end_date
		else:
			pjt.expected_end_date=self.end_date
			
		pjt.expected_start_date=self.start_date
		pjt.expected_end_date=self.end_date
		pjt.company=self.company
		pjt.estimated_costing=self.estimated_costing
		pjt.cost_center=self.cost_center
		pjt.notes=self.note
		pjt.save()