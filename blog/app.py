from blog import Blog
MENU_PROMPT = 'Enter "c" to create blog, "l to list blogs, "r" to read one , "p" to create post, or "q" to quit'
blogs = {}

def menu():

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_to_create_blog()
        elif selection == 'l':
            ask_to_list_blog()
        elif selection == 'r':
            ask_to_read_blog()
        elif selection == 'p':
            ask_to_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for blogname , blog in blogs.items():
        print('- {}'.format(blog))

def ask_to_create_blog():
    blog_info = input("Enter blog Title, content. In this format => Blog, Content")
    blog = Blog(blog_info.split(", ")[0], blog_info.split(", ")[1])
    blogs[blog_info.split(", ")[0]] = blog

def ask_to_list_blog():
    for blogname , blog in blogs.items():
        return ('- {}'.format(blog))

def ask_to_read_blog():
   blog_content = input('Enter Blog title of blog you want to read')
   return  blogs.get(blog_content, "Blog does not exist")

def ask_to_create_post():
    blog_content = input('Enter Blog title of blog you want to creat a')
    blog = blogs.get(blog_content, "Blog does not exist")
    