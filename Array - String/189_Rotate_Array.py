def swap_ends_inplace(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
    print(f"After swapping: {arr}")

my_list = [10,20,30,40]
swap_ends_inplace(my_list)

another_list = [5]
swap_ends_inplace(another_list)