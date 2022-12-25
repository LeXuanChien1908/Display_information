def Find_Max(arr):
    """
    :param arr: list of integer
    :return: item max of list
    """
    max = arr[0]

    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]

    return max


def Find_Min(arr):
    """
    :param arr: list of integer
    :return: item min of list
    """
    min = arr[0]

    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]

    return min


def Enter_List(n):
    """
    :param n: number of item' list
    :return: list
    """
    a = []
    for i in range(n):
        print("\tPhan tu thu", i+1, "la:", end=" ")
        a.append(int(input()))

    return a


def Show_List(arr):
    """
    :param arr: list
    :return: void
    """
    for i in arr:
        print("\t", i, end="")


# Chuong trinh chinh
n = int(input("Nhap vao so luong phan tu: n = "))
print("Nhap vao mang:")
arr = Enter_List(n)

print("Mang vua nhap la:")
Show_List(arr)

print("\nPhan tu lon nhat la: ", Find_Max(arr))
print("Phan tu nho nhat la: ", Find_Min(arr))