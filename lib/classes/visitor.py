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

    def __init__(self, name):
        self.name = name
        self._trips = [] #trips this individual visitor has taken
        self._national_parks_visited = [] #unique list of national parks visited - passing new nat'l park

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Name must be between 1 and 15 characters")
    
    #Returns list of all trips this visitor has taken
    def trips(self, new_trip=None):
        from classes.trip import Trip

        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return [trip for trip in Trip.all if trip.visitor == self]
    #   return self._trips


    #Returns unique list of all national parks this visitor has visited
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        from classes.trip import Trip
        if isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks_visited:
            self._national_parks_visited.append(new_national_park)
        return [trip.national_park for trip in self.trips()]