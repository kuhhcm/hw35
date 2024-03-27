class Student:
    def __init__(self, name, age, __average):
        self.name = name
        self.age = age
        self.__average = __average
        
    def get_average(self):
        return self.__average
    
    def set_average(self, average):
        self.__average = average
        
    def info(self):
        return(f"Name: {self.name}, Age: {self.age}, Average: {self.get_average()}")
        

class HighCourser(Student):
    def __init__(self, name, age, __average, __graduate_work):
        super().__init__(name, age, __average)
        self.__graduate_work = __graduate_work
        
    def get_graduate_work(self):
        return self.__graduate_work
    
    def set_graduate_work(self, graduate_work):
        self.__graduate_work = graduate_work
        
    def info(self):
        return(f"Name: {self.name}, Age: {self.age}, Average: {self.get_average()}, Graduate work: {self.get_graduate_work()}")
        
        
student = Student("John", 15, 5.0)
higher_coursers = HighCourser("Jane", 16, 4.0, "Diploma")

print(student.info())
print(higher_coursers.info())