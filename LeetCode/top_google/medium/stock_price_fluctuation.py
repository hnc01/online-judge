'''
    https://leetcode.com/problems/stock-price-fluctuation/

    2034. Stock Price Fluctuation


    You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price
    of the stock at that timestamp.

    Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse,
    some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

    Design an algorithm that:

    Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
    - Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
    - Finds the maximum price the stock has been based on the current records.
    - Finds the minimum price the stock has been based on the current records.

    Implement the StockPrice class:
        - StockPrice() Initializes the object with no price records.
        - void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
        - int current() Returns the latest price of the stock.
        - int maximum() Returns the maximum price of the stock.
        - int minimum() Returns the minimum price of the stock.
'''

'''
    Time limit exceeded
    
    Issue is that we're calling heapify every time we update an existing value. 
    
    To avoid this, we'll add both price and timestamp to the heap.
    
    ** According to the example from the documentation, you can use tuples, and it will sort by the first element of the tuple. **
'''

import heapq


class StockPrice:
    # to keep track of minimum price for stock
    min_heap = None
    # to keep track of maximum price for stock
    max_heap = None
    # timestamp heap: to keep track of maximum timestamp
    max_timestamp_heap = None
    # timestamp to price map
    timestamp_to_price = None

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.max_timestamp_heap = []
        self.timestamp_to_price = {}

    def update(self, timestamp: int, price: int) -> None:
        # first we need to see if we have timestamp in our timestamp_to_price map
        if timestamp in self.timestamp_to_price:
            # update the record
            old_price = self.timestamp_to_price[timestamp]

            if old_price != price:
                # we need to make the changes, otherwise we don't need to change anything
                self.timestamp_to_price[timestamp] = price

                # we need to readjust the heaps based on the update of a value
                self.min_heap = list(self.timestamp_to_price.values())
                self.max_heap = [-1 * p for p in self.timestamp_to_price.values()]

                heapq.heapify(self.min_heap)
                heapq.heapify(self.max_heap)
        else:
            # create the record
            self.timestamp_to_price[timestamp] = price

            # we need to add the new timestamp to the timestamps max heap
            heapq.heappush(self.max_timestamp_heap, -1 * timestamp)  # to make the min heap act as max heap

            # update the min heap and max heap
            heapq.heappush(self.min_heap, price)
            heapq.heappush(self.max_heap, -1 * price)  # to make the min heap act as max heap

    def current(self):
        # we need to take the max timestamp from the timestamp max heap
        max_timestamp = self.max_timestamp_heap[0] * -1

        return self.timestamp_to_price[max_timestamp]

    def maximum(self):
        return self.max_heap[0] * -1

    def minimum(self):
        return self.min_heap[0]


'''
    Accepted
'''


class StockPrice2:
    # to keep track of minimum price for stock
    min_heap = None
    # to keep track of maximum price for stock
    max_heap = None
    # to keep track of latest timestamp
    latest_timestamp = None
    # timestamp to price map
    timestamp_to_price = None

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.latest_timestamp = float('-inf')
        self.timestamp_to_price = {}

    def update(self, timestamp: int, price: int) -> None:
        # first we update the timestamp with the correct price
        self.timestamp_to_price[timestamp] = price

        # we update the latest timestamp
        self.latest_timestamp = max(self.latest_timestamp, timestamp)

        # we push the current price and timestamp tuple into the heaps
        # according to docs, the heaps will sort based on first element in tuple
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-1 * price, timestamp))

    def current(self):
        # we need to return the price of the latest timestamp
        return self.timestamp_to_price[self.latest_timestamp]

    def maximum(self):
        # the maximum is always the top element
        # however, if the top element is the old value of a timestamp, then we need
        # to discard this record and move on to the next top element
        top_timestamp = self.max_heap[0][1]
        top_price = -1 * self.max_heap[0][0]

        while top_price != self.timestamp_to_price[top_timestamp]:
            # we need to discard the element
            heapq.heappop(self.max_heap)

            top_timestamp = self.max_heap[0][1]
            top_price = -1 * self.max_heap[0][0]

        return top_price

    def minimum(self):
        # the minimum is always the top element
        # however, if the top element is the old value of a timestamp, then we need
        # to discard this record and move on to the next top element
        top_timestamp = self.min_heap[0][1]
        top_price = self.min_heap[0][0]

        while top_price != self.timestamp_to_price[top_timestamp]:
            # we need to discard the element
            heapq.heappop(self.min_heap)

            top_timestamp = self.min_heap[0][1]
            top_price = self.min_heap[0][0]

        return top_price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(1, 10)
# obj.update(2, 5)
# print(obj.current())
# print(obj.maximum())
# obj.update(1, 3)
# print(obj.maximum())
# obj.update(4, 2)
# print(obj.minimum())

obj = StockPrice2()

# commands = ["update", "maximum", "current", "maximum", "current", "minimum", "update", "maximum", "maximum", "current", "maximum", "current", "current", "maximum", "current", "update", "minimum",
#             "current", "minimum", "maximum", "current", "update", "update", "maximum", "update", "update", "minimum", "maximum", "minimum", "update", "minimum", "current", "maximum", "current",
#             "current", "update", "current", "maximum", "update", "maximum", "current", "maximum", "minimum", "minimum"]
# parameters = [[88, 9184], [], [], [], [], [], [83, 343], [], [], [], [], [], [], [], [], [87, 693], [], [], [], [], [], [88, 7810], [89, 624], [], [86, 9963], [88, 7345], [], [], [], [83, 5533], [],
#               [], [], [], [], [85, 4908], [], [], [85, 5125], [], [], [], [], []]

commands = ["update", "update", "update", "update", "update", "update", "update", "update", "update", "update", "maximum", "current", "maximum", "minimum", "minimum"]
parameters = [[88, 9184], [83, 343], [87, 693], [88, 7810], [89, 624], [86, 9963], [88, 7345], [83, 5533], [85, 4908], [85, 5125], [], [], [], [], []]

for i in range(0, len(commands)):
    command = commands[i]
    parameter = parameters[i]

    if command == "update":
        obj.update(parameter[0], parameter[1])
    elif command == "maximum":
        print(obj.maximum())
    elif command == "current":
        print(obj.current())
    elif command == "minimum":
        print(obj.minimum())
