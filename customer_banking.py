# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    savings_balance = float(input("What is your savings account balance?: "))
    savings_interest = float(
        input("What is the APR for the savings account?: ")
    )
    savings_maturity = int(
        input(
            "What is the length of months you want to calculate the "
            "interest gained on the account?: "
        )
    )
    # Call the create_savings_account function and pass the variables 
    # from the user.
    updated_savings_balance, interest_earned = create_savings_account(
        savings_balance, 
        savings_interest, 
        savings_maturity
        )
    # Print out the interest earned and updated savings account balance with 
    # interest earned for the given months.
    print(f"The interest earned in your savings account is: "
          f"${interest_earned:,.2f}")
    print(f"The future savings account balance after "
          f"{savings_maturity} month(s)is: ${updated_savings_balance:,.2f}")
    # Prompt the user to set the CD balance, interest rate, and months for the 
    # CD account.
    cd_balance = float(input("What is your initial CD account balance?: "))
    cd_interest = float(input("What is the APR for the CD account?: "))
    cd_maturity = int(input("What is the length of months for your CD?: "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, 
        cd_interest, 
        cd_maturity
    )
    # Print out the interest earned and updated CD account balance with 
    # interest earned for the given months.
    print(f"The interest earned in your savings account is: "
          f"${cd_interest_earned:,.2f}")
    print(f"The future savings account balance after {cd_maturity} is : "
          f"${updated_cd_balance:,.2f}")
if __name__ == "__main__":
    # Call the main function.
    main()