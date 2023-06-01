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

   