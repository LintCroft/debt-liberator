from modules.DebtCalculation import DebtCalculation

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

debtCalc = DebtCalculation(990000.0, 15*12, 580.0, 0.03, 1200.0)

def formatGbp(f):
    #print("f is:{}".format(f))
    f = round(f, 2)
    if (f<0):
        return "-£{}".format(abs(f))
    else:
        return "£{}".format(f)

def yearsAndMonth(monthIndex):
    years = int((monthIndex+1)/12)
    month_of_year = (monthIndex+1)-years*12
    return years, month_of_year

def reportWithinRemainingMonths():
    for i in range(debtCalc.remaining_months):
        years, month_of_year = yearsAndMonth(i)
        debtCalc.calculate()
        if (i%12==0):
            print("---\nYear", years, "\n---\n")
        print("Month", i+1)
        print("Debt payment this month:{}".format(formatGbp(debtCalc.monthly_debt_payment)))
        print("Capital paid:{}".format(formatGbp(debtCalc.capital_paid)))
        if (debtCalc.debt > 0):
            print("Remaining debt:{}\n".format(formatGbp(debtCalc.debt)))
        else:
            print("\nYou're done after {} years and {} months. With {} to spare!\n".format(years, month_of_year, abs(round(debtCalc.debt, 2))))
            exit()

def reportIfOverExpectedMonths():
    extra_months = 0
    while(debtCalc.debt > 0):
        debtCalc.calculate()
        extra_months += 1
        if (extra_months == debtCalc.remaining_months+100):
            print("Calculation limit reached [{}]. Your outstanding debt is still {}".format(extra_months, formatGbp(debtCalc.debt)))
            exit()
    print("You needed an extra {} month(s) to clear your debt".format(extra_months))


if __name__== "__main__":
    reportWithinRemainingMonths()
    reportIfOverExpectedMonths()
