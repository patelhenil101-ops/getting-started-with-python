number = int(input("Enter a number:"))
for i in range(1, number+1):
    binary ="" 
    place = 1
if number == 0:
  binary= '0' 
else:
    while place * 2 <= number:
        place = place * 2
    while place >=1:
        bit = 0
        while number >= place:
            number = number - place
            bit = bit +1
        binary = binary + str(bit)
        place = place//2
print("Binary number:", binary)
            
   
    