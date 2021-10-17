def check_word(word, hive):
    hive = hive.upper()
    key_letter = hive[0]
    if len(word) <= 3:
        return False
    word = set(word)
    hive = set(hive)
    if key_letter not in word:
        return False
    if word.issubset(set(hive)) == False:
        return False
    return True

def words_by_length(hive):
    word_dict = {}
    with open('dictionary.txt', 'r') as newdictionary:
        for word in newdictionary.readlines():

            #get rid of newline spaces and such
            word = word.strip()

            if check_word(word, hive) == True:
                word_length = len(word)
                if word_length not in word_dict:
                    word_dict[word_length] = []
                word_dict[word_length].append(word)
    return word_dict
