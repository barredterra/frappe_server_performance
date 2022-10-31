# Copyright (c) 2022, Raffael Meyer and Contributors
# See license.txt
from frappe import get_single


def after_install():
	"""Add Server Performance Log to Log Settings.
	
	This sets up Server Performance Logs to be deleted after 7 days by
	default, but can be changed by the user.
	"""
	log_settings = get_single("Log Settings")
	log_settings.append(
		"logs_to_clear",
		{
			"ref_doctype": "Server Performance Log",
			"days": 7
		}
	)
	log_settings.save()


def before_uninstall():
	"""Remove Server Performance Log from Log Settings."""
	log_settings = get_single("Log Settings")
	log_settings.logs_to_clear = [
		log
		for log in log_settings.logs_to_clear
		if log.ref_doctype != "Server Performance Log"
	]
	log_settings.save()
