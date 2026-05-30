#File: initials.py
#Description: Print out my initials
#Assignment Number: 2
#
#Name: Charity-Ann Nana Yaa Asiedu-Akrofi
#Student ID: 2425402332
#Email: 2425402332@live.gctu.edu.gh
#Grader: Augustus Buckman
#
#On my honor, Charity-Ann Asiedu-Akrofi, this programming assignment is my own work
#and I have not provided this code to any other student.


def main():
    # Print initials in small and large stylized block letters using only print and strings
    # Layout: 3dots | 12-char letter | 3 dots | period block | 3 dots | 12-char letter | 3 dots |
    # period block | 3 dots | 12-char letter | 3 dots | period block
    # No trailing spaces on any line

    print()
    print("...CNA")
    print()

    # --- C block (12 chars wide x 10 tall) ---
    c1 = "..CCCCCCCC.."
    c2 = ".CCCCCCCCCC."
    c3 = "CC.........."
    c4 = "CC.........."
    c5 = "CC.........."
    c6 = "CC.........."
    c7 = "CC.........."
    c8 = "CC.........."
    c9 = ".CCCCCCCCCC."
    c10= "..CCCCCCCC.."

    # --- N block (12 chars wide x 10 tall) ---
    n1 = "N..........N"
    n2 = "NN.........N"
    n3 = "N.NN.......N"
    n4 = "N..NN......N"
    n5 = "N...NN.....N"
    n6 = "N....NN....N"
    n7 = "N......NN..N"
    n8 = "N.......NN.N"
    n9 = "N.........NN"
    n10= "N.........NN"

    # --- A block (12 chars wide x 10 tall) ---
    a1 = ".....AAA...."
    a2 = "...AA..AA..."
    a3 = "..AA....AA.."
    a4 = ".AA......AA."
    a5 = "AAAAAAAAAAAA"
    a6 = "AA........AA"
    a7 = "AA........AA"
    a8 = "AA........AA"
    a9 = "AA........AA"
    a10= "AA........AA"

    # --- Period block ( 2 chars wide x 10 tall) ---
    p1 = ".."
    p2 = ".."
    p3 = ".."
    p4 = ".."
    p5 = ".."
    p6 = ".."
    p7 = ".."
    p8 = ".."
    p9 = "**"
    p10= "**"

    print("..." + c1 + "..." + p1 + "..." + n1 + "..." + p1 + "..." + a1 + "..." + p1)
    print("..." + c2 + "..." + p2 + "..." + n2 + "..." + p2 + "..." + a2 + "..." + p2)
    print("..." + c3 + "..." + p3 + "..." + n3 + "..." + p3 + "..." + a3 + "..." + p3)
    print("..." + c4 + "..." + p4 + "..." + n4 + "..." + p4 + "..." + a4 + "..." + p4)
    print("..." + c5 + "..." + p5 + "..." + n5 + "..." + p5 + "..." + a5 + "..." + p5)
    print("..." + c6 + "..." + p6 + "..." + n6 + "..." + p6 + "..." + a6 + "..." +p6)
    print("..." + c7 + "..." + p7 + "..." + n7 + "..." + p7 + "..." + a7 + "..." + p7)
    print("..." + c8 + "..." + p8 + "..." + n8 + "..." + p8 + "..." + a8 + "..." + p8)
    print("..." + c9 + "..." + p9 + "..." + n9 + "..." + p9 + "..." + a9 + "..." + p9)
    print("..." + c10 + "..." + p10 + "..." + n10 + "..." + p10 + "..." + a10 + "..." + p10)

    print()

main()
