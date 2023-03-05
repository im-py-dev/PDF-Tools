#!/usr/bin/env python
# coding: utf-8
# AUTHOR : ImPyDev

import time
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_file():
    # Get the current directory
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Get a list of all files in the directory
    files = os.listdir(dir_path)

    # Filter the list to only show txt files
    txt_files = [f for f in files if f.endswith('.txt')]

    # Show the user the available txt files
    print("Available txt files:")
    for i, f in enumerate(txt_files):
        print(f"{i + 1}. {f}")

    # Ask the user to choose a file
    choice = 1
    try:
        choice = int(input("Enter the number of the file you want to choose: "))
        if choice < 1:
            print("Choosing [1]")
    except ValueError:
        convert_file()

    # Get the chosen file name
    chosen_file = txt_files[choice - 1]

    print(f"You have chosen {chosen_file}.")

    file = open(chosen_file, "r")

    # create a new PDF file
    pdf = canvas.Canvas(f'{chosen_file}.pdf', pagesize=letter)

    # read the text file
    with open(chosen_file, 'r') as f:
        text = f.read()

    # split the text into paragraphs and add them to the PDF
    paragraphs = text.split('\n\n')
    for i, paragraph in enumerate(paragraphs):
        y = 750 - i * 20
        pdf.drawString(100, y, paragraph)

    # save the PDF file
    pdf.save()

    # pdf = FPDF()
    # pdf.add_page()
    # for text in file:
    #     if len(text) <= 20:
    #         pdf.set_font("Arial", "B", size=18)  # For title text
    #         pdf.cell(w=200, h=10, txt=text, ln=1, align="C")
    #     else:
    #         pdf.set_font("Arial", size=15)  # For paragraph text
    #         pdf.multi_cell(w=0, h=10, txt=text, align="L")
    # pdf.output(f"{chosen_file}.pdf")

    print("Successfully converted!")


def exit_program():
    quit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def author():
    print("DEVELOPED BY ImPyDev")
    print("Github.com/ImPyDev\n")


def menu():
    author()
    options_dict = {
        '1': convert_file,
        '0': exit_program,
    }
    option = input(
        """1. Pdf To Text
0. Exit

Enter Choice : 
""")
    fanc = options_dict.setdefault(option, program)
    fanc()


def program():
    try:
        menu()
    except KeyboardInterrupt:
        con = input("\n\n [c] Continue [q] Quit : ")
        if con == "c" or con == "C" or con == "continue" or con == "Continue":
            menu()
        else:
            exit()


if '__main__' == __name__:
    program()
