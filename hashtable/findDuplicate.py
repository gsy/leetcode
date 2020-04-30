class Solution:
    def findDuplicate(self, paths):
        revert = {}

        for path in paths:
            ls = path.split(" ")
            directory = ls[0]
            for nameContent in ls[1:]:
                name, content = nameContent.split("(")
                content = content[:-1]
                filepaths = revert.get(content, [])
                filepaths.append(directory + "/" + name)
                revert[content] = filepaths

        result = []
        for content, filepaths in revert.items():
            if len(filepaths) > 1:
                result.append(filepaths)
        return result
