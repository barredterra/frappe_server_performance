// Copyright (c) 2022, Raffael Meyer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server Performance Log", {
	refresh: function(frm) {
		frm.disable_save();
	}
});
