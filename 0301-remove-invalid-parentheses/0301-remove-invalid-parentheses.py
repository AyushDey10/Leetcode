class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = set([s])

        while queue:
            valid = []

            for current in queue:
                if isValid(current):
                    valid.append(current)

            if valid:
                return valid

            next_queue = []

            for current in queue:
                for i in range(len(current)):
                    if current[i] != '(' and current[i] != ')':
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]