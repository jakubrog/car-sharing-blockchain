from car_sharing import Owner, Car, Customer


def add_cars_to_rent(owner, car_names):
    for car in car_names:
        owner.add_car_to_rent(car[1], car[0])

def start():
    customer = Customer(500)
    owner = Owner(500)
    cars_and_prices = [("Ferrari", 50), ("Lamborghini", 40), ("Porsche", 30)]

    add_cars_to_rent(owner, cars_and_prices)


if __name__ == '__main__':
    start()
