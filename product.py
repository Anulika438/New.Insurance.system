class Product:
    def __init__(self, id, name, description, premium, coverage_amount, term_length):
        self.id = id
        self.name = name
        self.description = description
        self.premium = premium  # Regular payment amount
        self.coverage_amount = coverage_amount
        self.term_length = term_length  # in months
        self.status = "Active"
        self.creation_date = None
        self.last_updated = None
        import datetime
        self.creation_date = datetime.datetime.now()
        self.last_updated = self.creation_date

    def update(self, description=None, premium=None, coverage_amount=None, term_length=None):
        """Update product details"""
        if description:
            self.description = description
        if premium:
            self.premium = premium
        if coverage_amount:
            self.coverage_amount = coverage_amount
        if term_length:
            self.term_length = term_length

        import datetime
        self.last_updated = datetime.datetime.now()
        return f"Product {self.name} updated successfully"

    def suspend(self, reason):
        """Suspend the product"""
        if self.status == "Active":
            self.status = "Suspended"
            import datetime
            self.last_updated = datetime.datetime.now()
            return f"Product {self.name} suspended. Reason: {reason}"
        return f"Cannot suspend. Current status: {self.status}"

    def reactivate(self):
        """Reactivate a suspended product"""
        if self.status == "Suspended":
            self.status = "Active"
            import datetime
            self.last_updated = datetime.datetime.now()
            return f"Product {self.name} reactivated successfully"
        return f"Cannot reactivate. Current status: {self.status}"

    def remove(self):
        """Remove/deactivate a product"""
        if self.status != "Removed":
            self.status = "Removed"
            import datetime
            self.last_updated = datetime.datetime.now()
            return f"Product {self.name} removed successfully"
        return "Product already removed"

    def get_details(self):
        """Get detailed information about the product"""
        details = {
            "ID": self.id,
            "Name": self.name,
            "Description": self.description,
            "Premium": self.premium,
            "Coverage Amount": self.coverage_amount,
            "Term Length": f"{self.term_length} months",
            "Status": self.status,
            "Creation Date": self.creation_date,
            "Last Updated": self.last_updated
        }
        return details

    def __str__(self):
        return f"Product: {self.name} (ID: {self.id}), Premium: ${self.premium}, Status: {self.status}"