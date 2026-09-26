class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {}

        for key, value in knowledge:
            d[key] = value

        ans = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                if key in d:
                    ans += d[key]
                else:
                    ans += "?"

                i = j + 1

            else:
                ans += s[i]
                i += 1

        return ans        