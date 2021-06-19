# Total 26 albhabets
MAX = 26

def palindrome_permutations(string):
    string_len = len(string)
    freq_list = [0] * MAX
    
    # Frequency list
    for i in string:
        if i != ' ':
            freq_list[ord(i)-ord('a')] += 1
    
    # Find odd letter/char in the array
    # If odd letter/char is more than one then return False
    odd_char_count = 0
    for i in freq_list:
        if i % 2 != 0:
            odd_char_count += 1
    return odd_char_count <= 1

if __name__ == '__main__':
    string = 'race car'
    res = palindrome_permutations(string)
    print(res)
