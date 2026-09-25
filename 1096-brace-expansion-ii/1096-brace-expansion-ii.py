class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        
        def union(A, B):
            return A | B

        def product(A, B):
            result = set()
            for a in A:
                for b in B:
                    result.add(a + b)
            return result

        def parse(i):
            result = set()
            current = set([""])

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    result = union(result, current)
                    current = set([""])
                    i += 1

                elif expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = product(current, inside)

                else:
                    current = product(current, set([expression[i]]))
                    i += 1

            result = union(result, current)

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)        