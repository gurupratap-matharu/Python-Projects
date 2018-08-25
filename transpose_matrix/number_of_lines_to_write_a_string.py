class Solution:

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        self.line_width = 100
        self.s = S
        self.no_of_lines = 1

        # First we make a dictionary for each letter and its corresponding width
        letter_widths = {key: value for key, value in zip('abcdefghijklmnopqrstuvwxyz', widths)}

        for alphabet in self.s:

            if self.line_width - letter_widths[alphabet] >= 0:
                self.line_width -= letter_widths[alphabet]
            else:
                self.line_width = 100
                self.line_width -= letter_widths[alphabet]
                self.no_of_lines += 1
        return [self.no_of_lines, 100 - self.line_width]


ex1 = Solution()
print(ex1.numberOfLines([4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "bbbcccdddaaa"))

ex2 = Solution()
print(ex2.numberOfLines([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "abcdefghijklmnopqrstuvwxyz"))
