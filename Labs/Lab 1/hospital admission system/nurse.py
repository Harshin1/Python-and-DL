class Nurse(object):
    nurseEmp = 0;
    def __init__(self):
        self.nurseName = self.getNurseName()
        Nurse.nurseEmp += 1
        self.setNurseId(Nurse.nurseEmp)

    # return Nurse details
    def getNurseName(self):
        return "Nurse XYZ"

    # change Nurse for a patient
    def setNurseName(self,name):
        self.nurseName = name

    # get Nurse ID
    def getNurseId(self):
        return self.__nurseId

    # assign an ID to nurse
    def setNurseId(self, val):
        self.__nurseId = val

if __name__ == "__main__":
    x = Nurse()