class TwoSum:
    numbersStream = None

    def __init__(self):
        self.numbersStream = {}

    def add(self, number: int) -> None:
        if number in self.numbersStream:
            self.numbersStream[number] += 1
        else:
            self.numbersStream[number] = 1


    def find(self, value: int) -> bool:
        for num in self.numbersStream:
            diff = value - num

            if (diff == num and self.numbersStream[diff] > 1) or (diff != num and diff in self.numbersStream):
                return True

        return False




# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)