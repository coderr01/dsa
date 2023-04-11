# Check if element Satisfy certain condition
class Validate:
    """
        Solving the problem involves
            Validating the list of element for certain condition
            Validating any element based on certain condition
    """

    def __init__(self):
        pass

    # Power of 2
    def isPowerOfTwo(self, n):
        """
        Approach
            binary representation of the number should contain only 1 occurrence of digit "1"
        :param n: number we need to validate
        :return: True if no is power of two else False
        """
        return bin(n)[2:].count(str(1)) == 1

    # Check Arithmetic Progression
    def isAP(self, arr, n):
        """
        Steps:
            1. Sort the element
            2. check if difference in between element is fixed, if yes then it's AP
        :param arr: List of int
        :param n: length of arr
        :return: True if list can be formed with Arithmatic progression
        """
        arr.sort()
        diff = arr[1] - arr[0]
        for index in range(n - 1):
            if diff != arr[index + 1] - arr[index]:
                return False
        return True
