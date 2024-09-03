test_file = open("test.txt","a")

print("OLÁ, COMO VOCÊ ESTÁ?\n Estou bem!",file=test_file)

test_file.write("Eu sou o GAbriel")
test_file.close()