'''
    https://leetcode.com/problems/number-of-atoms/

    726. Number of Atoms

    Given a string formula representing a chemical formula, return the count of each atom.

    The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

    One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
    - For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.

    Two formulas are concatenated together to produce another formula.
    - For example, "H2O2He3Mg4" is also a formula.

    A formula placed in parentheses, and a count (optionally added) is also a formula.
    - For example, "(H2O2)" and "(H2O2)3" are formulas.

    Return the count of all elements as a string in the following form: the first name (in sorted order),
    followed by its count (if that count is more than 1), followed by the second name (in sorted order),
    followed by its count (if that count is more than 1), and so on.

    The test cases are generated so that all the values in the output fit in a 32-bit integer.
'''

class Solution:
    def countOfAtomsHelper(self, formula, atomCounts):
        # to be able to process ( ) structure
        stack = []

        i = 0

        while i < len(formula):
            # when we see an atom, we directly add its count to atomCounts
            # when we see a ( we push into the stack until we hit a ) at which case we pop the stack until we hit a (
            if formula[i].isalpha() and formula[i].isupper():
                # we have an atom so we need to extract it and add its count to atomCounts
                atom = formula[i]

                offset = 1

                while i + offset < len(formula) and formula[i + offset].isalpha() and formula[i + offset].islower():
                    atom += formula[i + offset]
                    offset += 1

                # now the (i + offset) is either at a new uppercase letter or an integer or ( or )
                count = ''

                while i + offset < len(formula) and formula[i + offset].isnumeric():
                    count += formula[i + offset]
                    offset += 1

                # now the i is either at a new uppercase letter or ( or )
                # we need to recurse, but first we need to log what we found
                if count == '':
                    # it means the count is 1
                    count = 1
                else:
                    count = int(count)

                # now that we have the atom and the count, we either add it to atomCounts or we push to stack
                if len(stack) == 0:
                    # process directly
                    if atom in atomCounts:
                        atomCounts[atom] += count
                    else:
                        atomCounts[atom] = count
                else:
                    stack.append((atom, count))

                # now we need our index i to move to after the current atom we just processed
                i = i + offset
            else:
                # we are at a ( or )
                if formula[i] == '(':
                    # we need to push into stack
                    stack.append((formula[i], 1))

                    i += 1
                else:
                    # we are at a ) so we need to pop and process
                    multiple = 1

                    if i + 1 < len(formula) and formula[i + 1].isnumeric():
                        count = ''

                        offset = 1

                        while i + offset < len(formula) and formula[i + offset].isnumeric():
                            count += formula[i + offset]

                            offset += 1

                        i = i + offset

                        multiple = int(count)
                    else:
                        # just skip the current )
                        i += 1

                    currentAtomCounts = {}

                    # as we're popping we need to multiply each count by `multiple`
                    # it's safe to do this because we are sure that the first ever character in stack is always a (
                    while stack[-1][0] != '(':
                        atom, count = stack.pop()

                        if atom in currentAtomCounts:
                            currentAtomCounts[atom] += (count * multiple)
                        else:
                            currentAtomCounts[atom] = (count * multiple)

                    # pop the (
                    stack.pop()

                    # when we reach this point either: stack is empty OR the top character is (
                    if len(stack) == 0:
                        # we process the atoms we just seen => add them to atomCounts
                        for atom in currentAtomCounts:
                            if atom in atomCounts:
                                atomCounts[atom] += currentAtomCounts[atom]
                            else:
                                atomCounts[atom] = currentAtomCounts[atom]
                    else:
                        # we push back the counts into stack and continue processing
                        for atom in currentAtomCounts:
                            stack.append((atom, currentAtomCounts[atom]))

    def countOfAtoms(self, formula: str) -> str:
        # this will map every atom to its count
        atomCounts = {}

        # this function will fill atomCounts
        self.countOfAtomsHelper(formula, atomCounts)

        atoms = sorted(atomCounts.keys())

        # now we build the final string where each element is followed by its count
        atomCountsResult = ''

        for atom in atoms:
            atomCount = atomCounts[atom]

            if atomCount > 1:
                atomCountsResult += atom + str(atomCount)
            else:
                atomCountsResult += atom

        return atomCountsResult


# print(Solution().countOfAtoms('H2O'))
print(Solution().countOfAtoms('K4(ON(SO3)2Mg(OH)3Ca)2'))
# print(Solution().countOfAtoms('K4(ON(SO3)Mg(OH)3Ca)2'))
# print(Solution().countOfAtoms('(K4(ON(SO3)2Mg(OH)3Ca)2)'))
