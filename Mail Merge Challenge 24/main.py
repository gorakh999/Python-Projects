with open("Input/Letters/t1.txt", "r") as f:
    content = f.read()
    

namelist = []
with open("Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()
    for i in names:
        namelist.append(i[:-1])
        

print(namelist)
print(content)

  
print(content)

for item in namelist:
    filename = "letter_for_" + item + ".txt"
    message = content.replace("[name]", item)
    path = "Output/ReadyToSend/" + filename

    f = open(f"{path}", 'w')
    f.write(message) 
    f.close()

