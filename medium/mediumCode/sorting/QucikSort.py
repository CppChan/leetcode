class QuicksSort(object):
    def quicksort(self, input):
        self.helper(input, 0, len(input) - 1)
        return input

    def helper(self, input, start, end):
        temp, begin, last = start, start, end
        while start < end:
            while input[temp] <= input[end] and start < end:
                end -= 1
            if input[temp] > input[end]:
                input[temp], input[end] = input[end], input[temp]
                temp = end
            while input[temp] >= input[start] and start < end:
                start += 1
            if input[temp] < input[start]:
                input[temp], input[start] = input[start], input[temp]
                temp = start
        if begin < temp: self.helper(input, begin, temp)
        if temp < last: self.helper(input, temp + 1, last)
