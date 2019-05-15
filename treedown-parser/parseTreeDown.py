class Node:
    def __init__(self, par, data, lvl =0,  chs = list()):
        self.parent = par
        self.info = data
        self.children = chs
        self.level = lvl
    def tostr(self):
        return self.info
    def hasChildren(self):
        return not(self.children == []) or len(self.children) > 0

    def output(self):
        if not(self.hasChildren()):
            return tuple(self.info.split(" ", 1))
        else:
            cs = list(map(lambda x: x.output(), self.children))
            return tuple(["\n".join(self.info.split(" ", 1))] + cs  )
import re

def tokenize(raw):
    marker ='@#@#@'
    x = re.sub(r'\t|    ', marker, raw.strip())
    parts = x.split('\n')
    return list(map(lambda x: (x.count(marker), x.replace(marker, '')), parts))

def buildTree(cur, tokens):
    out = cur
    if cur == None:
        if len(list(filter(lambda x: x[0] == 0, tokens))) > 1:
            print("Wrapping tree")
            out = Node(None, "Tree", -1)
            buildTree(out, tokens)
            return out
        else:
            out = Node(tokens[0][1], tokens[0][1])
            buildTree(out, tokens[1:])
            return out
    if len(tokens) < 1:
        return cur
    t = tokens[0]
    print(cur.tostr())
    print(t)
    if cur.level < t[0]:
        print("Adding child Node")
        # add child node
        # change curNode
        n = Node(cur, t[1], t[0], [])
        cur.children.append(n)
        print(len(cur.children))
        return buildTree(n, tokens[1:])
    elif cur.level == t[0]:
        print("adding sibling")
        # add sibling node, don't change curnode
        n = Node(cur.parent, t[1], t[0], [])
        cur.parent.children.append(n)
        print(len(cur.parent.children))
        return buildTree(n, tokens[1:])
    else:
        print("Moving up the tree")
        while True:
            cur = cur.parent
            if cur.level == t[0]:
                break
        # add sibling Node
        n = Node(cur.parent, t[1], t[0], [])
        cur.parent.children.append(n)
        print(len(cur.parent.children))
        return buildTree(n, tokens[1:])
    return out
       
def writeToFile(treestr, filename):
    import svgling
    tree = svgling.draw_tree(treestr)
    svgobj = tree.get_svg()
    svgobj.filename = filename
    svgobj.save()

x = Node("", "v have")

def main(ifile, ofile):
    with open(ifile, 'r', encoding="UTF8") as f:
        treedown = f.read().strip()
        tree = buildTree(None, tokenize(treedown))
        writeToFile(tree.output(), ofile)
    print("Done!")

print(x.info)
print(x.parent)
print(x.children)

TEST = "s tree\n\tpn he\n    vp\n        d the\n\t\tn cat\n    adv quickly\ns tree 2\n"

#ts = tokenize(TEST)
#print(list(ts))
#tree = buildTree(None, ts)
#print("Tree start: " + tree.info)

#for t in tree.children:
#    print("    " + t.info)
#print(tree.output())

# writeToFile(tree.output(), "C:\\Users\\fhard\\Desktop\\my_tree.svg")
# writeToFile(("S", ("NP", "we"), ("VP", "run fast")), "C:\\Users\\fhard\\Desktop\\my_tree.svg")

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    main(args[0], args[1])
