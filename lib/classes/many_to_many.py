class Article:
    # Class variable to track all articles instances
    all= []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        #Add this article for tracking  
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        """
        Setter for title property with validation and immutability.
        Title cannot be changed once set.(uses hasattr to check if _title is already set)
        Title muts be a string between 5 and 50 characters.
        """
        
        #prevent changing title if already set
        if hasattr(self, '_title'):
            return
        #validate that title is a string
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        #validate length of title
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass