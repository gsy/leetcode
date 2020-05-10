# -*- coding: utf-8 -*-

import argparse
import json
import importlib


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.hegiht = 0

def arr2Tree(arr):
    length = len(arr)
    nodes = []
    for i in range(length):
        val = arr[i]
        if val is not None:
            node = TreeNode(val)
        else:
            node = None
        nodes.append(node)

        if i > 0:
            parent = nodes[(i-1) // 2]
            if i % 2 == 1:
                parent.left = node
            else:
                parent.right = node
    return nodes[0]

def printTree(root):
    if root is None:
        return ""

    levels = []
    relationships = []
    nodes = [root]

    while len(nodes) > 0:
        values = []
        next_level = []
        relationship = []

        for node in nodes:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)
                values.append(node.value)
                if node.left:
                    relationship.append("/")
                else:
                    relationship.append(" ")
                if node.right:
                    relationship.append("\\")
                else:
                    relationship.append(" ")
        nodes = next_level
        levels.append(values)


        


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(testsuit):
    with open(testsuit, "r") as rfile:
        answer = json.load(rfile)
        module = importlib.import_module(answer["module"])
        instance = module.Solution()
        entry_func = getattr(instance, answer["module"])

        count = 0
        total = len(answer["cases"])
        for case in answer["cases"]:
            count = count + 1
            input = case["tree"]
            output = case["output"]

            root = arr2Tree(input[0])
            actual = entry_func(root, input[1])

            if actual != output:
                print(f"{bcolors.FAIL}[failed {count}/{total}] input: {input}, expect: {output}, got: {actual}{bcolors.ENDC}")
                exit(1)
            else:
                print(f"{bcolors.OKGREEN}[{count}/{total}]{bcolors.ENDC}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("testsuit", help="test suit")

    args = parser.parse_args()
    main(args.testsuit)
