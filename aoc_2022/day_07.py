from typing import Dict


def nested_set(dic: Dict, keys, value):
    "Set value in a nested dict given a path."
    for key in keys:
        dic = dic.setdefault(key, {})
    size = dic.setdefault("size", 0)
    dic["size"] = size + value[1]


class FileSystem:
    def __init__(self, data):
        self.dir_tree = self.reconstruct(data)
        self.sizes = []

    def reconstruct(self, log: str) -> Dict:
        tree = {}
        cwd = []
        for line in log.split('\n'):
            match line.split():
                case ["$", "ls"]:
                    continue
                case ["$", "cd", ".."]:
                    cwd.pop()
                case ["$", "cd", "/"]:
                    cwd = ["/"]
                case ["$", "cd", directory]:
                    cwd.append(directory)
                case ["dir", dirname]:
                    nested_set(tree, cwd, ("dir", 0))
                case [size, filename]:
                    nested_set(tree, cwd, (filename, int(size)))
        return tree

    def du(self, dir_tree: Dict, dir_name='/'):
        if isinstance(dir_tree, dict):
            size = sum([self.du(dir_tree[key], dir_name=key) for key in dir_tree])
            self.sizes.append(size)
        else:
            size = dir_tree
        return size
