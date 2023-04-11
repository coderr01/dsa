class Modify:
    """
        Solving the problem involves
            rotation (left and/or right Or clockwise and/or anti-clockwise)
            modification, replacement
            rearranging the elements
    """

    # Clockwise rotation of aray
    def rotate(self, arr, n, rotate=1):
        """
        :param arr: list of elements (elementy of type int)
        :param n: length of arr
        :param rotate: no of times right we need to do shift occur
        :return: right shifted array
        """
        rotate = rotate % n
        arr[rotate:], arr[:rotate] = arr[:n - rotate], arr[n - rotate:]

    # Sorting Records
    def sortData(self, arr, n):
        """
        :param arr: list of component
                component - contain list of length 2 (Example: [Ram, 50])
        :param n: length of arr
        :return: sorted arr
        """
        arr.sort(key=lambda component: component[1])
        return arr

        # Replace all 0's with 5

    # Replace all 0's with 5
    def replaceAll(self, n, x="5"):
        """
        :param n: number of type int
        :param x: number we need to replace with zero
        :return: number in which 0 are replaced by x
        """
        return int(str(n).replace("0", x))
