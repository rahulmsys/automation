import os


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
            print('Directory created')
        except OSError as e:
            print(e)
            raise e
    else:
        print('Directory already exists: {}'.format(dir_name))
