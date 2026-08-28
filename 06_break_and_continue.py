
print("this is a 'break' statement and stops at 11 -->") 
for i in range(0, 21):
    print(i)
    if i == 11:
        break # cancel the execution of the loop 


print("this is a 'continue' statement and skips #10 -->")

for i in range(1, 20):
    if i == 10:
        continue # continue the loop for the next interation here itself, i.e., skip the code below and resume loop
    print(i)