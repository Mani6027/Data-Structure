def urlify(string):
    string_original_len = len(string)
    space_count = string.count(' ')
    # we need to allocate two more spaces for each space.
    index = string_original_len + space_count * 2
    string = ['0' if i > string_original_len - 1 else string[i] for i in range(index)]
    j = string_original_len - 1
    index = index - 1
    while j > 0:
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index -= 3
        else:
            string[index] = string[j]
            index -= 1
        j -= 1
    return ''.join(string)


if __name__ == '__main__':
    string = 'mani kandan s'
    res = urlify(string)
