bookList = []
HP = {"title" : "HP","author" : "JK Rowling" ,"ISBN" : 2210,"genre" : "horror","avai_stat" : "yes"}
GD = {"title" : "Good Dad","author" : "David" ,"ISBN" : 2211,"genre" : "finance","avai_stat" : "no"}
dictGenre = {}
bookList.append(HP)
bookList.append(GD)


def add_book(title,author,ISBN,genre,avai_status):
    temp = {}
    temp["title"] = title
    temp["author"] = author
    temp["ISBN"] = ISBN
    temp["genre"] = genre
    temp["avai_stat"] = avai_status
    bookList.append(temp)


def search_by_isbn(ISBN):
    for book in bookList:
        if(book["ISBN"] == ISBN):
            print("Book is Available")
            print("Book title is ",book["title"])
            print("Book author is ",book["author"])
            print("Book title is ",book["genre"])
            print("Book title is ",book["avai_stat"])
            break

def update_book_details(ISBN):
    for book in bookList:
            if(book["ISBN"] == ISBN):
                print("Book is Available")
                temp = int(input('''1. Do you want to change title \n 2. Do you want to change author
3. Do you want to change genre \n 4. Do you want to change avaialbility status \n 5. Exit \n Enter that number'''))
                if(temp == 1):
                    temp2 = input("Enter new title")
                    book["title"] = temp2
                elif(temp == 2):
                    temp2 = input("Enter new author")
                    book["author"] = temp2
                elif(temp == 3):
                    temp2 = input("Enter new genre")
                    book["genre"] = temp2
                elif(temp == 4):
                    temp2 = input("Enter new avai_stat")
                    book["avai_stat"] = temp2
                else:
                    break


def generate_genre_report():
    dictGenre = {}
    for book in bookList:
        if(book["genre"] in dictGenre and book["avai_stat"] == "yes"):
            dictGenre[book["genre"]].append(book)
        elif(book["avai_stat"] == "yes"):
            dictGenre[book["genre"]] = [book]

    for genre,gList in dictGenre.items():
        print("genre :",genre)
        for book in gList:
            print(book)



add_book("Human","Random",2213,"finance","yes")

update_book_details(2210)

search_by_isbn(2210)

generate_genre_report()


    
