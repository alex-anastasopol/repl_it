def highest_even(li):
    highest = li[0]
    for i in li:
        if i % 2 == 0 and i > highest:
            highest = i
    return highest


print(highest_even([10, 2, 3, 4, 8, 11]))
