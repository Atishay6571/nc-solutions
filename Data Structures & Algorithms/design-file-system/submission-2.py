class FileSystem:

    def __init__(self):
        self.hmap = {"": 0} # maps values to their values

    def createPath(self, path: str, value: int) -> bool:
        part = path.rsplit('/',1 )
        if part[1] == "" or part[0] not in self.hmap or path in self.hmap:
            return False
        self.hmap[path] = value
        return True

    def get(self, path: str) -> int:
        return self.hmap.get(path, -1)     


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
