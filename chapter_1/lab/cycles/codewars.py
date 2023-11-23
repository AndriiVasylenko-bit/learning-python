# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    if arr is not None:
        lst = list()
        b = True
        for i in range(len(arr)):
            if arr[i] < 0 and b:
                lst.append(i-1)
                b = False