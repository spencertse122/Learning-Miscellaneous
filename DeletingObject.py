class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"Name:{self.name}\nid:{self.id}")

# Creating an emp instance of Employee class
emp = Employee(10, "John")
emp.display()
try:
    # Deleting the property of object
    del emp.id
except Exception as e:
    print("Error:", e)


print('-' * 20)
print(vars(emp))
