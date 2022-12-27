import random

def getExponents(Sum):
    powers = [i for i in range(7)]
    random.shuffle(powers)
    difficulty = random.randint(1,10) if Sum == 0 else 0
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

def getEq(prod, Sum):
    hasProd=random.randint(0,10) if prod==0 else 0
    qs = ""
    ans = ""
    if hasProd < 8:
        powers = getExponents(Sum)

        for power in powers:
            x,y = makeTerm(power)
            sign = random.choice(["+","-"])
            qs += x + sign
            ans+= y + sign
        qs = qs[:-1]
        ans=ans[:-1]

    if hasProd >= 8:
        storage = ["",""]
        derivatives = ["",""]
        for i in range(2):
            ans,qs = "",""
            qs += "("
            powers = getExponents(Sum)

            for power in powers:
                x,y = makeTerm(power)
                sign = random.choice(["+","-"])
                qs += x + sign
                ans+= y + sign
            qs = qs[:-1]
            ans=ans[:-1]
            qs += ")"
            storage[i]=qs
            derivatives[i]=ans

        qs = storage[0]+storage[1]
        ans = storage[0]+"("+derivatives[1]+")+"+storage[1]+"("+derivatives[0]+")"

    return qs, ans
