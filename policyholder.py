class PolicyHolder:
    def __init__(self, id, name, email, phone, address):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.status = "Active"
        self.policies = []  # List to store policies (products) purchased by this policyholder
        self.payments = []  # List to store payment history
        self.creation_date = None
        self.last_updated = None
        import datetime
        self.creation_date = datetime.datetime.now()
        self.last_updated = self.creation_date

    def register_policy(self, product):
        """Register a new policy for the policyholder"""
        if self.status != "Active":
            return f"Cannot register new policy. Policyholder status: {self.status}"

        if product not in self.policies:
            self.policies.append(product)
            import datetime
            self.last_updated = datetime.datetime.now()
            return f"Policy {product.name} registered successfully for {self.name}"
        return f"Policy {product.name} already registered for this policyholder"

    def suspend(self, reason):
        """Suspend the policyholder"""
        if self.status == "Active":
            self.status = "Suspended"
            import datetime
            self.last_updated = datetime.datetime.now()
            return f"Policyholder {self.name} suspended. Reason: {reason}"
        return f"Cannot suspend. Current status: {self.status}"

    def reactivate(self):
        """Reactivate a suspended policyholder"""
        if self.status == "Suspended":
            self.status = "Active"
            import datetime
            self.last_updated = datetime.datetime.now()
            return f"Policyholder {self.name} reactivated successfully"
        return f"Cannot reactivate. Current status: {self.status}"

    def add_payment(self, payment):
        """Add a payment to the policyholder's payment history"""
        self.payments.append(payment)
        import datetime
        self.last_updated = datetime.datetime.now()
        return f"Payment {payment.id} added to {self.name}'s history"

    def get_payment_history(self):
        """Get the payment history for this policyholder"""
        return self.payments

    def get_active_policies(self):
        """Get all active policies for this policyholder"""
        return [policy for policy in self.policies if policy.status == "Active"]

    def update_details(self, email=None, phone=None, address=None):
        """Update policyholder contact details"""
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address

        import datetime
        self.last_updated = datetime.datetime.now()
        return f"Details for {self.name} updated successfully"

    def get_account_details(self):
        """Get detailed account information including policies and payments"""
        active_policies = [policy.name for policy in self.get_active_policies()]
        recent_payments = [f"{payment.id}: ${payment.amount} ({payment.status})"
                           for payment in self.payments[-5:]] if self.payments else []

        details = {
            "ID": self.id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Address": self.address,
            "Status": self.status,
            "Active Policies": active_policies,
            "Recent Payments": recent_payments,
            "Creation Date": self.creation_date,
            "Last Updated": self.last_updated
        }
        return details

    def __str__(self):
        return f"Policyholder: {self.name} (ID: {self.id}), Status: {self.status}, Policies: {len(self.policies)}"