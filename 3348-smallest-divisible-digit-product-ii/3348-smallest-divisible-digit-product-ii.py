class Solution(object):
    def smallestNumber(self, num, t):
        need = [0, 0, 0, 0]

        while t % 2 == 0:
            need[0] += 1
            t //= 2

        while t % 3 == 0:
            need[1] += 1
            t //= 3

        while t % 5 == 0:
            need[2] += 1
            t //= 5

        while t % 7 == 0:
            need[3] += 1
            t //= 7

        if t != 1:
            return "-1"

        factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }

        memo = {}

        def min_digits(a, b, c, d):
            if a <= 0 and b <= 0 and c <= 0 and d <= 0:
                return 0

            key = (a, b, c, d)

            if key in memo:
                return memo[key]

            best = float('inf')

            for digit in range(2, 10):
                f = factors[digit]

                na = max(0, a - f[0])
                nb = max(0, b - f[1])
                nc = max(0, c - f[2])
                nd = max(0, d - f[3])

                if (na, nb, nc, nd) == (a, b, c, d):
                    continue

                value = 1 + min_digits(na, nb, nc, nd)

                if value < best:
                    best = value

            memo[key] = best
            return best

        def build(required, length):
            if min_digits(*required) > length:
                return None

            result = []

            for _ in range(length):
                for digit in range(1, 10):
                    f = factors[digit]

                    new_required = (
                        max(0, required[0] - f[0]),
                        max(0, required[1] - f[1]),
                        max(0, required[2] - f[2]),
                        max(0, required[3] - f[3])
                    )

                    if min_digits(*new_required) <= length - len(result) - 1:
                        result.append(str(digit))
                        required = new_required
                        break

            return ''.join(result)

        current = [0, 0, 0, 0]
        has_zero = False

        for ch in num:
            if ch == '0':
                has_zero = True
                continue

            f = factors[int(ch)]

            for j in range(4):
                current[j] += f[j]

        if not has_zero:
            if all(current[j] >= need[j] for j in range(4)):
                return num

        n = len(num)
        prefix = current[:]
        zero_count = num.count('0')

        for pos in range(n - 1, -1, -1):
            ch = num[pos]

            if ch == '0':
                zero_count -= 1
            else:
                f = factors[int(ch)]

                for j in range(4):
                    prefix[j] -= f[j]

            if zero_count != 0:
                continue

            original = int(ch)

            for digit in range(original + 1, 10):
                f = factors[digit]

                required = [
                    max(0, need[0] - prefix[0] - f[0]),
                    max(0, need[1] - prefix[1] - f[1]),
                    max(0, need[2] - prefix[2] - f[2]),
                    max(0, need[3] - prefix[3] - f[3])
                ]

                remaining = n - pos - 1

                suffix = build(required, remaining)

                if suffix is not None:
                    return num[:pos] + str(digit) + suffix

        minimum_length = min_digits(*need)
        length = max(n + 1, minimum_length)

        return build(tuple(need), length)


sol = Solution()

print(sol.smallestNumber("1234", 256))
print(sol.smallestNumber("12355", 50))
print(sol.smallestNumber("11111", 26))
print(sol.smallestNumber("2887553", 4147200000))