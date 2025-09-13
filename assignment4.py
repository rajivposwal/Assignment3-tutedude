#assignment 4
#task 1 Read a file and handle errors 
'''
try:
    with open("sample.txt","r")as file:

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error : The file 'sample.txt' does not exist.")

except Exception as e:
    print("An unexpected error occurred:",e)'''

#task 2 
user_input = input("Enter some text to write into the file: ")

with open("myfile.txt", "w") as file:
    file.write(user_input + "\n")

print("data written to output text")

extra_input = input("Enter a additional text to append: ")

with open ("output.txt","a") as file:
    file.write(extra_input + "\n")

print("Additional data append to output.txt")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
    