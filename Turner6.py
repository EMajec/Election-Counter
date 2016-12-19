#Ethan Turner
#November 30 2016
#Proposed Points: 14/15 because all pieces of the project are complete except for multiplier (However it is commented in for review just incase)



#This function reads data in the
#data in the poll file and puts it into a 2D list
#which it then returns.
#The parameter is the name of the file with the poll info.
def get_poll_data(polls_filename):
    polls_file = open(polls_filename,'r')

    #initialize our 2D list to have no rows initially
    poll_info = []

    #the first line is just the names of the columns, so we can read and ignore it
    polls_file.readline()

    #looping through every line in the file
    for line in polls_file:
        line = line.rstrip('\n') #get rid of the newline character
        vals = line.split(',') #split it into a list by the comma - this row should now have 6 items in it, and it can be one of our rows
        poll_info.append(vals) #throw the new row into the 2D list

    return poll_info


#this function should create a 2D list from the csv file
#given by the state_filename parameter
#return the 2D list that you create here
def get_state_data(state_filename): #sets function to open evperstate file
    state_file = open(state_filename,'r') #open file
    state_info = [] #creates an empty chart for information to go into a 2D list
    state_file.readline() #reads everyline in the file

    for row in state_file: #goes through each line in the file
        row = row.rstrip('\n') #strips each row of the breaks
        vals = row.split(',') #separates each item with a comma
        state_info.append(vals) #adds each of the rows into the empty chart for the 2D list

    return state_info
    #TODO: you need to fill in the rest of this function


#this function should calculate (and return) the average difference
#between Clinton's and Trump's vote % in the state
#whose name is passed as the state_name parameter (which is just a string)
#The poll_data parameter is the 2D list with all of the poll info in it
def get_avg_diff(state_name, poll_data):
    # multiplier = 1 This was for the Multiplier
    # multchart = [] This was for the Multiplier and would hold the days column
    hillary = [] #creates an empty list of hillary votes
    trump = [] #creates an empty list of trump votes
    f = poll_data #makes my life easier
    for row in f: #goes through the first row of the data line
        for column in row: #goes through the columns
            if column == state_name: #finds the searched state name rows and only runs these columns
                hillary += [row[2]] #adds hillary vote column to hillary's empty chart
                trump += [row[3]] #adds trump votes column to trumps empty chart
                # multchart += row[1] added the days to the multiplier cjart
                # if multchart > 243: old are worth less
                #     multiplier = 1
                # elif multchart > 121: more recent are worth more
                #     multiplier = 2
                # elif multchart < 121: most recent are worth even more
                #     multiplier = 3
    hillary = map(int, hillary) #converts stringed numbers in hillary's chart to integers
    hillary = sum(hillary) #adds all of her votes
    # hillary *= multiplier
    trump = map(int, trump) #converts stringed numbers in trump's chart to integers
    trump = sum(trump) #adds all of his votes
    # trump *= multiplier
    average = hillary - trump #finds out who had the most votes
    if average > 0: #if hillary had the most votes it will set hillary to the average to pass into another function
        average = "Hillary" #sets hillary as the state winner
        print('-----------------------------------------')
        print("Hillary will win", state_name) #fun addition to see who won the state
    elif average < 0: #if trump had the most votes it will set trump to the average to pass into another function
        print('-----------------------------------------')
        print("Trump will win", state_name) #fun addition to see who won the state
        average = "Trump" #sets trump as the state winner
    else: #fun addition, just incase there is the chance of a tie or someother situation, VP will break the tie
        average = "VP"
        print("The vice president will decide.")
    print("Hillary:",hillary, '| Trump:', trump) #prints the final score for each state
    print('-----------------------------------------')
    return average

    #TODO: you need to fill in the rest of this function



def main():
    polls_2D_list = get_poll_data('president_polls2016.csv') #sets variable for polls file
    state_2D_list = get_state_data('ev_per_state2016.csv') #sets variable for states file
    trumpcard = 0 #sets trumps electoral vote score
    hillyes = 0 #sets hillaries electoral vote score
    for row in state_2D_list: #goes through each row in the state list to get the state name
        state_column = row[0] #gets the state name
        average = get_avg_diff(state_column,polls_2D_list) #runs the state name through the function above to get a returned winner of the state
        if average == "Trump": #if the return value is Trump won the state it will add to trumps overall score
            points = int(row[1]) #finds amount of electoral votes trump should gain
            trumpcard += points #adds electoral votes to trump's total count
        if average == "Hillary": #if the return value is Hillary won the state it will add to hillarys overall score
            points = int(row[1]) #finds amount of electoral votes hillary should gain
            hillyes += points #adds electoral votes to hillarys total count
    if hillyes > trumpcard: #determines who is the winner based on total electoral votes, sets hillary as the winner and tells total votes
        print('*******************************************')
        print("Hillary will win with", hillyes, "votes")
        print("Trump will lose with", trumpcard, "votes")
        print('*******************************************')

    else: #sets trump to the winner if not Hillary and tells total votes
        print('*******************************************')
        print("Trump will win with", trumpcard, "votes")
        print("Hillary will lose with", hillyes, "votes")
        print('*******************************************')


    #TODO: loop through the state_2D_list
    #for each state, call get_avg_diff to calculate the average difference
    #in the polls for each candidate and total up the number of electoral
    #votes you project each candidate to win.
    #print out the final results for your prediction


#this function can be used to test the functions individually
#before making them all work together in the final program

#TODO: change this to instead just call main when your main function is ready to be tested
main()
