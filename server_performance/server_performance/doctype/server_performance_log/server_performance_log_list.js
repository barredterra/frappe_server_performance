// Copyright (c) 2022, Raffael Meyer and contributors
// For license information, please see license.txt

frappe.listview_settings["Server Performance Log"] = {
	onload: function (listview) {
		frappe.require("logtypes.bundle.js", () => {
			frappe.utils.logtypes.show_log_retention_message("Server Performance Log");
		});
	},
};