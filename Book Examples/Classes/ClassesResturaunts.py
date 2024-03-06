class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant1 = Restaurant('Mcdonalds', 'fast food')
restaurant2 = Restaurant('Tim Hortons', 'bad coffee')
restaurant3 = Restaurant('Starbucks','overpriced coffee')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



