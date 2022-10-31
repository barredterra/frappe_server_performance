# Copyright (c) 2022, Raffael Meyer and Contributors
# See license.txt
from psutil import cpu_percent, virtual_memory, disk_usage
from frappe import new_doc, get_site_path


def create_server_performance_log():
	perf_log = new_doc("Server Performance Log")
	perf_log.cpu_utilisation = cpu_percent()
	perf_log.ram_utilisation = virtual_memory().percent
	perf_log.disk_utilisation = disk_usage(get_site_path()).percent
	perf_log.save()
