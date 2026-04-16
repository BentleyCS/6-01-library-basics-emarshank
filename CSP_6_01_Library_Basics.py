#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)
import analytics as an

# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    for index in range(len(rawPrices)):
        rawPrices[index] = an.apply_markup(rawPrices[index], 15)
    return rawPrices
    


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    return an.get_highest(n), an.get_average(n)

# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(cleanlist):
    return (an.clean_text(cleanlist))

# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(arg):
    return an.filter_threshold(arg, 100)

# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case worsd with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items, target):
    items = an.clean_text(items)
    sorted = True
    for index in range(1, len(items)):
        if items[index-1] > items[index]:
            sorted = False
        else:
            pass
    if sorted == True:
        low = 0
        high = len(items)-1
        while high >= low:
            mid = int((low + high) / 2)
            if items[mid] == target:
                return mid
            if items[mid] > target:
                high = mid-1
            if items[mid] < target:
                low = mid+1
        return -1
    else:
        for index in range(0, len(items)):
            if items[index] == target:
                return index
        return -1
