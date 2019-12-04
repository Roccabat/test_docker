import copy
import numpy as np

class LeftRotation:
    def rotate_table(self, array, rotation_nb):
        array_lenght = len(array)
        # change the rotation number as N rotations for an array of size N just get back to the initial array
        rotation_nb = rotation_nb%array_lenght
        if type(array) == np.ndarray:
            # the copy allows us to handle numpy arrays properly
            returned_array = copy.deepcopy(array)
            returned_array[:array_lenght-rotation_nb],returned_array[array_lenght-rotation_nb:] = array[rotation_nb:],array[:rotation_nb]
            return returned_array
        try:
            array[:array_lenght-rotation_nb],array[array_lenght-rotation_nb:] = array[rotation_nb:],array[:rotation_nb]
            return array
        except:
            print("unsupported format")
            return array

    def rotate(self, initial_array, rotation_nb):
        # if the initial array is a string we want to return a string
        if type(initial_array) == str:
            initial_array = list(initial_array)
            initial_array = self.rotate_table(initial_array,rotation_nb)
            return(''.join(initial_array))
        return(self.rotate_table(initial_array,rotation_nb))