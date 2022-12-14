from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
        return "{} by {} ({} post{})".format(self.title, self.author, len(self.posts), 's' if len(self.posts) > 1 else "")

    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post.json())

    def json(self):
        return {
            "title" : self.title,
            "author" : self.author,
            "posts": self.posts,
        }
