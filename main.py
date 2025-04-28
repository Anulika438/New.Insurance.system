from policyholder import PolicyHolder
from product import Product
from payment import Payment
import datetime


def main():
    # Create some products
    health_insurance = Product(
        id=1,
        name="Standard Health Insurance",
        description="Comprehensive health coverage for individuals",
        premium=299.99,
        coverage_amount=50000.00,
        term_length=12  # 12 months
    )

    auto_insurance = Product(
        id=2,
        name="Full Coverage Auto Insurance",
        description="Protection for your vehicle against accidents and theft",
        premium=150.00,
        coverage_amount=25000.00,
        term_length=6  # 6 months
    )

    home_insurance = Product(
        id=3,
        name="Home Insurance Premium",
        description="Complete protection for your home and belongings",
        premium=225.50,
        coverage_amount=350000.00,
        term_length=12  # 12 months
    )

    # Create policyholders
    adaobi = PolicyHolder(
        id=101,
        name="Adaobi Olaide",
        email="adaobi.olaide@gmail.com",
        phone="234-1234-5678",
        address="81 Martins St, Isolo, Nigeria"
    )

    sarah = PolicyHolder(
        id=102,
        name="Sarah Johnson",
        email="sarah.j@hotmail.com",
        phone="234-3456-6543",
        address="112 Sam Ave, Lekki, Nigeria"
    )

    # Register policies
    print("\n=== Policy Registration ===")
    print(adaobi.register_policy(health_insurance))
    print(adaobi.register_policy(home_insurance))
    print(sarah.register_policy(auto_insurance))
    print(sarah.register_policy(health_insurance))

    # Create payments
    today = datetime.datetime.now()
    due_date = today - datetime.timedelta(days=5)  # Due date was 5 days ago

    # Create payments for John
    adaobi_payment1 = Payment(
        id=1001,
        policyholder=adaobi,
        product=health_insurance,
        amount=health_insurance.premium,
        due_date=due_date
    )

    adaobi_payment2 = Payment(
        id=1002,
        policyholder=adaobi,
        product=home_insurance,
        amount=home_insurance.premium,
        due_date=due_date
    )

    # Create payments for Sarah
    sarah_payment1 = Payment(
        id=1003,
        policyholder=sarah,
        product=auto_insurance,
        amount=auto_insurance.premium,
        due_date=due_date
    )

    sarah_payment2 = Payment(
        id=1004,
        policyholder=sarah,
        product=health_insurance,
        amount=health_insurance.premium,
        due_date=due_date
    )

    # Process payments
    print("\n=== Payment Processing ===")
    print(f"Processing payment for {adaobi.name}'s {health_insurance.name}:")
    print(adaobi_payment1.process_payment(today, 299.99))  # Paid full amount but late

    print(f"\nProcessing payment for {adaobi.name}'s {home_insurance.name}:")
    print(adaobi_payment2.process_payment(today, 200.00))  # Partial payment and late

    print(f"\nProcessing payment for {sarah.name}'s {auto_insurance.name}:")
    print(sarah_payment1.process_payment(today - datetime.timedelta(days=7), 150.00))  # Paid on time

    print(f"\nProcessing payment for {sarah.name}'s {health_insurance.name}:")
    print(sarah_payment2.process_payment(today, 250.00))  # Partial payment and late

    # Add payments to policyholder history
    adaobi.add_payment(adaobi_payment1)
    adaobi.add_payment(adaobi_payment2)
    sarah.add_payment(sarah_payment1)
    sarah.add_payment(sarah_payment2)

    # Send reminder for the partial payments
    print("\n=== Payment Reminders ===")
    print(adaobi_payment2.send_reminder())
    print(sarah_payment2.send_reminder())

    # Calculate penalties for late payments
    print("\n=== Penalty Calculation ===")
    adaobi_penalty = adaobi_payment2.calculate_penalties(today)
    print(f"Penalty for {adaobi.name}'s home insurance payment: ${adaobi_penalty:.2f}")

    # Test product updates
    print("\n=== Product Management ===")
    print(health_insurance.update(coverage_amount=60000.00))
    print(auto_insurance.suspend("Seasonal suspension"))
    print(auto_insurance.reactivate())

    # Test policyholder management
    print("\n=== Policyholder Management ===")
    print(adaobi.update_details(phone="234-1234-5678"))
    print(sarah.suspend("Temporary suspension requested by customer"))
    print(sarah.reactivate())

    # Display account details for demonstration
    print("\n=== Adaobi's Account Details ===")
    adaobi_details = adaobi.get_account_details()
    for key, value in adaobi_details.items():
        print(f"{key}: {value}")

    print("\n=== Sarah's Account Details ===")
    sarah_details = sarah.get_account_details()
    for key, value in sarah_details.items():
        print(f"{key}: {value}")

    # Display product details
    print("\n=== Health Insurance Product Details ===")
    health_details = health_insurance.get_details()
    for key, value in health_details.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()