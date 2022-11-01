# Copyright (c) 2022, Raffael Meyer and Contributors
# See license.txt
import frappe


def create_server_performance_log():
	return frappe.new_doc("Server Performance Log").save()
