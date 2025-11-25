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