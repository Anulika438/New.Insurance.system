Insurance System
This system provides an interface for insurance companies to manage policyholders, products, and payments. It allows policy managers to perform various tasks such as adding and suspending policyholders, registering new members, and managing policy products.
Project Structure
The project consists of the following Python files:

policyholder.py: Contains the PolicyHolder class for managing customer information
product.py: Contains the Product class for managing insurance products
payment.py: Contains the Payment class for processing payments and penalties
main.py: Demonstrates the functionality of the insurance system

Features
Policyholder Management

Register new policyholders
Suspend and reactivate policyholders
Update policyholder details
View policyholder account information

Product Management

Create insurance products with different coverage options
Update product details (description, premium, coverage amount, term length)
Suspend, reactivate, and remove products
View product details

Payment Management

Process payments for policies
Calculate penalties for late payments
Send payment reminders
Track payment history for policyholders

How to Use

Make sure you have Python 3.6 or later installed on your system.
Download or clone this repository to your local machine.
Navigate to the project directory in your terminal or command prompt.
Run the demonstration by executing:

python main.py
Class Details
PolicyHolder Class
The PolicyHolder class represents a customer who has purchased insurance policies.
Methods:

register_policy(product): Register a new policy for the policyholder
suspend(reason): Suspend the policyholder
reactivate(): Reactivate a suspended policyholder
add_payment(payment): Add a payment to the policyholder's history
get_payment_history(): Get the payment history
get_active_policies(): Get all active policies
update_details(email, phone, address): Update contact details
get_account_details(): Get detailed account information

Product Class
The Product class represents an insurance product that can be purchased by policyholders.
Methods:

update(description, premium, coverage_amount, term_length): Update product details
suspend(reason): Suspend the product
reactivate(): Reactivate a suspended product
remove(): Remove/deactivate a product
get_details(): Get detailed information about the product

Payment Class
The Payment class represents a payment made by a policyholder for a specific product.
Methods:

process_payment(payment_date, amount_paid): Process a payment
send_reminder(): Send a payment reminder
calculate_penalties(current_date): Calculate penalties for late payment
get_status(): Get detailed status of the payment

Example Usage
python# Create a policyholder
adaobi = PolicyHolder(
    id=101,
    name="Adaobi Olaide",
    email="adaobi.olaide@gmail.com",
    phone="234-1234-5678",
    address="81, Martins St, Isolo, Nigeria"
)

# Create an insurance product
health_insurance = Product(
    id=1,
    name="Standard Health Insurance",
    description="Comprehensive health coverage for individuals",
    premium=299.99,
    coverage_amount=50000.00,
    term_length=12
)

# Register the policy for the policyholder
adaobi.register_policy(health_insurance)

# Create a payment
payment = Payment(
    id=1001,
    policyholder=adaobi,
    product=health_insurance,
    amount=health_insurance.premium,
    due_date=datetime.datetime.now()
)

# Process the payment
payment.process_payment(datetime.datetime.now(), 299.99)

# Add the payment to the policyholder's history
adaobi.add_payment(payment)

# Display account details
account_details = adaobi.get_account_details()
Extending the System
You can extend this system by:

Adding more fields to the classes to store additional information
Implementing additional methods for specific business requirements
Creating a database backend to persist the data
Building a web interface to interact with the system
Adding reporting functionality to generate reports on policyholders and payments