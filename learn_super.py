class Employee:
    raise_amt = 2.00

    def __init__(self, first, last, pay) -> None:
        self.first =first
        self.last = last
        self.email = first + "_" + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first}, {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

class Developer(Employee):
    raise_amt= 1.04
    def __init__(self, first, last, pay, programming_lan) -> None:
        super().__init__(first, last, pay)
        self.lan = programming_lan

    def profile(self):
        return f"My name is {self.first}{self.last} and I am a {self.lan} programmer"

dev1 = Developer("Sam", "Emmanuel", 400, "Java")
dev2 = Developer("Eche", "Anakor", 700, "Python")
dev3 = Employee("Solo", "Agbado", 2000)
print(dev1.pay)
print(dev2.apply_raise())
dev3.fullname
print(dev1.profile())
print(dev2.profile())
#print(help(Developer))