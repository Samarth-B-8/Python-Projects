#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r"F:\JSS STU\Projects\Python\Python-Projects\Mail-Merge\Input\Names\invited_names.txt") as names_file:
    names = [name.strip() for name in names_file.readlines()]

print(names)

with open(file=r"F:\JSS STU\Projects\Python\Python-Projects\Mail-Merge\Input\Letters\starting_letter.txt", mode="r") as start_letter:
    letter = start_letter.read()

print(letter)

for name in names:
    with open(file=f"F:/JSS STU/Projects/Python/Python-Projects/Mail-Merge/Output/ReadyToSend/{name}.txt", mode="w+") as indv_letter:
        updated_letter = letter.replace("[name]", f"{name}")
        indv_letter.write(updated_letter)
        
