from wordfinder import words_by_length

def show_wordlist(hivedict):
    message = ''
    for i in hivedict.values():
        for words in i:
            message += words+', '
    return message



def get_total_words(hivedict):
    totalwords = 0
    for i in hivedict.values():
        totalwords += len(i)
    message = 'there are at MOST '+str(totalwords)+' total words'+"\n"

    return message

def get_wordcount_by_length(hivedict):
    message = 'maximum total words by letter count: \n'
    for i in hivedict:
        wordcount = len(hivedict[i])
        message += str(i)+' letter words: '+str(wordcount)+'\n'
    return message

def compile_data(hive):
    hivedict = words_by_length(hive)
    keyword2message = {}
    keyword2message['total words'] = get_total_words(hivedict)
    keyword2message['word lengths'] = get_wordcount_by_length(hivedict)
    keyword2message['show all'] = show_wordlist(hivedict)
    return keyword2message
