import random


def main():
    f = open("out/questions.tex", "w")
    g = open("out/answers.tex"  , "w")

    start(f)
    start(g)
    for _ in range(int(input("How many questions? ~"))):
        qs, sol = generate_eq()
        f.write(f"\\item ${qs}$")
        g.write(f"\\item ${sol}$")
    end(f)
    end(g)

def start(file):
    file.write("\\documentclass{article}\n\\usepackage[utf8]{inputenc}")
    file.write("\n\\usepackage{multicol}")
    file.write("\n\\begin{document}")
    file.write("\n\\begin{multicols}{2}")
    file.write("\n\\begin{enumerate}")
    return

def end(file):
    file.write("\\end{enumerate}\n\\end{multicols}\n\\end{document}")
    return

def generate_eq():
    qs = ""
    ans= ""
    coefficient, exponent = 0,0
    for i in range(3):
        rnd = random.randint(1,100)
        if rnd < i*40:
            break
        if i>0:
            qs  += "+"
            ans += "+"
        coefficient = random.randint(1,10)
        exponent = random.randint(0,6)
        if exponent == 0:
            qs = qs + str(coefficient)
            ans = ans + "0"
        elif exponent == 1:
            qs = qs + f"{coefficient}x"
            ans = ans + str(coefficient) 
        elif exponent == 2:
            qs = qs + f"{coefficient}x^2"
            ans = ans + f"{2*coefficient}x"
        else:
            qs = qs + f"{coefficient}x^{{{exponent}}}"
            ans = ans + f"{coefficient*exponent}x^{{{exponent-1}}}"
    return qs,ans

if __name__ == "__main__":
    main()
