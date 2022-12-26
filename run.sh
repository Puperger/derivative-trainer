#!/bin/bash

#Run the program
python3 main.py

#Compile the LaTeX files
cd out
pdflatex questions.tex
pdflatex answers.tex
cd ..
