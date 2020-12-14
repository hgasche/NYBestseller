#book class to store the information of a book
#this class is used to make objects
#it makes an instance of Book
#with the required paramters as title, author, publisher,
#date and category
class Book:
  #constructor of the class to create an isinstance
  #of Book class, by accepting the required parameters
  #of Book Instance
  def __init__(self, title, author, publisher, date, category):
    self.title = title
    self.author = author
    self.publisher = publisher
    self.date = date
    self.category = category

#if user inputs 1
#takes the starting and ending year as input
#and then show the books between these dates
def lookUpRange(books):
  beg=int(input("Enter beginning year: "))
  end=int(input("Enter ending year: "))
  if end<beg:
    end=int(input("Invalid input, ending year can't be less than beginning, Enter again: "))
  print("All Titles between "+str(beg)+" and "+str(end))
  found=False
  for book in books:
    year=int(book.date.split('/')[2])
    if year>=beg and year<=end:
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  if found==False:
    print("No Results Found...")
#if user inputs 2
#user takes input the month
#and the year
#then it iterates on all books, and selects
#the all books and display that are on this month and year
def lookUpMonthYear(books):
  mon=int(input("Enter month (as a number, 1-12): "))
  if mon<1 or mon>12:
    mon=int(input("Invalid Input, Only enter in range(as a number, 1-12): "))
  year=int(input("Enter year: "))
  found=False
  for book in books:
    year1=int(book.date.split('/')[2])
    mon1=int(book.date.split('/')[0])
    if mon==mon1 and year==year1:
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  if found==False:
    print("No Results Found...")
#if user inputs 3
#take input authors Name
#then iterates over the all books
#check if the author name entered is found in any of the book
#prints the book detail then
def searchAuthor(books):
  name=input("Enter an author's name (or part of a name): ")
  found=False
  for book in books:
    if name.lower() in book.author.lower():
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  if found==False:
    print("No Results Found...")
#if user inputs 4, then it asks user to enter the title of book
#iterates on all the books, check if a title matches
#prints the result of titles
def searchTitle(books):
  title=input("Enter a title (or part of a title): ")
  found=False
  for book in books:
    if title.lower() in book.title.lower():
      print("\t"+book.title+", by "+book.author+" ("+book.date+")")
      found=True
  if found==False:
    print("No Results Found...")

#calling open to to open the text file for reading data
file = open("bestsellers.txt","r")

#in strat creating an array of books, starting
#from empty, It will be updated as data supplied to it
books=[]

#looping over the data in the file line by line
#it reads a line, then parses the line to get data fields
for line in file:
  #split a line on spaces, to get the fields separated
  fields = line.split()
  #after splitting, it picks the book title, author, date publisher and category on the basis of Books added to it
  #it creates the instance books
  #and appends this instance to the list
  books.append(Book(fields[0],fields[1],fields[2],fields[3],fields[4]))

#initial menu to show a choice
#it asks user to input the required Value
#and then decides to which option to choose based
#upon user input
print("What would you like to do?")
print("1: Look up year range")
print("2: Look up month/year")
print("3: Search for author")
print("4: Search for title")
print("Q: Quit")

#input read
choice=input("> ")
#repeat loop until the value entered
#is in correct range which means its between 1 and 4
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
    print("Invalid Option, Try again... ")
  #display menu again, to take input
  #this menu is in loop, so it will keep showing this menu
  #until the user chooses invalid value or Q
  print("What would you like to do?")
  print("1: Look up year range")
  print("2: Look up month/year")
  print("3: Search for author")
  print("4: Search for title")
  print("Q: Quit")
  #taking menu input
  choice=input("> ")

print("--------------- good bye -----------------")
#close the file read
file.close()

Y
