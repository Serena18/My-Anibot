import csv

def read_csv():
    # Open the file given so we can read what's inside
    with open(FILE_NAME) as reader_file:
        # Read the file
        reader = csv.reader(reader_file)
        # Make it a list type, so it's easier for us to manage the data
        data = list(reader)
    # The first row of the data has the header
    # The rest of the data are records and will be stored in the database
    return (data[0], data[1:])


FILE_NAME = "Showtimes.csv"
    
def genre_split():
    with open("Showtimes.csv") as csv_file: # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (genre)
        csv_reader = csv.reader(csv_file, delimiter=',') # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (genre)
        genre_split = [] # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (genre)
        for lines in csv_reader: # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (genre)
            y = lines[4].split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
            genre_split.append(y)
    
def title_split():
    with open("Showtimes.csv") as csv_file: # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (title)
        csv_reader = csv.reader(csv_file, delimiter=',') # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (title)
        title_split = [] # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (title)
        for lines in csv_reader: # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values (title)
            z = lines[0].split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
            title_split.append(z)    

def genre_dictionary (title_split,genre_split): 
    with open("Showtimes.csv") as csv_file: # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values for dictionary
        csv_reader = csv.reader(csv_file, delimiter=',') # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values for dictionary
        genre_split = [] # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values for dictionary
        title_split = [] # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values for dictionary
        for lines in csv_reader: # https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html - Printing specific columns: Used to return the specific column values for dictionary
            y = lines[4].split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
            genre_split.append(y)
            z = lines[0].split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
            title_split.append(z)           
    genre_dictionary = {}
    for item in genre_split:
        num = genre_split.index(item)
        genre_dictionary[title_split[num][0]]=genre_split[num]
    return (genre_dictionary)

def compare (genre_dictionary, request_title, list_anime):
    genre_title = genre_dictionary.get(request_title)
    genre_request_title = genre_dictionary.get(list_anime)
    counter = 0
    genre_list = []
    for item in genre_title:
        for obj in genre_request_title:
            if item == obj: 
                counter +=1
    p = [request_title, list_anime, counter]
    genre_list.append(p)
    return p 

def sort(alist): #called bubble sort https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
    new_list = alist[:] # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php - create an identical list using spice, 
    for passnum in range(len(new_list)-1,0,-1): # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php - going from the back, decreasing by index of 1 each time, comparing index value
        for i in range(passnum): # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php- for i in range of the number
            if new_list[i][2] < new_list[i+1][2]: # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php - first i references which list, second is taking the value, comparing the value, comparing if it is higher or lower
                temp = new_list[i] # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php - putting the entire list into temporary list
                new_list[i] = new_list[i+1] # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php - shifting the values, the i+1 is how you shift the values (moving list in front of the other) 
                new_list[i+1] = temp # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php - edited list becomes new list 
    return new_list 

def global_list1():
    request_title = input("For what anime?\n")
    database = read_csv()[1]
    valid = False
    for anime_record in database:
        x = str(anime_record[1]).split(", ") # https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
        if (anime_record[0].lower() == request_title.lower() or request_title.lower() in x or request_title in x): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet 
            request_title = anime_record[0]
            valid = True
    if valid == True:
        global_list = []
        dictionary = genre_dictionary (title_split,genre_split)
        for list_anime in dictionary: 
            global_list.append(compare(dictionary, request_title, list_anime))
        return(global_list)
    elif valid == False:
        print("The anime you have entered may not be seasonal, or you have entered the wrong anime, please try again")
        ask_recommendation()
        see_more() 
        

def get_recommendation():
    y = (sort(global_list1()))
    print("Anime Recommendation: " + y[1][1])

def ask_recommendation():
    answer = input("\nWould you like to have a recommendation? ('yes' or 'no') \n")
    if (answer == "yes"):
        get_recommendation()
    elif (answer == "no"):
        print("")
    elif (answer != "yes" or "no"):
        print("Please enter 'yes' or 'no'")
        ask_recommendation()


def valid_search(title):
    database = read_csv()[1]
    valid = False
    for anime_record in database:
        x = str(anime_record[1]).split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
        if(anime_record[0].lower() == title.lower() or title.lower() in x or title in x): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet
            print ("Name of anime: " + anime_record[0])
            valid = True
    if valid == True:
        get_info(title)
    elif valid == False:
        print("The anime you have entered may not be seasonal, or you have entered the wrong anime, please try again")
        begin_program()
    
def get_airing(title):
    database = read_csv()[1]
    for anime_record in database:
        x = str(anime_record[1]).split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
        if (anime_record[0].lower() == title.lower() or title.lower() in x or title in x): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet
            print ("The airing time is " + str(anime_record[2]) + " at " + str(anime_record[3]))
        
def get_genre(title):
    database = read_csv()[1]
    for anime_record in database:
        x = str(anime_record[1]).split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
        if (anime_record[0].lower() == title.lower() or title.lower() in x or title in x): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet
            print ("Genre: " + str(anime_record[4]))

def get_rating(title):
    database = read_csv()[1]
    for anime_record in database:
        x = str(anime_record[1]).split(", ") #https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
        anime_record[5] = float(anime_record[5])
        if (anime_record[0].lower() == title.lower() or title.lower() in x or title in x): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet
            print ("Rating: " + str(anime_record[5]))

def get_studio(title):
    database = read_csv()[1]
    for anime_record in database:
        x = str(anime_record[1]).split(", ") # https://www.w3schools.com/python/ref_string_split.asp - Splitting up the alternative titles that were all written in one cell on the excel sheet
        if (anime_record[0].lower() == title.lower() or title.lower() in x or title in x): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet
            print ("Studio: " + anime_record[6]) 
    
def anime_day(day):
    print()
    database = read_csv()[1]
    for anime_record in database:
        if (anime_record[2].lower() == day.lower()): # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison - Case insensitive string: Took into account the user inputting anime titles in lower or upper case and how that would have affected the comparison to the excel sheet
            print(str(anime_record[0]) + " at " + str(anime_record[3]))


def get_info(title):
    get_airing(title)
    get_genre(title)
    get_rating(title)
    get_studio(title)
    ask_recommendation()
    see_more()
    


def see_more():
    more = input ("\nWould you want to check out more?\n(answer 'more' or 'no thanks' to end program)\n")
    if (more == "more"):
        begin_program()
    elif (more == "no thanks"):
        print("\nThank you for using MY ANIBOT (o^▽^o) \n")
        print("By the way, you can also type 'get_started()' to get more commands to explore with!")
        import sys #https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481 - allowed us cleanly terminate the program when needed
        sys.exit() #https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481 - allowed us cleanly terminate the program when needed      
    elif (more != "more" or "no thanks"):
        print("\nPlease enter 'other animes' or 'no thanks'")
        see_more() 


def get_ranking():
    with open("Showtimes.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        genre_split = []
        for lines in csv_reader:
            y = lines[5]
            genre_split.append(y)
            ranking = []
            for int in genre_split:
                if int not in ranking:
                    ranking.append(int)
        invalid_input = True
        answer = input("\nWould you want it in ascending or descending order?\n(answer 'ascending' or 'descending')\n")
        if (answer == "descending"):
            invalid_input = False
            ranking.sort(reverse = True) # https://www.afternerd.com/blog/python-sort-list/ - Sorting list elements in numerical and alphabetical order: sorting anime from best to worst and vice versa based on rating for get_rating() function
        elif (answer == "ascending"):
            invalid_input = False
            ranking.sort() # https://www.afternerd.com/blog/python-sort-list/ - Sorting list elements in numerical and alphabetical order: sorting anime from best to worst and vice versa based on rating for get_rating() function
        elif (answer != "descending" or "ascending"):
            print("Please answer 'ascending' or 'descending'")
            get_ranking()
    if invalid_input == False:
        for int in ranking:
            database = read_csv()[1]
            for anime_record in database:
                if int in anime_record[5]:
                    print((int) + " - " + str(anime_record[0]))
                    
def season():
    with open("Showtimes.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lista = []
        for lines in csv_reader:
            y = lines[0]
            lista.append(y)
            lista.sort() # https://www.afternerd.com/blog/python-sort-list/ - Sorting list elements in numerical and alphabetical order: Order anime in alphabetical order for the season() function
        print()
        print(*lista[0:-1], sep = "\n") #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/ - priting list elements in new lines to allow for a cleaner display of all seasonal anime


def get_started():
    print(" \nTo get when something is airing: \nget_airing('anime title') \nexample: get_anime_airing('boku no hero academia 4') \n")
    print("Alternative titles and short forms also work! \nexample: get_airing('bnh4') \n")    
    print("To get the genres of an anime: \nget_genre('anime title') \n")
    print("To get an anime's rating: \nget_rating('anime title') \n")
    print("To get anime's studio: \nget_studio('anime title') \n")
    print("For an anime recommendation: \nget_recommendation() \n")
    print("To get the list of anime that air on the same day of the week: \nanime_day('day of the week') \n")
    print("To get the list of all seasonal anime in alphabetical order: \nseason() \n")
    print("To get the seasonal ranking:\nget_ranking() \n")
    print("For customer service, please contact Sakura Igarashi at sakura.igarashi18@gmail.com \n")

def begin_program():
    start = input ("\nWould you want to get all the info of one seasonal anime or explore on your own?\n(answer 'one' or 'own')\n")
    if (start == "one"):
        title = input ("\nEnter an anime: ")
        print()
        valid_search(title)       
    elif (start == "own"):
        print("\nType 'get_started()' to get the list of commands that will \nhelp you with your seasonal anime searching! \n")
        import sys #https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481 - allowed us cleanly terminate the program when needed
        sys.exit() #https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481 - allowed us cleanly terminate the program when needed         
    elif (start != ("one" or "own")):
        print("\nPlease enter either 'one' or 'own'")
        begin_program()   
 
print ("\nHi there, welcome to MY ANIBOT")
print("For customer service, please contact Sakura Igarashi at sakura.igarashi18@gmail.com")
begin_program()
