from compiledata import compile_data
from validhive import check_hive

def input_hive():
    error_message = "Not a valid hive. Make sure that it's 7 distinct letters (with no commmas, spaces, etc.)"
    hive = input('Hive: ')
    if hive == 'quit':

        return 'quit'
    if check_hive(hive) == False:
        print(error_message)
        return input_hive()
    return compile_data(hive)

def input_query(data):
    error_message = "invalid query. Search 'total words', 'word lengths', or 'show all, or enter 'quit' to exit."
    query = input('Enter keyword: ')
    if query == 'quit':
        return query
    if query not in data:
        print(error_message)
        return input_query(data)
    response = data[query]
    print(response)
    print('make another search, or enter "quit" to exit.')
    return input_query(data)







def hivequeries():
    intro_message = "enter letters of hive with no spaces. put the required letter (hive center) first"
    error_message = "Not a valid hive. Make sure that it's 7 distinct letters (with no commmas, spaces, etc.)"

    hivedata = input_hive()
    if hivedata == 'quit':
        return
    while check_hive(hive) == False:
        print(error_message)
        hive = input('Hive: ')

    responses = compile_data(hive)
    query = input('enter keyword: ')
    while query not in responses:
        query = input('enter keyword: ')
    response = responses[query]
    print(response)
