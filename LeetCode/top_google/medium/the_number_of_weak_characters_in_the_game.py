'''
    https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

    1996. The Number of Weak Characters in the Game

    You are playing a game that contains multiple characters, and each of the characters has two main properties:
    attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents
    the properties of the ith character in the game.

    A character is said to be weak if any other character has both attack and defense levels strictly greater than this
    character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j
    where attackj > attacki and defensej > defensei.

    Return the number of weak characters.
'''

'''
    Correct but time limit exceeded as expected
'''


class Solution:
    def numberOfWeakCharacters(self, properties: [[int]]) -> int:
        count_weak = 0

        # More formally, a character i is said to be weak if there exists another character j
        # where attack of j > attack of i and defense of j > defense of i

        for i in range(0, len(properties)):
            attack_i = properties[i][0]
            defense_i = properties[i][1]

            for j in range(0, len(properties)):
                if i != j:
                    attack_j = properties[j][0]
                    defense_j = properties[j][1]

                    if attack_i < attack_j and defense_i < defense_j:
                        count_weak += 1

                        # we found at least one other character that i is weak against so we're done
                        break

        return count_weak


'''
    Motivation: 
    - we don't need to compare characters that have equal attack or equal defense because for sure not one is stronger than the other
    - when comparing a character to another, we only need to compare it against those with highest attack and inside those higher defense
    
    Correct but TLE.
'''


class Solution2:
    def numberOfWeakCharacters(self, properties: [[int]]) -> int:
        # sort in ascending order first by attack asc then by defense desc
        properties.sort(key=lambda item: (item[0], - item[1]))

        current_attack_group = None
        attack_groups = {}

        # now we need to go through the list and group characters by their attach values
        for i in range(0, len(properties)):
            character_attack = properties[i][0]

            if current_attack_group is None:
                current_attack_group = character_attack

                # start a new group
                attack_groups[current_attack_group] = [i]
            elif current_attack_group != character_attack:
                # we need to end the previous group
                attack_groups[current_attack_group].append(i - 1)

                # start a new group
                current_attack_group = character_attack
                attack_groups[current_attack_group] = [i]
            # else:
            # current_attack_group == character_attack
            # we are in the same group still

        # when the loop is done, we need to add the end index of the last attack group
        attack_groups[current_attack_group].append(len(properties) - 1)

        # this should allow us to know which group is the "next" group
        attack_groups_keys = list(attack_groups.keys())
        current_attack_group_index = 0

        weak_count = 0

        '''
            Observation: if a character is found weak in a group, it means that all the subsequent characters in its group
            are also weak because the same character that is stronger than the weak character we just found will be also stronger
            than the remaining characters in the group.
        '''

        current_character_index = 0

        while current_character_index < len(properties):
            character = properties[current_character_index]

            character_attack = character[0]
            character_defense = character[1]

            # from the character_attack we can know what is the next group
            if character_attack != attack_groups_keys[current_attack_group_index]:
                # we are done with a group and we need to move on to the next
                current_attack_group_index += 1
            # else we are still in the same group so we don't need to make any changes to the current group

            if current_attack_group_index == len(properties) - 1:
                # we are in the last attack group and it's the strongest one so no character is stronger than any of its characters
                break

            # this character, we need to compare its defense to all the subsequent characters from next group onwards
            # in each group, as soon as we see a defense < character_defense, we skip group because they are sorted in desc order of defense
            next_group_index = current_attack_group_index + 1
            is_current_character_weak = False

            while next_group_index < len(attack_groups_keys) and not is_current_character_weak:
                next_group_start, next_group_end = attack_groups[attack_groups_keys[next_group_index]]

                for j in range(next_group_start, next_group_end + 1):
                    if properties[j][1] > character_defense:
                        # the current character is weak
                        is_current_character_weak = True

                        # the current character and all subsequent characters in same group are weak
                        weak_count += (attack_groups[character_attack][1] - current_character_index) + 1

                        # the next character should be the first character in next group
                        current_character_index = attack_groups[character_attack][1] + 1

                        break
                    elif properties[j][1] <= character_defense:
                        # we need to skip this group because the subsequent characters have defense <= to our character
                        next_group_index += 1

                        break

            # we checked all the groups for this character, if it's not weak then we should simply proceed to next character
            # otherwise, if it's weak then the character_index would be updated in the loop already
            if not is_current_character_weak:
                current_character_index += 1

        return weak_count


'''
    Key observation: when we're checking if a character is weak, we only need to check if there's a defense value higher than it among all 
    subsequent groups. Groups are just characters grouped together by their equal attack values.
    
    - map each attack value to a group (implicit)
    - map each attack group to its highest defense value (easy to do since highest defense after sorting will be first character in group)
    - create accumulate structure to answer question: what is highest defense value after group x?
'''
from collections import OrderedDict

'''
    Accepted
'''


class Solution3:
    def numberOfWeakCharacters(self, properties: [[int]]) -> int:
        properties.sort(key=lambda item: (item[0], - item[1]))

        # map each attack group to its highest defense value (easy to do since highest
        # defense after sorting will be first character in group)
        highest_defense_in_group = OrderedDict()

        i = 0

        while i < len(properties):
            current_attack_value = properties[i][0]

            # the first element in group has the highest defense
            highest_defense_in_group[current_attack_value] = properties[i][1]

            # skipping the entire group
            while i < len(properties) and properties[i][0] == current_attack_value:
                i += 1

        # now we go through the list of highest defense per group and create the accumulate structure
        acc_highest_defense_in_group = {}

        group_keys = list(highest_defense_in_group.keys())

        # for the last group we don't need to calculate the acc because it's the same as the group's highest defense itself
        acc_highest_defense_in_group[group_keys[len(group_keys) - 1]] = highest_defense_in_group[group_keys[len(group_keys) - 1]]

        for j in range(len(group_keys) - 2, -1, -1):
            acc_highest_defense_in_group[group_keys[j]] = max(highest_defense_in_group[group_keys[j]], acc_highest_defense_in_group[group_keys[j + 1]])

        # count to keep track of weakest while we're processing the characters
        weakest_count = 0

        # now, for every character in a group, we just need to check if there's a higher defense in groups after it
        # note: we know that the order of the characters in properties is same order as group_keys in terms of attack values
        current_group_index = 0  # in group_keys

        for character in properties:
            character_attack, character_defense = character[0], character[1]

            # check if the current_group_index is up-to-date
            if character_attack != group_keys[current_group_index]:
                current_group_index += 1

            # check if we are in last group so we can skip it because the characters in last group are strongest
            if current_group_index == len(group_keys) - 1:
                break

            # are safe to continue
            # current_group_index is group of current character, so we need to get the next group onwards to see their highest defense
            # it's safe to do current_group_index + 1 because we know we'll never be in last group doing this
            highest_defense_in_next_groups = acc_highest_defense_in_group[group_keys[current_group_index + 1]]

            if highest_defense_in_next_groups > character_defense:
                weakest_count += 1

        return weakest_count


# print(Solution2().numberOfWeakCharacters(properties=[[5, 5], [6, 3], [3, 6]]))
# print(Solution2().numberOfWeakCharacters(properties=[[2, 2], [3, 3]]))
print(Solution3().numberOfWeakCharacters(properties=[[1, 5], [10, 4], [4, 2], [10, 4], [4, 3]]))
