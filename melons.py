import random
import datetime

"""Classes for melon orders."""

class TooManyMelonsError(ValueError):

    def __init__(self, message):  

        self.message = message
        super().__init__(self.message)     




class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_base_price(self):
        """Splurge pricing, randomily choose a base price for the order."""

        date_and_time = datetime.datetime.now()
        order_time = int(date_and_time.strftime("%H"))
        week_day_of_order = datetime.datetime.today()        

        base_price = random.randrange(5, 9)
        
        rush_order_price = 4               
        rush_hour = [8, 9, 10]
        rush_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        if order_time in rush_hour and week_day_of_order in rush_days:
            base_price = base_price + rush_order_price
            return base_price
        
        return base_price


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


    def get_total(self):
        """Calculate price, including tax."""

        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")
        
        self.base_price = self.get_base_price()        
        self.christmas_melon_price = self.base_price * 1.5

        if 'christmas melons' in self.species:
            total = (1 + self.tax) * self.qty * self.christmas_melon_price 
            return total
        else:
            total = (1 + self.tax) * self.qty * self.base_price

        return total         




class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08


    def __repr__(self):

        return f"species: {self.species}, amount: {self.qty}, shipped: {self.shipped}, order_type: {self.order_type}" 



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qtd, country_code):
        super().__init__(species, qtd)
  
        self.country_code = country_code    
        self.order_type = "international"
        self.tax = 0.17


    def __repr__(self):

        return f"species: {self.species}, amount: {self.qty}, shipped: {self.shipped}, order_type: {self.order_type}"      


    def get_total(self):
        total = super().get_total()
        """Calculate price, including tax."""     

        flat_fee = 3  
        
        if self.qty < 10:
            total = (1 + self.tax) * self.qty * self.base_price + flat_fee
            return total        
        
        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code



class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(self,species, qty)

        self.tax = 0
        self.passed_inspection = False


    def __repr__(self):

        return f"species: {self.species}, amount: {self.qty}, shipped: {self.shipped}" 


    def mark_inspection(self, passed):

        if passed:
            self.passed_inspection = True





