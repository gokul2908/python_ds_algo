class Tree:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        self.parent = None
        self.children = []

    def child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        x = self.parent
        while x:
            x = x.parent
            level += 1
        return level

    def print_tree(self, name=True, position=True):
        level = self.get_level()
        space = level*"    "
        prefix = space + "|_" if self.parent else ""
        if name == True and position == False:
            print(prefix+self.name+"\n")
        elif name == False and position == True:
            print(prefix+self.position+"\n")
        else:
            print(prefix+self.name+" "+"("+self.position+")"+"\n")

        i = 0
        while i < len(self.children):
            self.children[i].print_tree(name, position)
            i += 1


parent = Tree("Nilupul", "CEO")

level_1a = Tree("Chinmay", "CTO")
parent.child(level_1a)
level_2a = Tree("Vishva", "Infrastructure head")
level_1a.child(level_2a)
level_3a = Tree("Dhaval", "cloud manager")
level_3b = Tree("abhi", "App Manager")
level_2a.child(level_3a)
level_2a.child(level_3b)
level_1b = Tree("Gel", "HR")
parent.child(level_1b)
level_2b = Tree("Peter", "Recruitment manager")
level_2c = Tree("waque", "policy manager")
level_1b.child(level_2b)
level_1b.child(level_2c)

parent.print_tree(name=True, position=False)
