def save_some_money():
    print("Calculate savings *for new clients*")
    years = int(input("How many years do you want to save?: "))
    premium_months = int(input("How many months bank offers higher interest rate?: "))
    interest_prem = float(input("What is premium interest rate? <10% = 10>: "))
    interest_stan = float(input("What is normal interest rate: "))    
    month_deposit = int(input("How much do you want to deposit monthly? Only full amount > 100zł: "))
    account = int(input("What's your principal? "))
    years_to_months = years * 12
    months = years_to_months - premium_months
    print("")
    for i in range(0, premium_months):
        account = (account + month_deposit)
    
    account = account * (1 + (interest_prem * 0.01))
    
    for j in range(0, months):
        account = (account + month_deposit) * (1 + (interest_stan * 0.01))
    print("Final capital: {:0.2f}zł".format(account))
    
if __name__ == "__main__":
    save_some_money()

