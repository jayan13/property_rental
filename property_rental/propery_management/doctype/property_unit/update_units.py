import frappe

def update_unit(doc,event):
    if doc.property_unit:        
        udoc = frappe.get_doc('Property Unit', doc.property_unit)
        #print(f"{udoc.unit_no}")
        udoc.contract_start_date = doc.contract_start_date
        udoc.contract_end_date = doc.contract_end_date
        udoc.customer_name = doc.customer_name        
        udoc.unit_status = 'Occupied'
        udoc.contract_issue_date=doc.posting_date if doc.doctype=='Sales Invoice' else doc.transaction_date,
        udoc.save()        
        #frappe.throw("Error")

def validate_unit(doc,event):

    if doc.auto_repeat:
        auto=frappe.get_doc('Auto Repeat', doc.auto_repeat)
        if auto.reference_document!=doc.name:
            sales_order=frappe.db.get_value('Sales Invoice Item', {'parent': auto.reference_document,'sales_order':['!=','']}, ['sales_order'])
            doc.contract_start_date=frappe.utils.today()
            doc.contract_end_date=frappe.utils.today()
            if sales_order:
                for itm in doc.items:
                    itm.update({'sales_order':sales_order})

    if doc.property_unit and doc.company!='AL NOKHBA BUILDING':
        if doc.contract_start_date and doc.contract_end_date:
            #prv=frappe.db.sql(""" select * from `tabSales Invoice` where docstatus=1 and property_unit='{unit}' and 
            #(('{start}' between contract_start_date and contract_end_date) 
            #OR ('{end}' between contract_start_date and contract_end_date))
            #""".format(unit=doc.property_unit,start=doc.contract_start_date,end=doc.contract_end_date)) or frappe.db.sql(""" 
            #select * from `tabSales Order` where docstatus=1 and property_unit='{unit}' and 
            #(('{start}' between contract_start_date and contract_end_date) 
            #OR ('{end}' between contract_start_date and contract_end_date))
            #""".format(unit=doc.property_unit,start=doc.contract_start_date,end=doc.contract_end_date))
            prv=frappe.db.sql(""" select * from `tabProperty Unit` where  name='{unit}' and 
            (('{start}' between contract_start_date and contract_end_date) 
            OR ('{end}' between contract_start_date and contract_end_date))
            """.format(unit=doc.property_unit,start=doc.contract_start_date,end=doc.contract_end_date),debug=0)
            if prv:       
                frappe.throw("selected property is not available for given contract period")
    return doc

def validate_unit_order(doc,event):
    if doc.property_unit:
        if doc.contract_start_date and doc.contract_end_date:
            #prv=frappe.db.sql(""" select * from `tabSales Invoice` where docstatus=1 and property_unit='{unit}' and 
            #(('{start}' between contract_start_date and contract_end_date) 
            #OR ('{end}' between contract_start_date and contract_end_date))
            #""".format(unit=doc.property_unit,start=doc.contract_start_date,end=doc.contract_end_date)) or frappe.db.sql(""" 
            #select * from `tabSales Order` where docstatus=1 and property_unit='{unit}' and 
            #(('{start}' between contract_start_date and contract_end_date) 
            #OR ('{end}' between contract_start_date and contract_end_date))
            #""".format(unit=doc.property_unit,start=doc.contract_start_date,end=doc.contract_end_date))

            prv=frappe.db.sql(""" select * from `tabProperty Unit` where  name='{unit}' and 
            (('{start}' between contract_start_date and contract_end_date) 
            OR ('{end}' between contract_start_date and contract_end_date))
            """.format(unit=doc.property_unit,start=doc.contract_start_date,end=doc.contract_end_date),debug=0)
            if prv:       
                frappe.throw("selected property is not available for given contract period")
            if prv:       
                frappe.throw("selected property is not available for given contract period")



def update_unit_status():
    units=frappe.db.sql("""select name from  `tabProperty Unit`   where contract_end_date < CURDATE() and contract_end_date <> '' and (unit_status ='Occupied' or unit_status ='Occupied - Legal') """)
    for unt in units:
        frappe.db.sql("""update `tabProperty Unit` set unit_status ='Vacant'  where name=%s """,unt[0])
        
    frappe.db.commit()
