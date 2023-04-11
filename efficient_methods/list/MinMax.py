class MinMax:
    """
        Solving the problem involves
            To find out the min or max from a list of element
            To find out min or max from the sublist of list
            Min or max can be based on any condition
    """

    def findMinMax(self, a, n):
        # Method 1
        # a.sort()
        # return [a[0], a[-1]]

        # Method 2
        min_, max_ = a[0], a[0]
        for elem in a:
            if elem < min_:
                min_ = elem
            elif elem > max_:
                max_ = elem

        return [min_, max_]

    # Largest Product
    # Largest product that can be obtain by multiplying the subset of continuous m numbers
    def largestProd(self, arr, n, m):
        """
        Approach:
            1. access each element by index
            2. While accessing, multiply number with its previous
            3. multiple k number till it is less then k
            4. once it become k now we need to
                a. multiply the coming number
                b. divide the (index+1 - k) number so that the number will contain the product of k element
                    1. Example suppose k = 4
                    2. When index is 4, we need to compare for max_product and need to divide product from
                       index 0 to multiply 4th number on product.
                    3. When index is 5, we need to compare for max_product and need to divide product from
                       index 1 to multiply 4th number on product.
                    4. When index is 6, we need to compare for max_product and need to divide product from
                       index 2 to multiply 4th number on product.
                    5. When index is 7, we need to compare for max_product and need to divide product from
                       index 3 to multiply 4th number on product.
        :param arr: List of int
        :param n: length of arr
        :param m: no of element for which we need to find max product
        :return: max product of continues sub list
        """
        prod = 1
        max_prod = 1
        for index in range(n):
            prod *= arr[index]
            if index + 1 >= m:
                max_prod = prod if prod > max_prod else max_prod
                prod = prod // arr[index + 1 - m]
        return max_prod

    def kSmallest(self, arr, n, k):
        """
        Approach:
            1. Sort the array
            2. Return first k elements
        :param arr: list of int
        :param n: length of arr
        :param k: no of shortest elements
        :return: list of k shortest elements
        """
        arr.sort()
        return arr[:k]
