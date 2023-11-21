"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False



    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True 


    def get_total(self):
        """Calculate price, including tax."""

        self.base_price = 5
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



# class GovernmentMelonOrder(AbstractMelonOrder):

#     tax = 0
#     passed_inspection = False


#     def __repr__(self):

#         return f"species: {self.species}, amount: {self.qty}, shipped: {self.shipped}" 


#     def mark_inspection(self, passed):

#         if passed:
#             self.passed_inspection = True




