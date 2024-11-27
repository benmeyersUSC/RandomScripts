
class Node:
    def __init__(self, fn, name):
        self.children = []
        self.fn = fn
        self.parents = []
        self.output = 0
        self.name = str(name)

    def __repr__(self):
        return self.name

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def run(self, stack=None, depth=0):
        log = lambda msg: print(f'{(depth * "\t")}{self}: ' + msg)
        log(f"Running {self} with stack = {stack}")
        stack = stack or set()
        next_stack = set(list(stack) + [self])
        # self.output = self.fn(*map(lambda n: n.output if n in stack else n.run(next_stack), self.parents))
        parent_outputs = []
        for parent in self.parents:
            if parent in stack:
                log(f"Parent: {parent} is in stack so we take last output {parent.output}")
                parent_outputs.append(parent.output)
            else:
                log(f"Parent: {parent} is not in stack, so we go back")
                parent_outputs.append(parent.run(next_stack, depth + 1))
        self.output = self.fn(*parent_outputs)
        log(f"IN: {parent_outputs} -->  {self.output}")
        return self.output

make_nor = lambda name: Node(lambda x, y: 1 - (x | y), name)

nor1 = make_nor('nor1')
nor2 = make_nor('nor2')
lightbulb = Node(lambda x: x, 'lightbulb')

run = 0
input1 = Node(lambda: [0, 1, 0, 0, 0][run], 'input1')
input2 = Node(lambda: [0, 0, 0, 1, 0][run], 'input2')

nor1.add_child(nor2)
nor2.add_child(nor1)
nor2.add_child(lightbulb)
input1.add_child(nor1)
input2.add_child(nor2)

def eval_node(node):
    global run
    prev_out = None
    out = node.output
    while prev_out != out:
        prev_out = out
        out = node.run()

    run += 1
    return out

print(f'Result1: {eval_node(lightbulb)}\n')
print(f'Result2: {eval_node(lightbulb)}\n')
print(f'Result3: {eval_node(lightbulb)}\n')
print(f'Result4: {eval_node(lightbulb)}\n')
print(f'Result5: {eval_node(lightbulb)}\n')