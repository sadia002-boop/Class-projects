def add_book_to_file(filename, title, author, year, genre, readstatus):
    with open(filename, "a") as file:
         file.write("=== book details ===\n")
         file.write(f"Title: {title}\n")
         file.write(f"Author: {author}\n")
         file.write(f"Year: {year}\n")
         file.write(f"Genre: {genre}\n")
         file.write(f"Read status: {readstatus}\n")
         file.write("====================\n")
    print(f"Book added successfully!")

def remove_book_from_file(title_to_remove, filename):
    try:
        with open(filename, "r") as file:
            entries = file.read().split("=== book details ===\n")
        
        new_entries = []
        found = False
        for entry in entries:
            if entry.strip() == "":
                continue
            if f"Title: {title_to_remove}\n" in entry:
                found = True
            else:
                new_entries.append(entry)
        
        if found:
            with open(filename, "w") as file:
                for entry in new_entries:
                    file.write(entry.strip() + "=== book details ===\n")
            print("Book removed successfully!")
        else:
            print(f"No book with title '{title_to_remove}' found.")
    
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")

def search_book_by_title(search_title, filename):
    try:
        with open(filename, "r") as file:
            entries = file.read().split("=== book details ===\n")
        
        for entry in entries:
            if entry.strip() == "":
                continue
            if f"Title: {search_title}\n" in entry:
                print("Matching Books:\n" + entry.strip())
                return
        print(f"No book with title '{search_title}' found.")
    
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")

def serach_a_book_by_author(search_author, filename):
    try:
        with open(filename, "r") as file:
            entries = file.read().split("=== book details ===\n")

        found = False
        for entry in entries:
            if entry.strip() == "":
                continue
            if f"Author: {search_author}\n" in entry:
                print("Book by author found:\n" + entry.strip())
                print("Matching Books")
                found = True
        if not found:
            print(f"No books by author '{search_author}' found.")
    
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")

        
def display_all_books(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if content:
                print("All Books:\n")
                print(content)
                return True
            else:
                print("The book list is empty.")
                return False
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")

def display_book_statistics(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if not content:
                print("No books found.")
                return
            
            entries = content.split("=== book details ===\n")
            total_books = 0
            read_count = 0
            unread_count = 0

            for entry in entries:
                if entry.strip() == "":
                    continue
                total_books += 1

                # Manually extract author
                for line in entry.split("\n"):
                    line = line.strip()
                    if line.startswith("Read status: yes"):
                        read_count += 1
                        break
                    elif line.startswith("Read status: no"):
                        unread_count += 1
                        break

            print(f"Total books: {total_books}")
            if total_books > 0:
                read_percent = (read_count / total_books) * 100
                unread_percent = (unread_count / total_books) * 100
                print(f"Read: {read_count} ({round(read_percent, 2)}%)")
                print(f"Unread: {unread_count} ({round(unread_percent, 2)}%)")
            else:
                print("No status info found for books.")
    
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")

def exit_program():
    print("\nThank you for using the Book Manager!")
    print("Goodbye and happy reading! 📚✨\n")
    exit()

    

while True:
    print("""Welcome to your Personal Library Manager!  
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Display statistics  
6. Exit """)
    your_choice = input("Enter your choice:")
    filename = "sadia.txt"
    
    if your_choice == "add a book":
        title = input("Enter the book title:") 
        author = input("Enter the author:")
        year = input("Enter the publication year:")
        genre = input("Enter the genre:")
        readstatus = input("Have you read this book:")

        result = add_book_to_file(filename, title, author, year, genre, readstatus)
        print(result)

    elif your_choice == "remove a book":
        title = input("Enter the title of the book to remove:")
        remove_book_from_file(title, filename) 
    elif your_choice == "search for a book":
        print("""Search by:  
    1. Title  
    2. Author""")
        search_choice = input("Enter your choice (1/2): ")
        if search_choice == str(1) :
            title = input("Enter the title: ")
            search_book_by_title(title, filename)

        elif search_choice == str(2):
            author = input("Enter the author: ")
            serach_a_book_by_author (author, filename)

    elif your_choice == "display all books":
        display_all_books (filename)

    elif your_choice == "display Statistics":
       display_book_statistics(filename)
    
    elif your_choice == "exit":
        exit_program()
        break
    else: 
        print("Invalid option. Try again.")
