from tree import Tree


def mk_tree1():
    tree = Tree("A", 20)
    b = Tree("B", 80)
    c = Tree("C", 50)
    d = Tree("D", 110)
    e = Tree("E", 60)
    f = Tree("F", 150)

    tree.add_child(b)
    tree.add_child(c)
    c.add_child(d)
    c.add_child(e)
    d.add_child(f)

    return tree


def mk_tree2():
    tree = Tree("A", 20)
    b = Tree("B", 80)
    c = Tree("C", 80)
    d = Tree("D", 110)
    e = Tree("E", 60)
    f = Tree("F", 50)

    tree.add_child(b)
    tree.add_child(c)
    c.add_child(d)
    c.add_child(e)
    d.add_child(f)

    return tree


def mk_tree3():
    tree = Tree("A", 70)
    b = Tree("B", 200)
    c = Tree("C", 80)
    d = Tree("D", 110)
    e = Tree("E", 60)
    f = Tree("F", 10)
    g = Tree("G", 32)
    h = Tree("H", 64)

    tree.add_child(b)
    b.add_child(f)
    tree.add_child(c)
    tree.add_child(e)
    c.add_child(d)
    e.add_child(g)
    e.add_child(h)

    return tree


def mk_tree4():
    return Tree("F", 10)


tree1 = mk_tree1()
tree2 = mk_tree2()
tree3 = mk_tree3()
tree4 = mk_tree4()
