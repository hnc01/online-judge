'''
    https://leetcode.com/problems/snapshot-array/

    1146. Snapshot Array

    Implement a SnapshotArray that supports the following interface:

    - SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
    - void set(index, val) sets the element at the given index to be equal to val.
    - int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
    - int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
'''

'''
    Accepted
'''


class SnapshotArray:
    # the current snap ID
    snap_id = 0
    # will map each index to its value if it changes in snapshot
    history = {}

    def __init__(self, length: int):
        for i in range(0, length):
            self.history[i] = [(self.snap_id, 0)]

    def set(self, index: int, val: int) -> None:
        # the value of index at current snap_id to val
        if index < len(self.history):
            # check if the last entry in self.history belongs to current snap_id
            if self.history[index][-1][0] == self.snap_id:
                # the last element is current snap_id so we need to replace the entry
                self.history[index][-1] = (self.snap_id, val)
            else:
                # we don't have any recording of value change in current snap_id so we add it
                self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        old_snap_id = self.snap_id

        self.snap_id += 1

        return old_snap_id

    def get(self, index: int, snap_id: int) -> int:
        # we had to use the iterative version of binary search because the other one was getting
        # runtime error because it exceeded max recursion depth limit
        def binarySearch(history, s, e):
            nonlocal snap_id

            while s <= e:
                mid = s + (e - s) // 2

                # Check if x is present at mid
                if history[mid][0] == snap_id:
                    return mid

                # If x is greater, ignore left half
                elif history[mid][0] < snap_id:
                    s = mid + 1

                # If x is smaller, ignore right half
                else:
                    e = mid - 1

                # If we reach here, then the element
                # was not present

            return e

        if index < len(self.history):
            # first we get all the snaps where the index was changed
            index_history = self.history[index]

            # now we need to see if the snap_id is in the history using binary search
            snap_id_index = binarySearch(index_history, 0, len(index_history) - 1)

            if index_history[snap_id_index][0] == snap_id:
                # if we found the snap_id we're looking for
                return index_history[snap_id_index][1]
            elif index_history[snap_id_index][0] < snap_id:
                # if the snap_id we found is before the one we were looking for, then we return it
                return index_history[snap_id_index][1]
            else:
                # if the snap_id we found is after the one we're looking for then we get the one before it
                return index_history[snap_id_index - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(3)
# obj.set(0, 1)
# obj.set(1, 14)
# obj.snap()
# print(obj.get(0, 0))
# obj.set(0, 2)
# obj.snap()
# print(obj.get(0, 0))
# print(obj.get(1, 0))
# print(obj.get(1, 1))

obj = SnapshotArray(3)
obj.set(1, 6)
obj.snap()
obj.snap()
obj.set(1, 19)
obj.set(0, 4)
print(obj.get(2, 1))  # 0
print(obj.get(2, 0))  # 0
print(obj.get(0, 1))  # 0
