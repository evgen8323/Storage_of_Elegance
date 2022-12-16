def generate(ans, cur, open, closed, n):
    if len(cur) == 2 * n:
        ans.append(cur)
    if open < n:
        generate(ans, cur + '(', open+1, closed, n)
    if closed < open:
        generate(ans, cur + ')', open, closed+1, n)

def parens(n):
    ans = []
    generate(ans, '', 0, 0, n)
    return ans
