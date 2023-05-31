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

    def __init__(self, name):
        self.name = name
        self._trips = [] #list of trips planned for this nat'l park
        self._visitors = [] #unique list of visitors this nat'l park has rcvd

    @property
    def name(self):
        return self._name
    
    # and hasattr(str):
    @name.setter
    def name(self, name):
        # if not isinstance(self, NationalPark) and hasattr(name, str):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Invalid")
    

    # Returns a list of all trips planned for this national park
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return [trip for trip in Trip.all if trip.national_park == self]
    #   return self._trips
    

    # Returns unique list of visitors this nat'l park has rcvd
    #passing in visitor for this nat park
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor

        if new_visitor and isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return [trip.visitor for trip in self.trips()]
    


    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        pass

# carlsbad_caverns = NationalPark("Carlsbad Caverns")
# carlsbad_caverns.name = "New Name"
# print(carlsbad_caverns.name)