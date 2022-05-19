class ProductOfNumbers:
    # will hold the products of multiplying all the numbers together from the end of the array to the front
    products = None

    def __init__(self):
        # initialize empty products
        self.products = []

    def add(self, num: int) -> None:
        # we have 2 special cases: 0 and 1
        # when we are about to add a 0 to our products, it means that we have to make the entire products array a 0 because we'll be multiplying each entry by 1
        # when are about to add a 1 to our products, we don't change the array, we just append the 1
        # otherwise, we proceed normally

        if num == 0:
            # we reset the products array to 0 and we add an extra 0 at the end
            self.products = [0] * (len(self.products) + 1)
        elif num == 1:
            # we don't do any multiplication we just append the 1
            self.products.append(num)
        else:
            # when we add a new number, we multiply it by all the products we have so far (backwards) and then append it to the end
            for i in range(len(self.products) - 1, -1, -1):
                if self.products[i] != 0:
                    self.products[i] *= num
                else:
                    # everything from 0 to i will be 0 because we'd be multiplying the 0 by them
                    break

            self.products.append(num)

    def getProduct(self, k: int) -> int:
        # we already have the products accumulated so we just need to get the product from the array
        return self.products[-k]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)  # [3]
productOfNumbers.add(0)  # [3,0]
productOfNumbers.add(2)  # [3,0,2]
productOfNumbers.add(5)  # [3,0,2,5]
productOfNumbers.add(4)  # [3,0,2,5,4]
print(productOfNumbers.getProduct(2))  # return 20. The product of the last 2 numbers is 5 * 4 = 20
print(productOfNumbers.getProduct(3))  # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(productOfNumbers.getProduct(4))  # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)  # [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2))  # return 32. The product of the last 2 numbers is 4 * 8 = 32
