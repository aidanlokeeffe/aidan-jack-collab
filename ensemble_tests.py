from Ensemble import Ensemble

test_mat = [[0,1,1,0,0,1,0],
            [0,0,0,0,0,1,1],
            [0,1,0,0,1,0,1],
            [1,0,1,0,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,1,1,0,0],
            [1,0,0,0,1,0,0]]

ensemble = Ensemble(test_mat)

# Just making sure the initialization works as intended
'''
print(ensemble.ensemble)
print(ensemble.N)
print(ensemble.seed)
print(ensemble.num_iter)
'''
# all seems to be in order


# test out scrambling
test_mat2 = [ [ test_mat[i][j] for j in range(7) ] for i in range(7) ]

for i in range(7):
    print(test_mat2[i])
print("\n")

ensemble.rewire(test_mat2)
for i in range(7):
    print(test_mat2[i])
print("\n")
# Seems to work well


# Test out adding an element to the ensemble
ensemble.new_member()
for i in range(7):
    print(ensemble.members[0][i])
print("\n")
# Amazing, it really does preserve in- and out-degrees


# Testing out making a whole ensemble
ensemble = Ensemble(test_mat)
ensemble.create_members(100)
print("Printing an entire ensemble")
for member in ensemble.members:
    for i in range(7):
        print(member[i])
    print("\n")














