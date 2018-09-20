class Clerk(object):
    def __init__(self):
        self.clerkName = self.getclerkName()

    def getClerkName(self):
        return "Clerk PQR"

    def setClerkName(self,name):
        self.clerkName = name

if __name__ == "__main__":
    x = Clerk()