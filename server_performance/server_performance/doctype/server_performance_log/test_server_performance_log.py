# Copyright (c) 2022, Raffael Meyer and Contributors
# See license.txt

import frappe
from server_performance.server_performance.doctype.server_performance_log.server_performance_log import ServerPerformanceLog
from frappe.tests.utils import FrappeTestCase


class TestServerPerformanceLog(FrappeTestCase):
	def test_server_performance_log(self):
		performance_log = frappe.new_doc("Server Performance Log")

		self.assertIsNone(performance_log.cpu_utilisation)
		self.assertIsNone(performance_log.ram_utilisation)
		self.assertIsNone(performance_log.disk_utilisation)

		performance_log.save()

		self.assertIsInstance(performance_log.cpu_utilisation, float)
		self.assertIsInstance(performance_log.ram_utilisation, float)
		self.assertIsInstance(performance_log.disk_utilisation, float)

	def test_clear_old_logs(self):
		ServerPerformanceLog.clear_old_logs(days=7)
