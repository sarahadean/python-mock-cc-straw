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

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str):
            self._name = name
        else:
            raise Exception
    
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return list(set(self._visitors))
    
    def total_visits(self):
        return len(self._trips)
    
    #returns the visitor who has visited the park the most
    #[Joe, Jay, Tom, Joe, Sam, Joe]
    # max(set(List), key = List.count)
    def best_visitor(self):
        return max(set(self._visitors), key=self._visitors.count)
