class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def toString(root):
    if root is None:
        return ""

    level = [root]
    values = []
    while level:
        next_level = []
        value = []
        for node in level:
            if node:
                value.append(str(node.val))
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                value.append("$")
                # left
                next_level.append(None)
                next_level.append(None)
        values.append(" ".join(value))
        level = next_level
        if all(item == '$' for item in value):
            break

    result = ""
    for value in values:
        result += " ".join(value) + "\n"
    return result


def from_list(ls):
    if not ls:
        return None

    nodes = [TreeNode(int(value)) if value is not None else None for value in ls]
    i, j, length = 0, 1, len(nodes)

    while j < length:
        root = nodes[i]
        if root is None:
            i += 1
            continue
        else:
            left = nodes[j]
            right = nodes[j + 1] if j + 1 < length else None
            root.left = left
            root.right = right
            i += 1
            j += 2

    return nodes[0]


if __name__ == '__main__':
    root = from_list([3, 2, 3, None, 3, None, 1])
    print(toString(root))
