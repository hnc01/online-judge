class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_brackets = ["(", "{", "["]
        closed_brackets_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for character in s:
            if character in open_brackets:
                stack.insert(0, character)
            else:
                if len(stack) > 0:
                    latest_open_bracket = stack.pop(0)

                    if closed_brackets_map[latest_open_bracket] != character:
                        return False
                else:
                    return False

        return len(stack) == 0