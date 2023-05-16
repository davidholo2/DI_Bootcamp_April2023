class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise ValueError("Cannot add currencies with different labels")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError("Cannot add between Currency types <{}> and <{}>".format(
                    self.currency, other.currency))
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError("Unsupported operand type(s) for +=")
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))

result1 = c1 + 5
print(int(result1))

result2 = c1 + c2
print(int(result2))

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)
result3 = c1 + c3

print(result3)
