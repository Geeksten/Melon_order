"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    melon_price = 5
    discount = 0.75
    discount_qty = 3

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * int(qty)
        if qty >= self.discount_qty:
            total = self.discount * total


        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    melon_price = 5
    discount = 0.5
    discount_qty = 5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * int(qty)
        if qty >= self.discount_qty:
            total = self.discount * total

        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    melon_price = 6
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * self.shipping_cost * int(qty)

        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    melon_price = 5
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * self.shipping_cost * int(qty)

        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    melon_price = 5
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * self.shipping_cost * int(qty)

        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']
    melon_price = 5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * int(qty)

        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    melon_price = 5
    shipping_cost = 1.5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * self.shipping_cost * int(qty)

        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    melon_price = 5
    shipping_cost = 1.5
    square_surcharge = 2

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price * self.square_surcharge *  self.shipping_cost * int(qty)

        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    melon_price = 6

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered.

         Return a float of the total price.
        """
        total = self.melon_price *  int(qty)

        return total                

# class Melon(object):
#     name = None
#     color = None
#     is_imported = None
#     shape = None
#     season = None

