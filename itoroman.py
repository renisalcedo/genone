class IntRoman:
    def __init__(self, num):
        self.num = num
        self.table = {500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

    def start_point(self, num):
        table_values = [500, 100, 50, 10, 5, 1]

        for key in table_values:
            if num - key > 0:
                return (num - key, key)

    def int_to_roman(self):
        if self.num not in self.table:
            res = []
            n = self.num

            while n > 0:
                if n + 1 in self.table:
                    res.append(self.table[1])
                    res.append(self.table[n+1])

                    n -= n + 1
                    n -= 1

                elif n - 1 in self.table:
                    res.append(self.table[n-1])

                    n -= n - 1

                else:
                    print(n)
                    num, key = self.start_point(n)
                    res.append(self.table[key])

                    n = num

            return "".join(res)


            # vals = self.get_values(self.num)
            # zeroes = len(vals) - 1
            # res = []

            # for n in reversed(vals):
            #     if zeroes > 0:
            #         curr = n * 10

            #         if curr in self.table:
            #             res.append(self.table[curr])
            #         else:
            #             res.append(self.table[10] * n)

            #         zeroes -= 1

            #     else:
            #         while n > 0:
            #             if n in self.table:
            #                 res.append(self.table[n])

            #                 n -= n

            #             elif n - 1 in self.table:
            #                 res.append(self.table[n-1])

            #                 n -= n-1

            #             elif n + 1 in self.table: 
            #                 res.append(self.table[1])
            #                 res.append(self.table[n+1])

            #                 n -= n + 1
            #                 n -= 1

            #             else:
            #                 n -= 1
            #                 res.append(self.table[1])

            # return "".join(res)

        else:
            return self.table[self.num]

    # def get_values(self, num):
    #     vals = []

    #     while num > 0:
    #         vals.append(num % 10)
    #         num //= 10

    #     return vals

introman = IntRoman(16)
print(introman.int_to_roman())