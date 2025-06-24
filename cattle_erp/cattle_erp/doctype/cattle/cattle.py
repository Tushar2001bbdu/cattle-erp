# Copyright (c) 2025, Tushar Kumar Gupta and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today
from datetime import datetime

class Cattle(Document):
    def before_insert(self):
        if frappe.session.user != "Administrator":
            if self.owner != frappe.session.user:
                frappe.throw("You are not allowed to modify this record.")

    
        if self.date_of_birth:
            birth_date = datetime.strptime(str(self.date_of_birth), "%Y-%m-%d")
            today_date = datetime.strptime(today(), "%Y-%m-%d")
            self.age = (today_date - birth_date).days
        self.tag_id = f"{self.breed}{str(self.age)}"
