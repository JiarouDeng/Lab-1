#Author: Jiarou Deng dpj5243@psu.edu
#Collaborator: Qingyao Zhu qvz5130@psu.edu
#Collaborator: Brooke Bires bmb6210@psu.edu
#Collaborator: Jimmy Mattison jwm6532@psu.edu

tem = float(input("Enter temperature: "))
u = input("Enter unit in F/f or C/c: ")
if u == "C" or u == "c":
  f= tem*1.8+32;
  print (f"{tem}° in Celsius is equivalent to {f}° Fahrenheit.");
elif u == "F" or u =="f":
  c= (tem-32)/1.8
  print(f"{tem}° in Fahrenheit is equivalent to {c}° Celsius.");
else:
  print(f" Invalid unit({u}).")
 