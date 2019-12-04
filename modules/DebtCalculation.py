class DebtCalculation:

    def __init__(self, debt, remaining_months, monthly_payment, avg_annual_interest_rate, monthly_overpayment):
        self.debt = debt
        self.remaining_months = remaining_months
        self.monthly_payment = monthly_payment
        self.monthly_interest_rate = avg_annual_interest_rate/12
        self.monthly_overpayment = monthly_overpayment

    def calculate(self):
        #global monthly_debt_payment, capital_paid, debt
        self.monthly_debt_payment = self.debt * self.monthly_interest_rate
        self.capital_paid = (self.monthly_payment - self.monthly_debt_payment) + self.monthly_overpayment
        self.debt = self.debt - self.capital_paid
        return self.debt
