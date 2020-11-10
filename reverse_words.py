"""Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
    >>> reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ])
    steal pound cake
"""


def reverse_words(message):
    for i in range(len(message) // 2):
        message[i], message[-1-i] = message[-1-i], message[i]

    def helper(idx_start, idx_end):
        for i in range((idx_end-idx_start)//2):
            message[idx_start+i], message[idx_end -
                                          i] = message[idx_end-i], message[idx_start+i]

    print(''.join(message))

    word_idxs = []
    start = 0
    for i, char in enumerate(message):
        if char == ' ':
            word_idxs.append((start, i-1))
            start = i+1
        elif i == len(message)-1:
            word_idxs.append((start, i))

    for word_start, word_end in word_idxs:
        print(word_start, word_end)
        helper(word_start, word_end)

    print(''.join(message))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n **PASSED** \n')
