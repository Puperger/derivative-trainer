#!/bin/bash

#Create output dir
mkdir -p out

#Run the program
python3 main.py
echo "created questions"

#Compile the LaTeX files
cd out
pdflatex questions.tex > NUL 2>&1
echo "questions.pdf has been generated"
pdflatex answers.tex > NUL 2>&1
echo "answers.pdf has been generated"
cd ..
