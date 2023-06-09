def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left_half = merge_sort(s[:mid])
    right_half = merge_sort(s[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    if left:
        merged.extend(left[left_index:])
    if right:
        merged.extend(right[right_index:])

    return merged


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return "", "", False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_sorted = "".join(merge_sort(list(first_string)))
    second_sorted = "".join(merge_sort(list(second_string)))

    if first_string == "" or second_string == "":
        return first_sorted, second_sorted, False

    return first_sorted, second_sorted, first_sorted == second_sorted
    raise NotImplementedError
