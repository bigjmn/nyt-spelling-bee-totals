def check_hive(hive):
    #check hive is letters
    if hive.isalpha() == False:
        return False
    #check hive is 7 letters long
    if len(hive) != 7:
        return False
    #check hive has no repeat letters
    letters = set(hive)
    if len(letters) != 7:
        return False
    return True
