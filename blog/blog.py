class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
        return "Blog {}, {}, {}".format(self.title, self.author, self.posts)