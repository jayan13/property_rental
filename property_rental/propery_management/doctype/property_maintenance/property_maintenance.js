// Copyright (c) 2022, alantechnologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property Maintenance', {
	 refresh: function(frm) {
		
	if (frm.doc.project)
	{
		frappe.db.get_doc('Project', frm.doc.project).then(doc => {
		frm.set_value('actual_costing', doc.total_purchase_cost) })
	}

		frm.set_query("propperty_unit", function() {
			return {
				filters: {"property_name": frm.doc.property}
				
			}
		});

		frm.set_query("cost_center", function() {
			return {
				filters: {"company": frm.doc.company}
				
			}
		});

	 }
});
