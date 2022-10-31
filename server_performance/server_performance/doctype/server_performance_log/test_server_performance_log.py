# Copyright (c) 2022, Raffael Meyer and Contributors
# See license.txt

from server_performance.server_performance.doctype.server_performance_log.server_performance_log import ServerPerformanceLog
from frappe.tests.utils import FrappeTestCase


class TestServerPerformanceLog(FrappeTestCase):
	def test_clear_old_logs(self):
		ServerPerformanceLog.clear_old_logs(days=7)
