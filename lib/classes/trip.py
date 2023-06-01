
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
     