class Patient(object):
    def __init__(self, name, age, disease):
        self.set_Patient_Details(name,age,disease)

    # set Patient Details
    def set_Patient_Details(self,name,age,disease):
        self.name = name
        self.age = age
        self.disease = disease
        print('The patient details are: ')
        print(self.get_Patient_Details())

    # Get Patient Name
    def get_Patient_Name(self):
        return self.name

    # Get Patient Age
    def get_Patient_Age(self):
        return self.age

    # Get Patient Disease
    def get_Patient_Disease(self):
        return self.disease

    # Get Patient Details
    def get_Patient_Details(self):
        return self.get_Patient_Name() + " " + str(self.get_Patient_Age()) + " " + self.get_Patient_Disease()

class VisitingPatient(Patient):

    #assigning patient type
    def __init__(self):
        Patient.__init__(self)
        self.patientType = 'Visiting'


class InHousePatient(Patient):

    # assigning patient type
    def __init__(self):
        Patient.__init__(self)
        self.patientType = 'InHouse'

if __name__ == "__main__":
    x = Patient("ABC",22,"fever")