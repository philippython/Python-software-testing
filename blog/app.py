MENU_PROMPT = 'Enter "c" to create blog, "l to list blogs, "r" to read one , "p" to create post, or "q" to quit'
blogs = {}

def menu():

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for blogname , blog in blogs.items():
        print('- {}'.format(blog))

