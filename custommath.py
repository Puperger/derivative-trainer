import random

def getExponents():
    powers = [i for i in range(7)]
    random.shuffle(powers)
    difficulty = random.randint(1,10)
    if difficulty < 5: terms = 1
    else: terms = 2 if difficulty < 8 else 3
    powers = powers[0:terms]
    powers.sort()
    powers.reverse()
    return powers

def makeTerm(power):
    coef = random.randint(1,10)
    if power == 0:
        return str(coef), "0"
    if coef == 1 and power == 1:
        return "x", "1"
    if coef == 1 and power == 2:
        return "x^2", "2x"
    if power == 1:
        return f"{coef}x",str(coef)
    if coef == 1:
        return f"x^{{{power}}}",f"{power}x^{{{power-1}}}"
    if power == 2:
        return f"{coef}x^2", f"{2*coef}x"
    return f"{coef}x^{{{power}}}",f"{coef*power}x^{{{power-1}}}"

def getEq():
    powers = getExponents()
    qs = ""
    ans = ""
    for power in powers:
        x,y = makeTerm(power)
        qs += x + "+"
        ans+= y + "+"
    qs = qs[:-1]
    ans=ans[:-1]
    return qs, ans
