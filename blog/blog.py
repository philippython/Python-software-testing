from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
        return "Blog {}, {}, {}".format(self.title, self.author, self.posts)

    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post.json())

blog = Blog("TestBlog", "Testauthor")
print(blog)