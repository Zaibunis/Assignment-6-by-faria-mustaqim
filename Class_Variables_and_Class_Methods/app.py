class Bank:
    bank_name = "Bank of Python"

    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
b1.change_bank_name("Bank of Typescript")
b2.change_bank_name("Bank of Java")
print(b1.bank_name)  
print(b2.bank_name)
