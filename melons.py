"""This file should have our melon-type classes in it."""

class MelonOrder(object):
    melon_price = 5

    def get_base_price(self):

        return self.melon_price

class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    discount = 0.75
    discount_qty = 3

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * int(qty)
        if qty >= self.discount_qty:
            total = self.discount * total


        return total

class CantaloupeOrder(MelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    discount = 0.5
    discount_qty = 5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * int(qty)
        if qty >= self.discount_qty:
            total = self.discount * total

        return total

class CasabaOrder(MelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = (self.get_base_price() + 1) * self.shipping_cost * int(qty)

        return total

class SharlynOrder(MelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * self.shipping_cost * int(qty)

        return total

class SantaClausOrder(MelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * self.shipping_cost * int(qty)

        return total

class ChristmasOrder(MelonOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * int(qty)

        return total

class HornedMelonOrder(MelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * self.shipping_cost * int(qty)

        return total

class XiguaOrder(MelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    shipping_cost = 1.5
    square_surcharge = 2

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.get_base_price() * self.square_surcharge *  self.shipping_cost * int(qty)

        return total

class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = (self.get_base_price() + 1) *  int(qty)

        return total                

