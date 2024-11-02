"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance:float, interest_rate:float, months:int):
    """Creates a CD account, calculates interest earned, and updates 
    the account balance.
    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.
    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance 
    # and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    cd_account = Account(balance,0)
    # Calculate interest earned
    interest_earned = balance * (interest_rate/100) * (months/12)
    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance 
    # of the CD Account class.
    cd_account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance 
    # of the CD Account class.
    cd_account.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return float(cd_account.balance), float(cd_account.interest) 

if __name__ == "__main__":
    print("*" * 79)
    i_Balance = 1000
    i_interest = 0
    k_InterestRate = 2
    m_months = 24
    
    My_Account = Account(i_Balance,i_interest)
    print(f"My initial account balance is: {My_Account.balance}")
    print(f"My initial interest is: {My_Account.interest}")
    My_Account = Account(
        *create_cd_account(i_Balance, k_InterestRate, m_months)
    )
    print(f"My final account balance is: {My_Account.balance}")
    print(f"My final interest is: {My_Account.interest}")
    print("*" * 79)