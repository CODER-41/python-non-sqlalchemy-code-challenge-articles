class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self.name = name

    @property
    def name(self):
        return self.__qualname__
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise  AttributeError("Cannot change name after author is instatiated")
        self._name = value

    def articles(self):
        return[article for article in Article._all if article.auuthor == self]
        #pass

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
        #pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        #pass

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set([article.magazine.category for article in articles]))
        #pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not(2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass