class Search:
    """
        Solving the problem involves
            Search the element based on condition
            Count or replace the elements based on condition
    """
    def search(self, arr, N, X):
        """
        :param arr: list of element (element type : int)
        :param N: length of arr
        :param X: element we need to find
        :return: True if X in the arr else False
        """
        for elem in arr:
            if elem == X:
                return True
        return False

    # Number of occurrence
    def count(self, arr, n, x):
        """
        :param arr: list of element (element type : int)
        :param n: length of arr
        :param x: element whose occurrence needed to be found
        :return: No of occurrence of x in arr
        """
        return arr.count(x)

    # Find Number of Numbers
    def findDigitCount(self, arr, n, k):
        """
        :param arr: list of element (element type : int)
        :param n: length of arr
        :param k: element whose occurrence needed to be found
        :return: total number of occurrence of k in numbers of list
        """
        count = 0
        k = str(k)
        for elem in arr:
            count += str(elem).count(k)
        return count

    # Swap and Maximize
    def maxSum(self, arr, n):
        """
        We need to find the maxima of total diff in between the numbers
        Approach
            1. diff will be maximum if highest number is subtracted from lowest
            2. diff will be maximum if second highest number is subtracted from second lowest ....
            3. for that we need to sort the array in ascending order
            4. after that element at 0 index should be subtracted from index at -1
            5. after that element at 1 index should be subtracted from index at -2 ... And So on
            6. Because we are processing the two element at single index so loop need to run from 0 to n // 2
        :param arr: list of element (element of type int)
        :param n: length of arr
        :return:
        """
        arr.sort()
        sum_ = 0
        for index in range(n // 2):
            sum_ += abs(arr[index] - arr[-index - 1])
        return sum_

    # Segregate Even and Odd numbers
    def segegateEvenOdd(self, arr, n):
        """
        :param arr: list of elements (elements of type int)
        :param n: length of arr
        :return: segregate the list of sorted even elements first and then list of sorted odd elements
        """
        odd, even = [], []
        for elem in arr:
            even.append(elem) if elem % 2 == 0 else odd.append(elem)
        even.sort()
        odd.sort()
        return even + odd

    # Type of array
    def maxNtype(self, arr, n):
        """
        :param arr: list of int
        :param n: length of arr
        :return:
            1. if array is Ascending
            2. if array is Descending
            3. if array is Descending Rotated (Example : [3, 2, 6, 5, 4])
            4. if array is Ascending Rotated (Example : [ 2, 3, 4, 0, 1])
        """
        # code here.
        max_num = max(arr)
        ind = arr.index(max_num)
        if 0 < ind < n - 1:
            return [3, max_num] if arr[ind - 1] < arr[ind + 1] else [4, max_num]
        elif ind == 0:
            return [2, max_num] if arr[1] > arr[-1] else [4, max_num]
        else:
            return [1, max_num] if arr[1] > arr[0] else [3, max_num]

    # Repeated IDs
    def uniqueId(self, arr):
        """
        Remove redundant element without changing the sequence
        :param arr: list with redundant element
        :return: list of unique element
        """
        unique = []
        dict_ = {}
        for elem in arr:
            dict_.update({elem:dict_.get(elem, 0)+1})
            unique.append(elem) if dict_[elem] < 2 else None
        return unique
