import os


def get_resource_file_path(resource_name: str, root_dir=os.path.abspath(os.curdir)):
    return (os.path.join(root_dir, 'resources', resource_name))
