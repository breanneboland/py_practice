message = 'find you will pain only go you recordings security the into if'

def reverse_words_not_in_place(str):
    word_list = str.rsplit(" ")
    word_list.reverse()
    reversed_string = " ".join(word_list)
    print(reversed_string)

# reverse_words_not_in_place(message)

def reverse_words_in_place(str):
    word_list = str.rsplit(" ")
    half_list_len = int(len(word_list) / 2)

    for front_index in range(half_list_len):
        back_index = -front_index - 1

        word_list[front_index], word_list[back_index] =\
            word_list[back_index], word_list[front_index]

    print(" ".join(word_list))

reverse_words_in_place(message)
# returns: 'if into the security recordings you go only pain will you find'
