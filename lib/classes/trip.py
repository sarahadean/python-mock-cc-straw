
#intermediary
#Deliverables:
# Trip __init__(self, visitor, national_park, start_date, end_date)
#       Trips should be initialized with a visitor, national_park, start_date(str), end_date(str)

#Trip property visitor
#       Returns the visitor object for that trip
#       Must be of type Visitor
#       raise Exception if setter fails

# Trip property national_park
#       Returns the NationalPark object for that trip
#       Must be of type NationalPark
#       raise Exception if setter fails
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        
        national_park.visitors(visitor) #double check these later
        national_park.trips(self)

        visitor.national_parks_visited(national_park)
        visitor.trips(self)
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("Invalid")



    @property
    def national_park(self):
        return self._national_park
        
    @national_park.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("Invalid")