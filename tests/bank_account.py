# bank_account.py

def create_account(name, opening_balance=0):
    acct = {
        "name": name,
        # store integer balance
        "balance": 0,
        # transaction list
        "transactions": [],
    }
    if opening_balance != 0:
        acct["balance"] += opening_balance
        acct["transactions"].append(("opening_balance", opening_balance))
    return acct

def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        account["transactions"].append(("deposit", amount))
        return True
    raise ValueError("Amount must be a positive integer")

def withdraw(account, amount):
    if amount > 0 and amount <= account["balance"]:
        account["balance"] -= amount
        account["transactions"].append(("withdraw", amount))
        return True
    elif amount <= 0 or amount > account["balance"]:
        raise ValueError("Amount must be a positive integer and less than or equal to balance")

def transfer(from_account, to_account, amount):
    if isinstance(from_account, dict) and isinstance(to_account, dict):
        if amount > 0 and amount <= from_account["balance"]:
            from_account["balance"] -= amount
            from_account["transactions"].append(("transfer_out", amount))
            to_account["balance"] += amount
            to_account["transactions"].append(("transfer_in", amount))
            return True
        elif amount <= 0 or amount > from_account["balance"]:
            raise ValueError("Amount must be a positive integer and less than or equal to from_account balance")
        else:
            raise ValueError("Both accounts must be valid account dicts")
    else:
        raise ValueError("Both accounts must be valid account dicts")

def account_str(account):
    return f"{account['name']}: {account['balance']}"