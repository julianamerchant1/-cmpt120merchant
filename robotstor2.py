#RobotStoreNew.py Altered RobotStore program, part 2 of lab.
#JULIANA MERCHANT

class Product():
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def has_enough_in_stock(self, count):
        return count <= self.stock
    
    def cost_of_products(self, count):
        return count * self.price
    
    def remove_product_from_stock(self, count):
        self.stock = self.stock - count
a = Product("Ultrasonic range finder", 2.5, 4)
b = Product("Servo motor", 14.99, 10)
c = Product("Servo controller", 44.95, 5)
d = Product("Microcontroller Board", 34.95, 7)
e = Product("Laser range finder", 149.99, 2)
f = Product("Lithium polymer battery", 8.99, 8)
products = [
            a, b, c, d, e, f
            ]
#print(a.has_enough_in_stock(4)), True
#print(a.has_enough_in_stock(11)), False
#print(a.cost_of_products(3))
#print(a.stock) # 4
#a.remove_product_from_stock(2)
#print(a.stock) # 2
#checking validity of new class created ^


#productNames = [ "Ultrasonic range finder"
#     , "Servo motor"
#     , "Servo controller"
#     , "Microcontroller Board"
#     , "Laser range finder"
#     , "Lithium polymer battery"
#     ]
#productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
#productQuantities = [ 4, 10, 5, 7, 2, 8 ]
#all still true, must be changed to work with class created

def printStockNew():
    print()
    print("Available Products")
    print("------------------")
    if cash > 0:
        print(product.stock)
        
#OLD CODE:        
#def printStock():
#    print()
#    print("Available Products")
#    print("------------------")
#    for i in range(0,len(productNames)):
#        if productQuantities[i] > 0:
#            print(str(i)+")",productNames[i], "$", productPrices[i])
#    print ()

def main():
    cash = float(input("How much money do you have?. If you have none, have a nice day anyway! $"))
#    while cash > 0:
#    printStock()

    while cash > 0:
        print(self.stock) # not working as an alt to printStock to output created classes for product list
        # says 'self' is undefined, improperly calling?
        vals = input("Enter product ID and quantity you wish to buy, or quit if you wish to: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        
        if self.stock[prodId] >= count:
            if cash >= self.price[prodId]:
                self.stock[prodId] -= count
                cash -= self.price[prodId] * count
                print("You purchased", count, self.name[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
             print("Sorry, we are sold out of", self.name[prodId])
# though not properly working toward the end, I did substitute my class names within the old program to attempt the new iteration
main()
