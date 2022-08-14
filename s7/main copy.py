from packageF1.Pilote import *

A = Pilote("A", "Mercedes")
B = Pilote("B", "RedBull")
C = Pilote("C", "Ferrari")
D = Pilote("D", "McLaren")
E = Pilote("E", "Alpine")
F = Pilote("F", "AlphaTauri")
G = Pilote("G", "AstonMartin")
H = Pilote("H", "Williams")
I = Pilote("I", "AlfaRomeo")
J = Pilote("J", "Haas")
K = Pilote("K", "Mercedes")
L = Pilote("L", "RedBull")
M = Pilote("M", "Ferrari")
N = Pilote("N", "McLaren")
O = Pilote("O", "Alpine")
P = Pilote("P", "AlphaTauri")
Q = Pilote("Q", "AstonMartin")
R = Pilote("R", "Williams")
S = Pilote("S", "AlfaRomeo")
T = Pilote("T", "Haas")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
c = ['R', 'N', 'L', 'O', 'P', 'A', 'I', 'J', 'Q', 'D', 'H', 'E', 'S', 'T', 'K', 'C', 'F', 'B', 'G', 'M']

#sort randomly a list of pilots
from random import shuffle

shuffle(alphabet)
print(alphabet)