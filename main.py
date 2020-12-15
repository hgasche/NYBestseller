########################################
######## PROJECT NEW YORK TIMES ########
########################################

#creation of "book" class to store the information of a book
#a Python class is used to define a particular type of object. In our case, it created an instance "Book" with the required parameters title, author, publisher, date and category
class Book:
  #constructor of the class to create an isinstance of Book class, by accepting the required parameters of the Book Instance
  def __init__(self, title, author, publisher, date, category):
    self.title = title
    self.author = author
    self.publisher = publisher
    self.date = date
    self.category = category


#DISPLAY ALL BOOKS IN A YEAR RANGE:
#if the user inputs "1", the task is to display all books in a year range entered
#first, take the starting and the ending year as input, then print all the books between these dates
def lookUpRange(books):
  beg=int(input("\nEnter beginning year: "))
  end=int(input("Enter ending year: "))
  #check whether the entered beginning year is bigger than the end variable as it needs to be verified that the interval is entered in the correct order. if end<beg, print a respective error message and ask for a new ending year
  if end<beg:
    end=int(input("\nPlease try again. Your ending year cannot be less than the beginning year. You can now enter a new ending year: "))
  #if the entered numbers are in the correct order, print out all book within the given year-frame
  print("\nHere are all books between "+str(beg)+" and "+str(end)," \n")
  found=False
  for book in books:
    year=int(book.date.split('/')[2])
    if year>=beg and year<=end:
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  #if there are no books on the bestseller list that fall in the range the user entered, print a respective error message
  if found==False:
    print("Unfortunately, no results were found...")


#DISPLAY ALL BOOKS IN A SPECIFIC MONTH AND YEAR:
#if user inputs "2", the task is to display all books in a specific month and year
#first, take the user's input for a specific month and then for a year
#a for loop is used to iterate on all books, and select the ones that fall into the given month of the given year
def lookUpMonthYear(books):
  mon=int(input("\nEnter month (as a number between 1-12): "))
  if mon<1 or mon>12:
    #in the case that the month number entered is either smaller than one or larger than 12, the user is asked to enter another number within the given range
    mon=int(input("Please try again. You can only enter a number in range 1-12): "))
  year=int(input("Enter year: "))
  #print the books of the user's month and year
  print(" \nHere are all books that reached #1 during the month "+str(mon)+" of the year "+str(year)," \n")
  found=False
  for book in books:
    year1=int(book.date.split('/')[2])
    mon1=int(book.date.split('/')[0])
    if mon==mon1 and year==year1:
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  #if there are no books on the bestseller list that reached nb.1 during the given month and year, print a respective error message
  if found==False:
    print("Unfortunately, no results were found...")


#SEARCH FOR AN AUTHOR:
#if user inputs "3", the task is to search for a specific author
#first, take input of one author's name (regardless of upper of lower case) and then, a for loop is used to iterate over the all books to check if the author name entered is found for any of the book
def searchAuthor(books):
  name=input("\nEnter an author's name (or a part of a name): ")
  print(" \nHere are all books of the author "+str(name),"\n")
  found=False
  for book in books:
    if name.lower() in book.author.lower():
      #print the details for all book of the author entered
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  #in the case that the author entered cannot be found for any of the books, print a respective error message
  if found==False:
    print("Unfortunately, no results were found...")


#SEARCH FOR A TITLE:
#if user inputs "4", the task is to search for a specific book title
#first, ask the user to enter the title of book (i.e. a word in the title), then a for loop is used to iterate on all the books and check if a title matches the input
def searchTitle(books):
  title=input("\nEnter a word of title (or a part of a title): ")
  print(" \nHere are all books that include the word "+str(title),"in their title \n")
  found=False
  for book in books:
    #if the entered title is found for one book on the list, print the result
    if title.lower() in book.title.lower():
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  #in the case that string input entered cannot be found in any of the books' titles, print a respective error message
  if found==False:
    print("Unfortunately, no results were found...")

    
#INPUT DATA SET AND CONSTRUCT A LIST OF BOOKS
#calling "open" in order to open the text file "bestellers.txt" that contains all books for reading data
file = open("bestsellers.txt","r")

#first, creating a list of books, that is first empty and will be filled as the data is supplied
books=[]

#looping over the data in the file line by line to read each line and then parse the line to get all data fields
for line in file:
  #split a line at the spaces to get the different information (title, author, publisher, date it first reached #1 on one of the best seller lists, and category) separated
  fields = line.split()
  #after splitting the content of the lines, pick the book title, author, date publisher and category on the basis of books added to the array
  #create the instance books and appends this instance to the list "books"
  books.append(Book(fields[0],fields[1],fields[2],fields[3],fields[4]))

#this is the initial menu/ console that shows the user a choice of options and asks him/her to choose one option by entering either a number between 1-4 or "Q" to quit the program
print("\nHello, what would you like to do?")
print("1: Look up year range")
print("2: Look up month/year")
print("3: Search for author")
print("4: Search for title")
print("Q: Quit")

#input read
choice=input("> ")
#check, whether the input is valid and repeat loop until the value entered is in correct range which means its between 1 and 4 or Q / q
while choice!='Q' and choice!='q':
  if choice=='1':
    lookUpRange(books)
  elif choice=='2':
    lookUpMonthYear(books)
  elif choice=='3':
    searchAuthor(books)
  elif choice=='4':
    searchTitle(books)
  elif choice!='Q' and choice!='q':
    print("\nUnfortunately, this is an invalid option. Please try again by entering one of the options displayed... ")

  #once one option was successfully performed, display the menu / console again, to take another input
  #as this menu is in loop, it will keep appearing until the user enters invalid input or decides to quit the program through choosing Q
  print("\nWhat would you like to do next?")
  print("1: Look up year range")
  print("2: Look up month/year")
  print("3: Search for author")
  print("4: Search for title")
  print("Q: Quit")
  #taking menu input
  choice=input("> ")

#when the user quits the program, print a "goodbye" message and terminate the program by closing the file
print("------------- Thank you and goodbye! ---------------")
file.close()
