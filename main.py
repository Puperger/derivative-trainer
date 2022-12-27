import custommath


def main():
    f = open("out/questions.tex", "w")
    g = open("out/answers.tex"  , "w")

    start(f)
    start(g)
    for _ in range(int(input("How many questions? ~"))):
        qs, sol = custommath.getEq()
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

if __name__ == "__main__":
    main()
