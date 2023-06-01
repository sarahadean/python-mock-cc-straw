#Deliverables:
# NationalPark property name
#       Returns the NationalPark's name
#       Should not be able to change after the NationalPark is created
#       raise Exception if setter fails

# NationalPark trips()
#       Returns a list of all trips planned for this national park
#       The list of trips must contain type trip

# NationalPark visitors()
#       Returns a unique list of all visitors a national park has recieved
#       The list of visitors must contain type Visitor

class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        self._trips = [] #list of trips planned for this nat'l park
        self._visitors = [] #unique list of visitors this nat'l park has rcvd