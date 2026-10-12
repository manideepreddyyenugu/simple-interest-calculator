class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self):
        return (self.principal * self.rate * self.time) / 100

# Usage
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

calculator = SimpleInterestCalculator(p, r, t)
print(f"Simple Interest: ${calculator.calculate():.2f}")   