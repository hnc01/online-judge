'''
    https://leetcode.com/problems/longest-absolute-file-path/

    388. Longest Absolute File Path

    Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:

    Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext
    and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.

    In text form, it looks like this (with ⟶ representing the tab character):
    dir
    ⟶ subdir1
    ⟶ ⟶ file1.ext
    ⟶ ⟶ subsubdir1
    ⟶ subdir2
    ⟶ ⟶ subsubdir2
    ⟶ ⟶ ⟶ file2.ext

    If we were to write this representation in code, it will look like this:
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". Note that the '\n' and '\t' are the new-line
    and tab characters.

    Every file and directory has a unique absolute path in the file system, which is the order of directories that must be opened to reach
    the file/directory itself, all concatenated by '/'s. Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext".
    Each directory name consists of letters, digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of
    letters, digits, and/or spaces.

    Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted
    file system. If there is no file in the system, return 0.
'''

'''
    Accepted
'''


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # each time we read from the input, we need to look for the pattern
        # (\n(\t)+)* => the presence of no \n means we're at level 0
        # if we see \n, then the number of \t tells us which level we're at
        # first let's split input by \n so that we can have \t as the only symbol
        # to use to know on which level we are
        if len(input) == 0:
            return 0

        max_length = 0

        # we're sure we have at least one character in input
        input = input.split("\n")

        # we will use this to keep track of the path while going through the input
        stack = []

        # now we go through input element by element and we use \t to know the level
        for el in input:
            # first let's check if el contains any tabs
            level = el.count("\t")

            # we remove the tabs from the element
            el = el.replace('\t', '')

            # we try to push the current element in the stack
            while len(stack) > 0 and stack[len(stack) - 1][1] >= level:
                top_element, top_element_level = stack.pop()

                # if top_element is a file, then we evaluate the length of absolute path and move on
                if '.' in top_element:
                    # then it's a file
                    # the absolute path of this file is all the elements in the stack
                    if len(stack) > 0:
                        file_path = '/'.join([x[0] for x in stack]) + '/' + top_element
                    else:
                        file_path = top_element

                    max_length = max(len(file_path), max_length)

            # we are done with popping the current path branch from the stack
            # we push the current element to start a new one
            stack.append((el, level))

        # when we are done with the above, there might still be elements in the stack that could lead to a valid
        # absolute path so we need to cater for these
        if len(stack) > 0:
            top_element, top_element_level = stack.pop()

            # if top_element is a file, then we evaluate the length of absolute path and move on
            if '.' in top_element:
                # then it's a file
                # the absolute path of this file is all the elements in the stack
                if len(stack) > 0:
                    file_path = '/'.join([x[0] for x in stack]) + '/' + top_element
                else:
                    file_path = top_element

                max_length = max(len(file_path), max_length)

        return max_length


# input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# input = "a"
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# input = "file1.txt\nfile2.txt\nlongfile.txt"

print(Solution().lengthLongestPath(input))
