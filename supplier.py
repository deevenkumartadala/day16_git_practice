class Supplier:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

    def display(self):
        print("Supplier:",self.name)
        print("Phone Number:",self.phone)