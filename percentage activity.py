print("Enter marks obtained in 4 subjects")
math=int(input("Math:"))
english=int(input("English:"))
science=int(input("science:"))
hindi=int(input("hindi:"))

sum = math+english+science+hindi
print("sum of math, english, science, hindi=", sum)

perc = (sum/400)*100

print(end="Percentage mark =")
print(perc)