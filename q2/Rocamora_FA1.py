class LibraryObjects:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        if author is None:
                    self.author = "Unknown Author"

    @property
    def get_title(self):
        print(self.title)

    @property
    def get_author(self):
        print(self.author)

    @get_title.setter
    def set_title(self, title):
        self.title = title
        print(f"Title updated to: {self.title}")

    @get_author.setter
    def set_author(self, author):
        self.author = author
        print(f"Author updated to: {self.author}")

    @property
    def display_info(self):
        print(f"{self.title} by {self.author}")

class Book(LibraryObjects):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages
        if self.number_of_pages is not None and self.number_of_pages <= 0:
            raise ValueError("Number of pages must be a positive integer.")

    @property
    def display_info(self):
        print(f"{self.title} by {self.author}, Pages: {self.number_of_pages}")

    @property
    def get_number_of_pages(self):
        print(f"Number of pages: {self.number_of_pages}")

    @get_number_of_pages.setter
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages is not None and number_of_pages <= 0:
            raise ValueError("Number of pages must be a positive integer.")
        self.number_of_pages = number_of_pages
        print(f"Number of pages updated to: {self.number_of_pages}")

class Magazine(LibraryObjects):
    def __init__(self, title, author, issue_number = None):
        super().__init__(title, author)
        self.issue_number = issue_number
        if self.issue_number is not None and self.issue_number <  0:
            raise ValueError("Issue number must be a positive integer.")
        elif self.issue_number is None:
            self.issue_number = "N/A"

    @property
    def display_info(self):
        print(f"{self.title} by {self.author}, Issue: {self.issue_number}")

    @property
    def get_issue_number(self):
        print(f"Issue number: {self.issue_number}")


    @get_issue_number.setter
    def set_issue_number(self, issue_number):
        if issue_number is not None and issue_number < 0:
            raise ValueError("Issue number must be a positive integer.")
        self.issue_number = issue_number
        print(f"Issue number updated to: {self.issue_number}")

mag = Magazine("bagazine", "Tinoy", 1)
book = Book("book", "Tinoy", 100)


mag.display_info
mag.set_issue_number = 2
mag.get_issue_number
mag.display_info
