from nurse import Nurse
from clerk import Clerk

class Doctor(Nurse,Clerk):
    def __init__(self):
        self.doctorName = 'Dr. ABC'
        self.getHospNurse()
        self.getHospClerk()
        self.getDoctorName()

    # assign Nurse to patient
    def getHospNurse(self):
        print('The nurse is: ', end="")
        nurse = Nurse()
        print(nurse.nurseName)

    # assign Clerk to patient
    def getHospClerk(self):
        print('The clerk is: ', end="")
        print(Clerk.getClerkName(self))

    # assign Doctor to patient
    def getDoctorName(self):
        print('The doctor is: ',end="")
        print(self.doctorName)

if __name__ == "__main__":
    x = Doctor()