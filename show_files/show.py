import os


def _files(directory):
    return (os.path.join(directory, f) for f in os.listdir(directory))


def canonical(f, rel_path=os.curdir):
    return os.path.realpath(os.path.join(os.path.realpath(rel_path), f.strip('/')))


def show_files(directory):
    parent_dir = canonical(directory)

    return '\n'.join(_files(directory))


def subdirs(directory):
    return (f for f in _files(directory) if os.path.isdir(f))
