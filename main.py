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
    coefficient = random.randint(1,10)
    exponent = random.randint(0,10)
    if exponent == 0:
        return coefficient,0
    if exponent == 1:
        return f"{coefficient}x",coefficient 
    if exponent == 2:
        return f"{coefficient}x^2",f"{2*coefficient}x" 
    return f"{coefficient}x^{{{exponent}}}",f"{coefficient*exponent}x^{{{exponent-1}}}" 
if __name__ == "__main__":
    main()
