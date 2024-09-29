        
def rev_num(num):
  return int(str(num)[::-1])
while True:
  number = input("Enter a five-digit number: ")
  
  if len(number) == 5 and number.isdigit():
    num = int(number)
    rev_num = rev_num(num)
    
    if num == rev_num:
        print(f"The original number {num} and the reversed number {rev_num} are equal.")
    else:
        print(f"The original number {num} and the reversed number {rev_num} are not equal.")
    break
else:
  print("Please enter a valid five-digit number.")       
  
