'''
    https://leetcode.com/problems/employee-importance/

    690. Employee Importance


    You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

    You are given an array of employees employees where:

    - employees[i].id is the ID of the ith employee.
    - employees[i].importance is the importance value of the ith employee.
    - employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.

    Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.
'''


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: [int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: [Employee], id: int) -> int:
        # first let's map every ID to its employee so we can quickly access the employee through his ID
        id_to_employee = {}

        for employee in employees:
            id_to_employee[employee.id] = employee

        def bfs(node):
            total_importance = 0

            queue = []
            queue.append(node)

            while len(queue) != 0:
                current_employee = queue.pop(0)

                total_importance += current_employee.importance

                # add all the subordinates (given in ids need to map to employee objects) to the tree
                for sub_id in current_employee.subordinates:
                    queue.append(id_to_employee[sub_id])

            return total_importance

        # now we need to find the total importance of the employee with given id
        target_employee = id_to_employee[id]

        # now we need to bfs traverse the tree rooted at target_employee to get the total importance
        return bfs(target_employee)

# emp1 = Employee(1, 5, [2,3])
# emp2 = Employee(2, 3, [])
# emp3 = Employee(3, 3, [])
#
# print(Solution().getImportance([emp1, emp2, emp3], 1))


emp1 = Employee(1, 2, [5])
emp2 = Employee(5, -3, [])

print(Solution().getImportance([emp1, emp2], 5))