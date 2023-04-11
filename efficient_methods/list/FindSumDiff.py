class SumDiff:
    """
        Solving the problem involves
            sum or diff of m numbers based on condition
            sum of diff of m numbers equal to any number
    """
    def __init__(self):
        pass

    # Friendly Array
    def friendliness(self, arr, n):
        """
        friendliness: lowest the diff to its adjacent neighbours (in right and left) more friendly
        Approach:
            1. Sort the array as the sorted list will have the lowest diff in between adjacent
            2. Find out the lowest diff in between its right and left adjacent and add it to friendliness
            3. Because element at index 0 has no left element so we need to calculate it's diff
                from the index 1 element and add it to friendliness.
            4. Because element at index n-1 has no right element so we need to calculate it's diff
                from the index n-2 element and add it to friendliness.
        :param arr: list of element (element type is int)
        :param n: length of arr
        :return: total sum of friendliness
        """
        arr.sort()
        friendliness = 0
        for index in range(1, n - 1):
            one = abs(arr[index] - arr[index + 1])
            two = abs(arr[index] - arr[index - 1])
            friendliness += min(one, two)
        friendliness += abs(arr[-1] - arr[-2])
        friendliness += abs(arr[1] - arr[0])
        return friendliness

