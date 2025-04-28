class Payment:
    def __init__(self, id, policyholder, product, amount, due_date):
        self.id = id
        self.policyholder = policyholder
        self.product = product
        self.amount = amount
        self.due_date = due_date
        self.payment_date = None
        self.status = "Pending"
        self.penalties = 0
        self.reminders_sent = 0

    def process_payment(self, payment_date, amount_paid):
        """Process a payment for a policy"""
        import datetime

        if self.status == "Paid":
            return "Payment already processed"

        self.payment_date = payment_date

        # Check if payment is on time
        if payment_date > self.due_date:
            days_late = (payment_date - self.due_date).days
            # Apply penalty if late (5% of amount per week late)
            weeks_late = days_late // 7 + (1 if days_late % 7 > 0 else 0)
            self.penalties = self.amount * 0.05 * weeks_late
            total_due = self.amount + self.penalties

            if amount_paid >= total_due:
                self.status = "Paid"
                overpayment = amount_paid - total_due
                return f"Payment processed with penalties. Penalties: ${self.penalties}. Overpayment: ${overpayment}"
            else:
                self.status = "Partially Paid"
                remaining = total_due - amount_paid
                return f"Partial payment processed. Remaining (incl. penalties): ${remaining}"
        else:
            # On-time payment
            if amount_paid >= self.amount:
                self.status = "Paid"
                overpayment = amount_paid - self.amount
                return f"Payment processed successfully. Overpayment: ${overpayment}"
            else:
                self.status = "Partially Paid"
                remaining = self.amount - amount_paid
                return f"Partial payment processed. Remaining: ${remaining}"

    def send_reminder(self):
        """Send a payment reminder to the policyholder"""
        if self.status in ["Pending", "Partially Paid"]:
            self.reminders_sent += 1
            return f"Reminder #{self.reminders_sent} sent to {self.policyholder.name} for product {self.product.name}"
        return "No reminder needed"

    def calculate_penalties(self, current_date):
        """Calculate penalties for late payment"""
        if self.status in ["Pending", "Partially Paid"] and current_date > self.due_date:
            days_late = (current_date - self.due_date).days
            # Apply penalty if late (5% of amount per week late)
            weeks_late = days_late // 7 + (1 if days_late % 7 > 0 else 0)
            self.penalties = self.amount * 0.05 * weeks_late
            return self.penalties
        return 0

    def get_status(self):
        """Get detailed status of the payment"""
        details = {
            "ID": self.id,
            "Policyholder": self.policyholder.name,
            "Product": self.product.name,
            "Amount": self.amount,
            "Due Date": self.due_date,
            "Payment Date": self.payment_date,
            "Status": self.status,
            "Penalties": self.penalties,
            "Reminders Sent": self.reminders_sent
        }
        return details

    def __str__(self):
        return f"Payment: {self.id}, Amount: ${self.amount}, Status: {self.status}"