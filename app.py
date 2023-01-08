from itertools import permutations, product


class Solver:
    # configurations
    operatorsAvailable = ['+', '-', '/', '*']
    total = 10
    expressions = []
    groups = []
    expressionsData = []

    def __init__(self, numbers, operators=[], debug=False):
        self.operators = operators
        self.numbers = numbers
        self.debug = debug
        self.setOperatorsAvailable()
        self.permutate()

        for data in self.groups:
            grouped = data['grouped']
            ungrouped = data['ungrouped']
            operatorCombinations = list(self.combinationsOfOperators())

            if len(grouped) == 0:
                for operatorCombination in operatorCombinations:
                    self.expressionsData.append(
                        f"{ungrouped[0]}{operatorCombination[0]}{ungrouped[1]}{operatorCombination[1]}{ungrouped[2]}{operatorCombination[2]}{ungrouped[3]}")

            if len(grouped) == 2:
                for operatorCombination in operatorCombinations:
                    self.expressionsData.append(
                        f"({grouped[0]}{operatorCombination[0]}{grouped[1]}){operatorCombination[1]}{ungrouped[0]}{operatorCombination[2]}{ungrouped[1]}")
                    self.expressionsData.append(
                        f"{grouped[0]}{operatorCombination[0]}({grouped[1]}{operatorCombination[1]}{ungrouped[0]}){operatorCombination[2]}{ungrouped[1]}")
                    self.expressionsData.append(
                        f"{grouped[0]}{operatorCombination[0]}{grouped[1]}{operatorCombination[1]}({ungrouped[0]}{operatorCombination[2]}{ungrouped[1]})")

            if len(grouped) == 3:
                for operatorCombination in operatorCombinations:
                    self.expressionsData.append(
                        f"({grouped[0]}{operatorCombination[0]}{grouped[1]}{operatorCombination[1]}{grouped[2]}){operatorCombination[2]}{ungrouped[0]}")
                    self.expressionsData.append(
                        f"{grouped[0]}{operatorCombination[0]}({grouped[1]}{operatorCombination[1]}{grouped[2]}{operatorCombination[2]}{ungrouped[0]})")

        self.expressions = [
            expressionString for expressionString in self.expressionsData if self.calculate(expressionString)]

        if self.debug == False:
            self.solutions = self.expressions
        else:
            print("\n".join(self.expressions))

    def setOperatorsAvailable(self) -> None:
        if len(self.operators):
            self.operatorsAvailable = [
                operator for operator in self.operatorsAvailable
                if operator in self.operators]

    def getOperatorsAvailable(self) -> list:
        return self.operatorsAvailable

    def getNumbers(self) -> list:
        return [number for number in self.numbers]

    def permutate(self) -> None:

        for numsT in permutations(self.numbers):
            self.groups.append({
                "grouped": [],
                "ungrouped": list(numsT)
            })

        for (num1, num2) in permutations(self.getNumbers(), 2):
            numberList = self.getNumbers()
            numberList.remove(num1)
            numberList.remove(num2)
            self.groups.append({
                "grouped": [num1, num2],
                "ungrouped": numberList
            })

        for (num1, num2, num3) in permutations(self.getNumbers(), 3):
            numberList = self.getNumbers()
            numberList.remove(num1)
            numberList.remove(num2)
            numberList.remove(num3)
            self.groups.append({
                "grouped": [num1, num2, num3],
                "ungrouped": numberList
            })

    def calculate(self, expression: str) -> bool:
        if type(expression) == str:
            try:
                mathResult = eval(expression)
                if self.debug == True:
                    # print({"expression": expression, "mathResult": mathResult})
                    print(f"{expression},{mathResult}")
                if float(mathResult) == float(self.total):
                    return True
            except Exception as e:
                pass
        return False

    def combinationsOfOperators(self):
        return product(self.operatorsAvailable, repeat=len(self.numbers)-1)


# mathExpression = Solver([5, 1, 1, 8], operators=['+', '-', '/', '*'], debug=False)
mathExpression = Solver([5, 1, 1, 8])
print(f"Solutions: ", mathExpression.solutions)
