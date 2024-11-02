"""Import the Account class from the Account.py file."""
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance:float, interest_rate:float, months:int):
    """Creates a savings account, calculates interest earned, and updates 
    the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.
    Returns:
        float: The updated savings account balance after adding the 
        interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and 
    # interest parameters.
    # Hint: You need to add the interest as a value, i.e, 0.
    savings_account = Account(balance,0)
    # Calculate interest earned
    interest_earned = balance * (interest_rate/100) * (months/12)
    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance 
    # of the SavingsAccount class.
    savings_account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance 
    # of the SavingsAccount class.
    savings_account.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return   float(savings_account.balance), float(savings_account.interest) 

if __name__ == "__main__":
    print("*" * 79)
    i_Balance = 1000
    i_interest = 0
    k_InterestRate = 1

    My_Account = Account(i_Balance,i_interest)
    print(f"My initial account balance is: {My_Account.balance}")
    print(f"My initial interest is: {My_Account.interest}")
    My_Account = Account(
        *create_savings_account(i_Balance,k_InterestRate, 12)
    )
    print(f"My final account balance is: {My_Account.balance}")
    print(f"My final interest is: {My_Account.interest}")
    print("*" * 79)