import math
import random

operation = []
while True:
    op = input("->")
    if op == "=":
        break
    else:
        operation.append(op)

first = operation[0]
if first == "+" or first == "-" or first == "*" or first == "/":
    operation.insert(0, "0")

l = len(operation)

while len(operation) != 1:
    try:
        for op in range(0, len(operation)):
            if operation[op] == "sqrt":
                final = math.sqrt(int(operation[op+1]))
                operation.pop(op)
                operation.pop(op)
                operation.insert(op, str(final))
        for op in range(0, len(operation)):
            if operation[op] == "cu":
                final = float(operation[op-1])*float(operation[op-1])*float(operation[op-1])
                operation.pop(op-1)
                operation.pop(op-1)
                operation.insert(op-1, str(final))
                print(operation)
        for op in range(0, len(operation)):
            if operation[op] == "sq":
                final = float(operation[op-1])*float(operation[op-1])
                operation.pop(op-1)
                operation.pop(op-1)
                operation.insert(op-1, str(final))
                print(operation)
        for op in range(0, len(operation)):
            if operation[op] == "/":
                final = float(operation[op-1]) / float(operation[op+1])
                operation.pop(op-1)
                operation.pop(op-1)
                operation.pop(op-1)
                operation.insert(op-1, str(final))
                print(operation)
        for op in range(0, len(operation)):
            if operation[op] == "*":
                final = float(operation[op-1]) * float(operation[op+1])
                operation.pop(op-1)
                operation.pop(op-1)
                operation.pop(op-1)
                operation.insert(op-1, str(final))
                print(operation)
        for op in range(0, len(operation)):
            if operation[op] == "+":
                if operation[op-2] == "-":
                    final = float(operation[op-1]) - float(operation[op+1])
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.insert(op-1, str(final))
                    print(operation)
                else:
                    final = float(operation[op-1]) + float(operation[op+1])
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.insert(op-1, str(final))
                    print(operation)
        for op in range(0, len(operation)):
            if operation[op] == "-":
                if operation[op-2] == "-":
                    final = float(operation[op-1]) + float(operation[op+1])
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.insert(op-1, str(final))
                    print(operation)
                else:
                    final = float(operation[op-1]) - float(operation[op+1])
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.pop(op-1)
                    operation.insert(op-1, str(final))
                    print(operation)
    except:
        pass

print(operation)