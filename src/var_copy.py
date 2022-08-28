"""
# Copy of immutable and mutable objects #

the '=' operator is used to copy objects. BUT it does not create a new object, it only creates a new variable that share reference to the original object

Mutable objects: means that if we change the value of this object, then the address of this object will not be changed

Immutable object: means that if we change the value of this object, then the address of this object will be changed 

Mutable: list, dictionary, set
Immutable: integer, float, boolean, tuple, string

shallow copy: will create new and independent object with same content
deep copy: creates a new object and recursively adds the copies of nested objects present in the original elements.
"""
import copy

def main():
    print('[INFO] copy example of immutable object:')
    a = 5
    print(f'a before the copy {a}')
    b = a
    print(f"b the copy {b}")
    b = 23
    print(f"new value to b {b}")
    print(f'a after the copy and new value {a}')
    print(f'ID of a {id(a)}')
    print(f'ID of b {id(b)}')    
   
    input("\n[INFO] Press ENTER to continue...\n")

    print("[INFO] copy example of mutable object:")
    A = [[1, 1, 2], [3, 5, 9]]
    print(f'A before the copy {A}')
    B = A
    print(f"B the copy {B}")
    B[1][2] = 8
    print(f'new value to B {B}')
    print(f'A after the copy and new value {A}')
    print(f'ID of A: {id(A)}')
    print(f'ID of B: {id(B)}')

    input("\n[INFO] Press ENTER to continue...\n")

    # shallow copy
    A = [[1, 1, 2], [3, 5, 8]]
    B = copy.copy(A)
    A.append([13, 21, 34])
    print(A)
    print(B)# B is not updated
    ## but not recursive
    C = [[1, 1, 2], [3, 5, 9]]
    D = copy.copy(C)
    C[1][2] = 8
    print(C)
    print(D)# D is updated

    input("\n[INFO] Press ENTER to continue...\n")

    # deep copy
    C = [[1, 1, 2], [3, 5, 9]]
    D = copy.deepcopy(C)
    C[1][2] = 8
    print(C)
    print(D)# D is not updated


if __name__=="__main__":
    main()