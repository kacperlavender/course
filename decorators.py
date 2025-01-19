"""
Dectorator = A function that extends the behavior of another funcion
            without modifying the base funcion
            Pass the base funcion as an argument to the decorator

            We're adding something to base function without chaning it
"""
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print('syou add sprinkles')
        func(*args, **kwargs) #  treat is as -> print("here is your ice cream")
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print('you add fudge')
        func(*args, **kwargs)
    return wrapper



@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"here is your {flavour} ice cream")

get_ice_cream('vanilla')