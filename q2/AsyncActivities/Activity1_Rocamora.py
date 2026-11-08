class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def add_bill(self, amount):
        self.__bill_amount += amount

    @property
    def get_name(self):
        return self.__name  
    
    @get_name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def get_bill_amount(self):
        return self.__bill_amount 

    @get_bill_amount.setter
    def set_bill_amount(self, amount):
        self.__bill_amount = amount

    @property
    def calculate_bill(self):
        print(f"Original bill for {self.get_name} is: ${self.get_bill_amount}")
        print(f"Final bill for {self.get_name} is: ${self.get_bill_amount}")     

class Senior(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        
    @property
    def calculate_bill(self):
            print(f"Original bill for {self.get_name} is: ${self.get_bill_amount}")
            print(f"Final bill for {self.get_name} is: ${self.get_bill_amount * 0.80}")


class PhilHealth(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
            
    @property
    def calculate_bill(self):
        print(f"Original bill for {self.get_name} is: ${self.get_bill_amount}")
        print(f"Final bill for {self.get_name} is: ${self.get_bill_amount * 0.85}")

Tinoy = Patient("Tinoy", 1000)
Estiquo = Senior("Estiquo", 1000)
Rina = PhilHealth("Rina", 1000)

patients = [Tinoy, Rina, Estiquo]

for patient in patients:
    print(f"Patient Name: {patient.get_name}")
    patient.calculate_bill
