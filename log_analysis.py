__author__ = 'guang'
import collections

class LogAnalyser(object):
    def __init__(self, filename):
        self.user = []
        self.topic = []
        self.filename = filename

    def get_line_token(self):
        """
        >>> reader = LogAnalyser("/Users/guang/code/python/learning/test.txt")
        >>> for line in reader.get_line_token():
        ...     print line
        """
        with open(self.filename, "r") as f:
            for line in f.readlines():
                yield line.split()

    def visit_twice(self):
        """
        :return:
        >>> reader = LogAnalyser("/Users/guang/code/python/learning/test.txt")
        >>> candidates = [line for line in reader.visit_twice()]
        >>> len(candidates)
        3
        """
        counter = collections.defaultdict()

        for tokens in self.get_line_token():
            user = tokens[3]
            method = tokens[5]
            category = tokens[6].split("/")[1]
            if category == "topic" and method == "GET":
                counter[user] = counter.get(user, 0) + 1
                if counter[user] >= 2:
                    yield tokens

    def different_topic(self):
        """
        :return:
        >>> reader = LogAnalyser("/Users/guang/code/python/learning/test.txt")
        >>> result = [user for user in reader.different_topic()]
        >>> len(result)
        1
        """
        counter = collections.defaultdict()

        for tokens in self.visit_twice():
            user = tokens[3]
            topic = tokens[6].split("/")[2]
            topics = counter.get(user, [])
            if topics and topic not in topics:
                yield tokens

            topics.append(topic)
            counter[user] = topics

    def at_least_two_user_read_twice(self):
        counter = collections.defaultdict()

        for tokens in self.different_topic():
            user = tokens[3]
            topic = tokens[6].split("/")[2]
            users = counter.get(topic, [])
            if users and user not in users:
                yield tokens

            users.append(user)
            counter[topic] = user

