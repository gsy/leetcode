# -*- coding: utf-8 -*-

import argparse
import json
import importlib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2LinkList(ls):
    head, prev = None, None

    for item in ls:
        node = ListNode(item)
        if head is None:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def linkList2list(lls):
    result = []

    node = lls
    while node:
        result.append(node.val)
        node = node.next
    return result


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
            input = case["input"]
            output = case["output"]

            if answer["expand"]:
                if isinstance(input, list):
                    args = []
                    for item in input:
                        if isinstance(item, list):
                            args.append(list2LinkList(item))
                        else:
                            args.append(item)
                    actual = entry_func(*args)
                elif isinstance(input, dict):
                    actual = entry_func(**input)
                else:
                    actual = entry_func(input)
            else:
                if isinstance(input, list):
                    input = list2LinkList(input)
                actual = entry_func(input)

            if answer.get("convertResult", False):
                actual = linkList2list(actual)
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
