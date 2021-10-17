from queries import input_hive, input_query
import sys
def main():
    startmessage = "Input the 'hive' as a string. Make sure it's 7 distinct letters (no commas, spaces, etc) and put the center letter at the beginning."
    querymessage = "Enter 'total words' to get the number of total words (at MAXIMUM, NYT has fewer.)"+"\n"+ "Enter 'word lengths' to get the (maximum) number of total words by length."+"\n"+ "Enter 'show all' to see the list of all possible words."+"\n"+"Enter 'quit' to exit. \n "
    print(startmessage)


    hivedata = input_hive()
    if hivedata == 'quit':
        return None
    print(querymessage)

    hiveresponse = input_query(hivedata)
    if hiveresponse == 'quit':
        return None

if __name__ == '__main__':
    sys.exit(main())
