import os


def get_resource_file_path(resource_name: str):
    return (os.path.join(os.path.abspath(os.curdir), 'resources',  resource_name))

