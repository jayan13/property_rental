import frappe

def update_unit(doc,event):
    if doc.property_unit:
        udoc = frappe.get_doc('Property Unit', doc.property_unit)
        #print(f"{udoc.unit_no}")
        udoc.contract_start_date = doc.contract_start_date
        udoc.contract_end_date = doc.contract_end_date
        udoc.customer_name = doc.customer_name        
        udoc.unit_status = 'Occupied'
        udoc.contract_issue_date=doc.posting_date,
        udoc.save()        
        #frappe.throw("Error")

def update_unit_status():
    units=frappe.db.sql("""select name from  `tabProperty Unit`   where contract_end_date < CURDATE() and contract_end_date <> '' and (unit_status ='Occupied' or unit_status ='Occupied - Legal') """)
    for unt in units:
        frappe.db.sql("""update `tabProperty Unit` set unit_status ='Vacant'  where name=%s """,unt[0])
        
    frappe.db.commit()
