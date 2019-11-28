print("Liberate yourself from your mortgage\n")
# try:
#     debt = float(input("What is the total debt?\n"))
#     remaining_months = int(input("How many months are remaining in your term?\n"))
#     monthly_payment = float(input("What is your obligatory monthly payment?\n"))
#     avg_annual_interest_rate = float(input("What's the average APR % of the entire term?\n"))/100
#     monthly_overpayment = float(input("What's your average monthly overpayment?\n"))
# except Exception as e:
#     print(e)
#     exit()

debt = 98000.00
remaining_months = 15 * 12
monthly_payment = 580.00
avg_annual_interest_rate = 2 / 100
monthly_overpayment = 1200.00

monthly_interest_rate = avg_annual_interest_rate/12
monthly_debt_payment = ""
capital_paid = ""
remaining_debt = debt

def formatGbp(f):
    #print("f is:{}".format(f))
    f = round(f, 2)
    if (f<0):
        return "-£{}".format(abs(f))
    else:
        return "£{}".format(f)

def calculate():
    global remaining_debt, monthly_debt_payment, capital_paid, remaining_debt
    monthly_debt_payment = remaining_debt * monthly_interest_rate
    capital_paid = (monthly_payment - monthly_debt_payment) + monthly_overpayment
    remaining_debt = remaining_debt - capital_paid

def process():
    for i in range(remaining_months):
        calculate()
        if (i%12==0):
            print("---\nYear", int((i/12)+1), "\n---\n")
        print("Month", i+1)
        print("Debt payment this month:{}".format(formatGbp(monthly_debt_payment)))
        print("Capital paid:{}".format(formatGbp(capital_paid)))
        if (remaining_debt > 0):
            print("Remaining debt:{}".format(formatGbp(remaining_debt)))
        else:
            print("You're done! With {} to spare".format(abs(round(remaining_debt, 2))))
            exit()
        print()
    extra_months = 0
    while(remaining_debt > 0):
        calculate()
        extra_months += 1
        if (extra_months == remaining_months*100):
            print("Calculation limit. Your outstanding debt is still:{}".format(formatGbp(remaining_debt)))
            exit()
    print("You needed an extra {} month(s) to clear your debt".format(extra_months))


if __name__== "__main__":
    process()
