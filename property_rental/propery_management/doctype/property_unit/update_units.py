import frappe

def update_unit(doc,event):
    if doc.property_unit:
        udoc = frappe.get_doc('Property Unit', doc.property_unit)
        #print(f"{udoc.unit_no}")
        udoc.contract_start_date = doc.contract_start_date
        udoc.contract_end_date = doc.contract_end_date
        udoc.annual_rent = doc.annual_rent
        udoc.customer_name = doc.customer_name
        udoc.security_deposit = doc.security_deposit
        udoc.unit_status = doc.unit_status
        udoc.save()
        #frappe.throw("Error")

    

