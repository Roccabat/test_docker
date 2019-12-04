from LeftRotation import LeftRotation
import sys

if __name__ == "__main__":
  chaine_de_caractere = sys.argv[1]
  nb_de_rotation = int(sys.argv[2])
  left_rotation = LeftRotation()
  print (left_rotation.rotate(chaine_de_caractere, nb_de_rotation))