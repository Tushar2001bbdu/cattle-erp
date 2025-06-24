# Copyright (c) 2025, Tushar Kumar Gupta and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class VetDoctor(Document):
	def before_submit(self):
		if frappe.session.user != "Administrator":
            if self.owner != frappe.session.user:
                frappe.throw("You are not allowed to modify this record.")
