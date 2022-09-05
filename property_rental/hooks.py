from . import __version__ as app_version

app_name = "property_rental"
app_title = "Propery Management"
app_publisher = "alantechnologies"
app_description = "property rental management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jayakumar@alantechnologies.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/property_rental/css/property_rental.css"
# app_include_js = "/assets/property_rental/js/property_rental.js"

# include js, css files in header of web template
# web_include_css = "/assets/property_rental/css/property_rental.css"
# web_include_js = "/assets/property_rental/js/property_rental.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "property_rental/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "property_rental.install.before_install"
# after_install = "property_rental.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "property_rental.uninstall.before_uninstall"
# after_uninstall = "property_rental.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "property_rental.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
    "Sales Invoice": {
        "on_submit": "property_rental.propery_management.doctype.property_unit.update_units.update_unit",
        "before_insert": "property_rental.propery_management.doctype.property_unit.update_units.validate_unit",
    },
    "Sales Order": {
        "on_submit": "property_rental.propery_management.doctype.property_unit.update_units.update_unit",
        "before_insert": "property_rental.propery_management.doctype.property_unit.update_units.validate_unit",
    },
}
# Scheduled Tasks
# ---------------

scheduler_events = {

 	"daily": [
 		"property_rental.propery_management.doctype.property_unit.update_units.update_unit_status"
 	],

    }

# scheduler_events = {
# 	"all": [
# 		"property_rental.tasks.all"
# 	],
# 	"daily": [
# 		"property_rental.tasks.daily"
# 	],
# 	"hourly": [
# 		"property_rental.tasks.hourly"
# 	],
# 	"weekly": [
# 		"property_rental.tasks.weekly"
# 	]
# 	"monthly": [
# 		"property_rental.tasks.monthly"
# 	]
# }

# Testing
# -------
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                    "Sales Invoice-column_break_64",                    
                    "Sales Invoice-contract_end_date",
                    "Sales Invoice-contract_start_date",
                    "Sales Invoice-property_unit_details",
                    "Sales Invoice-property_unit",
                    "Sales Invoice-property",
                    "Property Unit-column_break_5",
                    'Request for Quotation-property_maintenance',
                    'Supplier Quotation-property_maintenance',
                    'Purchase Receipt-property_maintenance',
                    'Purchase Order-property_maintenance',
                    'Purchase Invoice-property_maintenance',
                    'Journal Entry-property_maintenance',
                    'Payment Entry-property_maintenance',
                    'Purchase Invoice Item-property_maintenance',
                    'Contract-property',
                    'Contract-property_unit',
                ),
            ]
        ],
    },
    { "doctype": "Client Script", "filters": [ ["name", "in", ( "Sales Invoice-Form","Contract-Form")] ] },
    'Property Type',
    'Project Type',

]
# before_tests = "property_rental.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "property_rental.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "property_rental.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"property_rental.auth.validate"
# ]

