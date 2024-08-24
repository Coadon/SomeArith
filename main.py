import random as r
import time
import os

SAY_OPTIONS = "-v Tingting"
# SAY_OPTIONS = ""

q_total_num = int(input("Number of questions: ") or 50)
q_operand1_max = 9 * 10 ** (int(input("Operand1 digits: ") or 1)-1)
q_operand2_max = 9 * 10 ** (int(input("Operand2 digits: ") or 1)-1)

problems = []

# Addition Only for Now

for i in range(0, q_total_num):
    o1 = r.randint(0, q_operand1_max)
    o2 = r.randint(0, q_operand2_max)
    problems.append({
        "o1":   str(o1),
        "o2":   str(o2),
        "ans":  str(o1 + o2)})

for i, p in enumerate(problems):
    os.system(f"say {SAY_OPTIONS} \" {p['o1']} plus {p['o2']} \"")
    time.sleep(7)

input("PRESS RETURN")
os.system(f"say {SAY_OPTIONS} \"ANSWERS\"")

for i, p in enumerate(problems):
    os.system(f"say {SAY_OPTIONS} \"{p['ans']}\"")
