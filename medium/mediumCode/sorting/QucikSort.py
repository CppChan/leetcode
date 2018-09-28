class QuicksSort(object):
    def quickSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        start = 0
        end = len(array) - 1
        key = array[0]
        result = self.swap(array, start, end)
        return result

    def swap(self, array, low, high):
        start = low
        end = high
        key = array[start]
        while (start < end):
            while (key <= array[end] and start < end):
                end = end - 1
            if (key > array[end]):
                temp = array[end]
                array[end] = key
                array[start] = temp
            while (key >= array[start] and start < end):
                start = start + 1
            if (key < array[start]):
                temp = array[start]
                array[start] = key
                array[end] = temp
        if (start == end and start > low):
            self.swap(array, low, start)
        if (start == end and start < high):
            self.swap(array, start + 1, high)
