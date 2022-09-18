blogs = {}

def menu():

    print_blogs()


def print_blogs():
    for blogname , blog in blogs.items():
        print('- {}'.format(blog))

