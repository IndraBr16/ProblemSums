import re


class PalindromeSolution(object):
    """
    A class focused on solving palindrome problem sums
    """


    def customValidatePalindrome(self, string):
        """
        Function takes in a string and checks if it can be a palindrome. If it is a sentence, remove the whitespaces
        and punctuation.
        :return:
        """
        cleansedString = re.sub('\W+','', string.lower())
        print("Transform string into: " +  cleansedString)
        print("Total no. of characters: " + str(len(cleansedString)))
        print()

        # If number of characters in string is even, split characters into 2 sub lists and compare them after
        # reversing one of them.
        subList = []
        subListToReverse = []
        if (len(cleansedString) % 2) == 0:
            subList = []
            subListToReverse = []

            # Range to use based on length of string of characters
            halfNumOfChar = int(len(cleansedString) / 2)

            # Append the first half of characters into subList.
            for i in range(halfNumOfChar):
                subList.append(cleansedString[i])
            # print("Sub List 1: " + str(subList))

            # Tranform the string of characters to only have the second half
            secondHalfString = cleansedString[(halfNumOfChar):]

            # Append the second half of characters into subListToReverse.
            for i in range(halfNumOfChar):
                subListToReverse.append(secondHalfString[i])
            subListToReverse.reverse()
            # print("Sub List 2: " + str(subListToReverse))

            # If both sublists are the same in terms of list of characters and its order, return True.
            if subList == subListToReverse:
                return "String of characters is a Palindrome :)"

            # Else, reverse the entire string.
            else:
                nonPalindromeString = list(cleansedString)
                nonPalindromeString.reverse()
                finalOutput = ''.join(nonPalindromeString)
                return "Reverse of Non-Palindrome String: " + finalOutput

        else:
            # Range to use based on length of string of characters
            halfNumOfChar = int((len(cleansedString) - 1) / 2)

            for i in range(halfNumOfChar):
                subList.append(cleansedString[i])
            # print("Sub List 1: " + str(subList))

            # Tranform the string of characters to only have the second half
            secondHalfString = cleansedString[(halfNumOfChar+1):]

            # Append the second half of characters into subListToReverse.
            for i in range(halfNumOfChar):
                subListToReverse.append(secondHalfString[i])
            subListToReverse.reverse()
            # print("Sub List 2: " + str(subListToReverse))

            # If both sublists are the same in terms of list of characters and its order, return True.
            if subList == subListToReverse:
                return "String of characters is a Palindrome :)"

            # Else, reverse the entire string.
            else:
                nonPalindromeString = list(cleansedString)
                nonPalindromeString.reverse()
                finalOutput = ''.join(nonPalindromeString)
                return "Reverse of Non-Palindrome String: " + finalOutput


if __name__ == '__main__':
    solution = PalindromeSolution()
    print("Testing Palindrome Solution:")
    print(solution.customValidatePalindrome("Murder for a jar of red rum"))
