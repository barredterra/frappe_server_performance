# Copyright (c) 2022, Raffael Meyer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.query_builder import Interval
from frappe.query_builder.functions import Now


class ServerPerformanceLog(Document):
	@staticmethod
	def clear_old_logs(days=90):
		table = frappe.qb.DocType("Server Performance Log")
		frappe.db.delete(table, filters=(table.creation < (Now() - Interval(days=days))))
