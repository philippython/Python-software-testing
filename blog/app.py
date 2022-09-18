MENU_PROMPT = 'Enter "c" to create blog, "l to list blogs, "r" to read one , "p" to create post, or "q" to quit'
blogs = {}

def menu():

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_to_create_blog()
        if selection == 'l':
            ask_to_list_blog()
        if selection == 'r':
            ask_to_read_blog()
        if selection == 'p':
            ask_to_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for blogname , blog in blogs.items():
        print('- {}'.format(blog))

def ask_to_create_blog():
    pass
def ask_to_list_blog():
    pass
def ask_to_read_blog():
    pass
def ask_to_create_post():
    pass
