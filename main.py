#Author: Jiarou Deng dpj5243@psu.edu
#Collaborator: Qingyao Zhu qvz5130@psu.edu
#Collaborator: Brooke Bires bmb6210@psu.edu
#Collaborator: Jimmy Mattison jwm6532@psu.edu

tem = input("Enter temperature:")
u = input("Enter unit in F/f or C/c:")
if u == "C" or u == "c":
  f= float(float(tem)/5*9)+32;
  print (f"{tem}° in Celsius is equivalent to {f}°in Fahrenheit.");
elif u == "F" or u =="f":
  c= float(float(tem)-32)/5*9;
  print(f"{tem}° in Fahrenheit is equivalent to {c}° Celsius.");
else:
 print(f"Invalid unit({u}).")
 