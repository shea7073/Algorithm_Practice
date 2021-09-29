# find largest continuous sum

def cont_sum(arr):
    max = 0
    current_total = 0
    start = 0
    end = 0
    index = -1
    for num in arr:
        current_total = num
        index += 1
        count = 1
        try:
            for i in range(index + count, len(arr)):
                current_total += arr[index + count]
                if current_total > max:
                    max = current_total
                    start = num
                    end = arr[index + count]
                count += 1
        except IndexError:
            pass
    print(max, start, end)


cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])
