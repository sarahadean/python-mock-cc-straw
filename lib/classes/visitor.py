# Deliverables:
# Visitor __init__(self, name)
#       Visitor should be initialized with a name

# Visitor property name
#       Return name
#       Names must be of type str
#       Names must be between 1 and 15 characters, inclusive
#       raise Exception if setter fails

# Visitor trips()
#       Returns a list of all trips for that visitor
#       The list of trips must contain type Trip

# Visitor national_parks()
#       Returns a unique list of all parks who that visitor has visited.
#       The list of national parks must contain type NationalPark


class Visitor:
    # all = []
    
    def __init__(self, name):
        self.name = name
        self._trips = [] #trips this individual visitor has taken
        self._national_parks = [] #unique list of national parks visited - passing new nat'l park

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark):
            self._national_parks.append(new_national_park)
        return list(set(self._national_parks))