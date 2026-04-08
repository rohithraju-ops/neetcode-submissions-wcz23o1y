class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out = []
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit() :
                out.append(int(operations[i]))
            elif operations[i] == "+" :
                out.append(out[-1] + out[-2])
            elif operations[i] == "C" :
                out.pop()
            elif operations[i] == "D" :
                prod = 2 * out[-1]
                out.append(prod)
        return sum(out)