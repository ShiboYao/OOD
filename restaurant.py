'''
https://www.jiuzhang.com/problem/restaurant-oo-design/
'''
class Party(object):
    def __init__(self, capacity):
        self.capacity = capacity
    
    def getCapacity(self):
        return self.capacity


class Meal(object):
    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price


class Order(object):
    def __init__(self, meals=None):
        self.meals = meals
   
    def getMeals(self):
        return self.meals
    
    def orderDishes(self, meal): # Meal object
        self.meals.append(meal)
    
    def merge(order): # merge with another order
        if order is not None:
            self.meals.extend(order.meals)


class Table(object):
    def __init__(self, table_id, seats):
        self.available = True
        self.num_of_seats = seats
        self.table_id = table_id
        self.order = None

    def __lt__(self, other): #similar to comparator in C++
        return self.num_of_seats < other.num_of_seats

    def getTableId(self):
        return self.table_id
    
    def isAvailable(self):
        return self.available
    
    def markAvailable(self):
        self.available = True
        
    def markUnavailable(self):
        self.available = False
    
    def getNumOfSeats(self):
        return self.num_of_seats

    def setOrder(self, order): # copy the idea from Java solution
        if self.order is None:
            self.order = order
        else:
            self.order.merge(order)

    def getBill(self):
        bill = 0
        if self.order is not None:
            for m in self.order.getMeals():
                bill += m.price
        return bill


class Restaurant(object):
    def __init__(self):
        self.tables = [] 
        self.menu = []
    
    def addTable(self, table):
        self.tables.append(table)
        self.tables.sort() #keep sorted on key "num_of_seats"
        #assuming tables not changing frequently

    def addToMenu(self, meal):
        self.menu.append(meal) #assuming no redundancy

    def getMenu(self):
        return self.menu
    
    def findTable(self, party):
        num_of_guests = party.getCapacity()
        for table in self.tables:
            if not table.available:
                continue
            if table.num_of_seats >= num_of_guests:
                table.markUnavailable()
                return table
        return None
    
    def takeOrder(self, table_id, order):
        self.tables[table_id].setOrder(order)
       
    def checkOut(self, table_id):
        if table_id >= len(self.tables):
            raise ValueError("Invalid table id")
        bill = self.tables[table_id].getBill()
        self.tables[table_id].markAvailable()
        self.tables[table_id].order = None
        return bill
    
    def restaurantDescriptor(self):
        d = ""
        for i in range(len(self.tables)):
            table = self.tables[i]
            s = ("Table: " + str(i) + ", table size: " + str(table.num_of_seats) + ", is_available: " + str(table.available) + ". ")
            d += s
            if table.order is None:
                d += "No current orders"
            else:
                s =  ("Current Orders: " + str(table.getBill()))
                d += s
            d += ".\n"
        d += "********************"
        return d


if __name__ == "__main__":
    ## test case 0
    restaurant = Restaurant()
    #create 3 meals
    restaurant.addToMenu(Meal(10.0))
    restaurant.addToMenu(Meal(13.0))
    restaurant.addToMenu(Meal(17.0))

    #create 3 tables
    restaurant.addTable(Table(0,4)) #id, capacity
    restaurant.addTable(Table(1,4))
    restaurant.addTable(Table(2,10))

    #waiting party #perhaps using a queue is more appropriate
    p0 = Party(3)
    p1 = Party(7)
    p2 = Party(4)
    p3 = Party(6)
    p4 = Party(1)

    #create order
    o1 = Order([restaurant.menu[0]])
    o2 = Order([restaurant.menu[1],restaurant.menu[2]])

    #find table for 1,3,4
    restaurant.findTable(p0)
    print(restaurant.restaurantDescriptor())
    restaurant.findTable(p2)
    print(restaurant.restaurantDescriptor())
    restaurant.findTable(p3)
    print(restaurant.restaurantDescriptor())

    #table 1 had order 1
    restaurant.takeOrder(0, o1)
    print(restaurant.restaurantDescriptor())

    #table 3 had order 2
    restaurant.takeOrder(2, o2)
    print(restaurant.restaurantDescriptor())

    #table 3 checkout
    restaurant.checkOut(2)
    print(restaurant.restaurantDescriptor())

    #give p4 a table?
    restaurant.findTable(p4)
    print(restaurant.restaurantDescriptor())
 
    print("\n\n")

    ## test case 1
    restaurant = Restaurant()
    restaurant.addToMenu(Meal(12.0))
    restaurant.addTable(Table(0,4)) #id, capacity
    restaurant.addTable(Table(1,4))
    restaurant.addTable(Table(2,10))
    p0 = Party(13)
    restaurant.findTable(p0)
    print(restaurant.restaurantDescriptor())
