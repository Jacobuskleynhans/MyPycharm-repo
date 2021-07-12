# Copy your Burrito class from the last exercise. Now, add
# a method called "get_cost" to the Burrito class. It should
# accept zero arguments (except for "self", of course) and
# it will return a float. Here's how the cost should be
# computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
# Make sure to return the result as a float even if the total
# is a round number (e.g. for burrito with no meat or
# guacamole, return 5.0 instead of 5).


# Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False,
                 corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

    def set_meat(self, meat):
        if meat == "chicken" or meat == "pork" or meat == "steak" or meat == "tofu":
            self.meat = meat
        else:
            self.meat = False

    def set_to_go(self, to_go):
        if to_go == True:
            self.to_go = True
        else:
            self.to_go = False

    def set_rice(self, rice):
        if rice == "brown" or rice == "white":
            self.rice = rice
        else:
            self.rice = False

    def set_beans(self, beans):
        if beans == "black" or beans == "pinto":
            self.beans = beans
        else:
            self.beans = False

    def set_extra_meat(self, extra_meat):
        if extra_meat == True:
            self.extra_meat = True
        else:
            self.extra_meat = False

    def set_guacamole(self, guacamole):
        if guacamole == True:
            self.guacamole = True
        else:
            self.guacamole = False

    def set_cheese(self, cheese):
        if cheese == True:
            self.cheese = True
        else:
            self.cheese = False

    def set_pico(self, pico):
        if pico == True:
            self.pico = True
        else:
            self.pico = False

    def set_corn(self, corn):
        if corn == True:
            self.corn = True
        else:
            self.corn = False

    def get_cost(self):
        base_cost = float(5.00)
        if self.meat == "chicken" or self.meat == "pork" or self.meat == "tofu":
            base_cost += float(1.00)
        elif self.meat == "steak":
            base_cost += float(1.50)
        if self.extra_meat == True and not self.meat == False:
            base_cost += float(1.00)
        if self.guacamole == True:
            base_cost += float(0.75)
        return base_cost


# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost


# Below are some lines of code that will test your class.
# You can change the value of the variable(s) to test your
# class with different inputs.
#
# If your function works correctly, this will originally
# print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat=True, guacamole=True)
print(a_burrito.get_cost())
