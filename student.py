class Student:
    name ="Emily"
    age = 21
    school ="AkiraChix"
    nationality ="Kenyan"
    first_name ="liana"
    last_name ="Maria"
    country ="Kenya"
    
class Student:    
    school = "AkiraChix"
    def __init__(self,name,age,nationality,first_name,last_name,country): #used
        self.name =name
        self.age = age
        self.nationality = nationality
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        
    def greet_student(self):
        return f"Hello{self.name} welcome to {self.school} are you from {self.nationality}"
    
    def show_full_name(self):
        return f"Hello I am {self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        return f"My year of bith is {2023-self.age}"
    
    def show_initials(self):
        return f"{self.first_name[0].upper} {self.last_name[0].upper}"
        
        
  