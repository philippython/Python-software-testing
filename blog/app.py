from blog import Blog
MENU_PROMPT = 'Enter "c" to create blog, "l to list blogs, "r" to read one , "p" to create post, or "q" to quit'
POST_FORMAT = """
-------{}------------

{}
"""
blogs = {}

def menu():

    print_blogs()
    selection = input(MENU_PROMPT)
    # while selection != 'q':
    if selection == 'c':
            ask_to_create_blog()
    elif selection == 'l':
            print_blogs()
    elif selection == 'r':
            ask_to_read_blog()
    elif selection == 'p':
            ask_to_create_post()
    # selection = input(MENU_PROMPT)

def print_blogs():
    for blogname , blog in blogs.items():
        print('- {}'.format(blog))

def ask_to_create_blog():
    blog_title = input("Enter blog Title")
    blog_author = input("Enter blog content ")
    blogs[blog_title] = Blog(blog_title, blog_author)
     
    
def ask_to_read_blog():
    title = input('Enter Blog title of blog you want to read')
    print_post(blogs.get(title, "Blog Not found"))

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_FORMAT.format(post.title, post.content))

def ask_to_create_post():
    pass
    # blog_content = input('Enter Blog title of blog you want to creat a')
    # blog = blogs.get(blog_content, "Blog does not exist")
    

