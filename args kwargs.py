def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2))


def displayname(*args):
    for arg in args:
        print(arg, end=" ")

displayname("dr", "spongebob", "squarepants", "III")


def print_addres(**kwargs):
    for key, value, in kwargs.items():
        print(f"{key}: {value}")

print_addres(street="karola", 
            city="krakow", 
            woj="malopolskie", 
            zip="1234",
            apt="100")


def shipping(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('woj')} {kwargs.get('zip')}")

shipping("dr", "spongebob", "squarepants", "III",
        street="123 street",
        apt="#100",
        city="krakow",
        woj="malopolskie",
        zip="12345")