saarc = ["Bangladesh", "Afganisthan", "Bhutan", "Nepal", "India", "Pakistan", "Srilanka"]

country = input("Enter the name of your country: ")

if country in saarc:
    print(country , "is a member of SAARC")

else: 
    print(country , "is not a member of SAARC");
    

print("Program terminated")