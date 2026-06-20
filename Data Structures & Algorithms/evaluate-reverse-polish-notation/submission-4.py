class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        a, b = 0, 0
        for i in tokens:
            if i == "+" or i == "-" or i =="*" or i == "/":
                b = s.pop()
                a = s.pop()
                if i == "+":
                    temp = int(a) + int(b)
                    s.append(temp)
                elif i == "-":
                    temp = int(a) - int(b)
                    s.append(temp)
                elif i == "*":
                    temp = int(a) * int(b)
                    s.append(temp)
                elif i == "/":
                    temp = int(int(a) / int(b))
                    s.append(temp)
            else:
                s.append(i)
        res = s.pop()
        return int(res)