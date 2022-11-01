# Copyright (c) 2022, Raffael Meyer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.query_builder import Interval
from frappe.query_builder.functions import Now
from psutil import cpu_percent, disk_usage, virtual_memory


class ServerPerformanceLog(Document):
	def before_insert(self):
		self.cpu_utilisation = cpu_percent()
		self.ram_utilisation = virtual_memory().percent
		self.disk_utilisation = disk_usage(frappe.get_site_path()).percent

	@staticmethod
	def clear_old_logs(days=90):
		table = frappe.qb.DocType("Server Performance Log")
		frappe.db.delete(table, filters=(table.creation < (Now() - Interval(days=days))))
