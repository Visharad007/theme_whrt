app_name = "theme_whrt"
app_title = "theme whrt"
app_publisher = "Visharad"
app_description = "Theme for Erpnext"
app_email = "vish@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "theme_whrt",
# 		"logo": "/assets/theme_whrt/logo.png",
# 		"title": "theme whrt",
# 		"route": "/theme_whrt",
# 		"has_permission": "theme_whrt.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/theme_whrt/css/theme_whrt.css"
# app_include_js = "/assets/theme_whrt/js/theme_whrt.js"

# include js, css files in header of web template
# web_include_css = "/assets/theme_whrt/css/theme_whrt.css"
# web_include_js = "/assets/theme_whrt/js/theme_whrt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "theme_whrt/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "theme_whrt/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "theme_whrt.utils.jinja_methods",
# 	"filters": "theme_whrt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "theme_whrt.install.before_install"
# after_install = "theme_whrt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "theme_whrt.uninstall.before_uninstall"
# after_uninstall = "theme_whrt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "theme_whrt.utils.before_app_install"
# after_app_install = "theme_whrt.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "theme_whrt.utils.before_app_uninstall"
# after_app_uninstall = "theme_whrt.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "theme_whrt.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"theme_whrt.tasks.all"
# 	],
# 	"daily": [
# 		"theme_whrt.tasks.daily"
# 	],
# 	"hourly": [
# 		"theme_whrt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"theme_whrt.tasks.weekly"
# 	],
# 	"monthly": [
# 		"theme_whrt.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "theme_whrt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "theme_whrt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "theme_whrt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["theme_whrt.utils.before_request"]
# after_request = ["theme_whrt.utils.after_request"]

# Job Events
# ----------
# before_job = ["theme_whrt.utils.before_job"]
# after_job = ["theme_whrt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"theme_whrt.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

