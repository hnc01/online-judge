'''
    https://leetcode.com/problems/partition-labels/

    763. Partition Labels

    You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

    Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

    Return a list of integers representing the size of these parts.
'''

'''
    Accepted
'''


class Solution:
    def is_overlap(self, s1, e1, s2, e2):
        if s1 > s2:
            # we need s1 to me the smaller one
            s1, s2 = s2, s1
            e1, e2 = e2, e1

        # now we know that (s1, e1) starts before (s2, e2)
        return e1 >= s2

    def partitionLabels(self, s: str) -> [int]:
        # list of tuples (s1,e1) that mark the start and end indexes of a group
        parts = []

        # list of sets and each set will contain the letters belonging to a part
        # the letters in parts[i] is at groups[i]
        groups = []

        for i in range(0, len(s)):
            character = s[i]

            # find the group that 'character' belongs to
            group_found = False

            for g in range(0, len(groups)):
                if character in groups[g]:
                    # we need to expand the end_index of parts[i] to include the current index
                    (s1, e1) = parts[g]
                    parts[g] = (s1, i)

                    group_found = True

                    # now we need to merge all the groups whose index ranges overlap with group[g]
                    parts_to_merge = []
                    parts_to_merge.append(g)

                    # start_index will always be that of parts[g][0]
                    start_index = parts[g][0]
                    # the end_index will be max out of all parts
                    end_index = parts[g][1]

                    merged_group = set()
                    merged_group.update(groups[g])

                    for p in range(0, len(parts)):
                        if p != g:
                            if self.is_overlap(parts[p][0], parts[p][1], parts[g][0], parts[g][1]):
                                merged_group.update(groups[p])
                                parts_to_merge.append(p)
                                end_index = int(max(end_index, parts[p][1]))

                    new_parts = []
                    new_groups = []

                    # the new range is [start_index, end_index]
                    for p in range(0, len(parts)):
                        if p not in parts_to_merge:
                            new_groups.append(groups[p])
                            new_parts.append(parts[p])
                        elif p == g:
                            new_parts.append((start_index, end_index))
                            new_groups.append(merged_group)

                    groups = new_groups
                    parts = new_parts

                    break

            if not group_found:
                # it means we found a new character
                new_group = set()
                new_group.add(character)
                groups.append(new_group)

                parts.append((i, i))

        answer = []

        for (start_index, end_index) in parts:
            answer.append(end_index - start_index + 1)

        return answer


s = "ababcbacadefegdehijhklij"
# s = "eccbbbbdec"

print(Solution().partitionLabels(s))
