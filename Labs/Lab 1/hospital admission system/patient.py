class Patient(object):
    def __init__(self, name, age, disease):
        self.set_Patient_Details(name,age,disease)


    def set_Patient_Details(self,name,age,disease):
        self.name = name
        self.age = age
        self.disease = disease
        print('The patient details are: ')
        print(self.get_Patient_Details())

    def get_Patient_Name(self):
        return self.name

    def get_Patient_Age(self):
        return self.age

    def get_Patient_Disease(self):
        return self.disease

    def get_Patient_Details(self):
        return self.get_Patient_Name() + " " + str(self.get_Patient_Age()) + " " + self.get_Patient_Disease()

class VisitingPatient(Patient):

    def __init__(self):
        Patient.__init__(self)
        self.patientType = 'Visiting'


class InHousePatient(Patient):

    def __init__(self):
        Patient.__init__(self)
        self.patientType = 'InHouse'

if __name__ == "__main__":
    x = Patient("ABC",22,"fever")