class Sneaker:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price
class SneakerStore:
    def __init__(self):
        self.stock = []
    def add_sneaker(self, brand, size, price):
        sneaker = Sneaker(brand, size, price)
        self.stock.append(sneaker)
        print("Были добавлены " + brand + " " + str(size) + " " + str(price))
    def display_stock(self):
        if self.stock == []:
            print("Склад пустой")
        else:
            print("В складе есть:")
            for sneaker in self.stock:
                    print(sneaker.brand, sneaker.size, sneaker.price)
    def buy_sneaker(self, brand, size, budget):
        for sneaker in self.stock:
            if sneaker.brand == brand and sneaker.size == size:
                if(budget >= sneaker.price):
                    self.stock.remove(sneaker)
                    print("Ты купил " + brand + " " + str(size))
                    return
                else:
                    print("Недостаточно средств")
                    return
        print("Таких кросс нету в наличии")
budget = int(input())
store = SneakerStore()
store.add_sneaker("Nike", 41, 15000)
store.add_sneaker("Adidas", 52, 19000)
store.add_sneaker("Dolce Banana", 38, 13000)
store.display_stock()
store.buy_sneaker("Adidas", 52, budget)

