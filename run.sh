#!/usr/bin/env -S bash -Eeuo pipefail

#Create output dir
mkdir -p out

#Run the program
python3 main.py
echo "created questions"

#Compile the LaTeX files
cd out
pdflatex questions.tex >&/dev/null
echo "questions.pdf has been generated"
pdflatex answers.tex >&/dev/null
echo "answers.pdf has been generated"
cd ..
