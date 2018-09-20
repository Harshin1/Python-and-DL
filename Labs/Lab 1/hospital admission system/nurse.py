class Nurse(object):
    nurseEmp = 0;
    def __init__(self):
        self.nurseName = self.getNurseName()
        Nurse.nurseEmp += 1
        self.setNurseId(Nurse.nurseEmp)

    def getNurseName(self):
        return "Nurse XYZ"

    def setNurseName(self,name):
        self.nurseName = name

    def getNurseId(self):
        return self.__nurseId

    def setNurseId(self, val):
        self.__nurseId = val

if __name__ == "__main__":
    x = Nurse()