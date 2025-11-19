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
    
    @property
    def author(self):
        """Getter for author property."""
        return self._author
    
    @author.setter
    def author(self, value):
        """
        Setter for author property.
        Can be changed after initialization.(mutable)
        Author must be an instance of Author class.
        """
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = value
    
    @property
    def magazine(self):
        """Getter for magazine property."""
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        """
        Setter for magazine property with validation.
        Can be changed after initialization.(mutable)
        Magazine must be an instance of Magazine class.
        """
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        self._magazine = value

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """Getter for name property."""
        return self._name



    @name.setter
    def name(self, value):
        """
        Setter for name property with validation.
        Name must be a non-empty string.
        Once set, name cannot be changed (uses hasattr to check if _name is already set).
        """
        #prevent changing name if already set
        if hasattr(self, '_name'):
            return
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        
        #validate name is not empty
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = value  

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