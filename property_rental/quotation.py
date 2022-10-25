# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from collections import defaultdict

import frappe
from frappe import _
from frappe.utils import cint, cstr, flt, getdate
from erpnext.setup.utils import get_exchange_rate
from erpnext.stock.doctype.item.item import get_last_purchase_details

@frappe.whitelist()
def quotation_comparison(property_main):

	spli=[]

	supplier_list = frappe.db.sql(
			"""
			SELECT			
				DISTINCT sq.supplier as supplier_name,sq.discount_amount,sq.warranty,sq.payment_terms,sq.other_notes,sum(sqi.net_amount) as total,sq.name
			FROM
				`tabSupplier Quotation Item` sqi,
				`tabSupplier Quotation` sq
			WHERE
				sqi.parent = sq.name
				AND sq.docstatus < 2
				AND sq.property_maintenance='{0}'
				AND sq.status<>'Expired'
				group by sq.supplier order by sq.supplier """.format(
				property_main
			),
			as_dict=1,debug=0
			)

	item_list = frappe.db.sql(
			"""
			SELECT			
				DISTINCT(sqi.item_code) as item_code,sq.company,sqi.uom,sqi.qty,sqi.conversion_factor,sqi.item_name
			FROM
				`tabSupplier Quotation Item` sqi,
				`tabSupplier Quotation` sq
			WHERE
				sqi.parent = sq.name
				AND sq.docstatus < 2
				AND sq.status<>'Expired'
				AND sq.property_maintenance='{0}'
				group by sqi.item_code order by sqi.qty desc""".format(
				property_main
			),
			as_dict=1,debug=0
			)
	dta=[]
	for itm in item_list:
		dati={}
		last_purchase_details = get_last_purchase_details(itm.item_code)
		lastpur=0
		if last_purchase_details:
			lastpur = last_purchase_details["base_net_rate"]

		company_total_stock=0
		ac_qty=frappe.db.sql(""" select sum(actual_qty) as actual_qty from `tabBin` where item_code='{0}' 
		and warehouse in (select name from `tabWarehouse` where company='{1}') group by item_code""".format(itm.item_code,itm.company),as_dict=1,debug=0)
		if ac_qty:
			company_total_stock=ac_qty[0].actual_qty
		dati.update({'item_code':itm.item_code+'-'+itm.item_name,'uom':itm.uom,'qty':itm.qty,'last_purchase_rate':lastpur,'company_total_stock':company_total_stock})
		spi=[]
	
		for s in supplier_list:
			
			supplier_quotation_item = frappe.db.sql(
				"""
				SELECT			
					sqi.rate, sq.supplier as supplier_name,sqi.net_amount
				FROM
					`tabSupplier Quotation Item` sqi,
					`tabSupplier Quotation` sq
				WHERE
					sqi.parent = sq.name
					AND sq.docstatus < 2
					AND sq.status<>'Expired'
					AND sqi.item_code ='{0}'
					AND sq.name='{1}'
					AND sq.supplier='{2}'
					order by sq.supplier limit 0,1""".format(
					itm.item_code,s.name,s.supplier_name
				),
				as_dict=1,debug=0
				)

			if supplier_quotation_item:
				for si in supplier_quotation_item:
					#amt=pitem.qty*si.rate
					amt=si.net_amount					
					sp={}
					sp.update({'rate':si.rate,'amount':amt,'supplier':s.supplier_name})
					spi.append(sp)
			else:			
					sp={}
					sp.update({'rate':0,'amount':0,'supplier':s.supplier_name})
					spi.append(sp)
			
		dati.update({'sup':spi})
		dta.append(dati)

	#frappe.msgprint(str(dta))
	data={'items':dta,'suplier':supplier_list}
	return data

