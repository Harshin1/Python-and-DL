from patient import Patient
from doctor import Doctor

class Book(Patient):
    def __init__(self):
        self.getDetails();

    def getDetails(self):
        self.name = input('Enter Patient name: ')
        self.age = input('Enter Patient Age: ')
        self.disease = input('Enter Patient disease: ')
        Patient.__init__(self,self.name,self.age,self.disease)
        self.getDoctorDetails()

    def getDoctorDetails(self):
        doc = Doctor()
        print('Your details are saved')

if __name__ == "__main__":
    x = Book()