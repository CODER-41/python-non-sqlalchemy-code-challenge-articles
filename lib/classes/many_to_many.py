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
        """
        Returns a list of Article instances written by this author.
        Filters the Article.all list to find articles where author matches self.
        """
        return [article for article in Article.all if article.author == self]

        #pass

    def magazines(self):
        """
        Retuns a unique list of magazines this author has contributed to.
        Uses a set to collect unique magazines from the author's articles.
        """
        return list (set([article.magazine for article in self.articles()]))

        #pass

    def add_article(self, magazine, title):
        """
        Creates and returns a new Article instance.
        Associates the article with this author and the provided magazine
        """

        return Article(self, magazine, title)

        #pass

    def topic_areas(self):
        """
        Returns a unique list of category strings for magazines this author has contributed to.
        Returns None if the author has not contributed to any magazines.
        """
        articles = self.articles()
        #return None if author has no articles
        if not articles:
            return None
        #collect unique categories from magazines of author's articles
        return list(set([article.magazine.category for article in articles]))


        #pass

class Magazine:
    #class variable to track all magazine instances
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category

        Magazine.all.append(self)

    @property
    def name(self):
        """Getter for name property."""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Setter for name property with validation.
        Name must be a string between 2 and 16 characters (inclusive).
        Can be changed after initialization.(mutable)

        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        #validate  name length (2-16 characters)
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        """Getter for category property."""
        return self._category
    
    @category.setter
    def category(self, value):
        """
        Setter for category property with validation.
        Category must be a non-empty string.
        Can be changed after initialization.(mutable)
        """
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        #validate category is not empty
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value


    def articles(self):
        """
        Returns a list of all articles published in this magazine.
        Filters the Article.all list to find articles where magazine matches self.
        """
        return [article for article in Article.all if article.magazine == self]

        #pass

    def contributors(self):
        """
        Returns a unique list of authors who have contributed to this magazine.
        Uses a set to collect unique authors from the magazine's articles and to remove duplicates.
        """
        return list(set([article.author for article in self.articles()]))
        #pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass