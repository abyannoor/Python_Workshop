# Casting
# Change data type  to another type
# data type = int, float, str, boolean


print("=================CHANGE DATA INTEGER======================")
## Data Integer
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))

# Integer to Float
data_float = float(data_int)

# Integer to String
data_str = str(data_int)

# Integer to Boolean
# if the value is 0 then "false", else "True"
data_bool  = bool(data_int) 
 
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))






print("=================CHANGE DATA FLOAT========================")
## Data Float
data_float = 0; #sembilan,lima fm 
print("data = ", data_float, ",type =",type(data_float))

# Float to Integer
data_int = int(data_float) # Dibulatkan ke bawah

# Float to String
data_str = str(data_float)

# Float to Boolean
# if the value is 0 then "false", else "True"
data_bool  = bool(data_float) 
 
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))




print("=================CHANGE DATA BOOLEAN======================")
## Data Boolean
data_bool = True;
print("data = ", data_bool, ",type =",type(data_bool))

# Boolean to Integer
data_int = int(data_bool)

# Boolean to String
data_str = str(data_bool)

# Boolean to Float
data_float  = float(data_bool) 
 
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))




print("=================CHANGE DATA STRING=======================")
## Data String
data_str = "10";
print("data = ", data_str, ",type =",type(data_str))

# String to Integer
# String must be a number
data_int = int(data_str)

# String to Boolean
# if the string is 0 then "false", else "True"
data_bool = bool(data_str)

# String to Float
# String must be a number
data_float  = float(data_str) 
 
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_bool, ",type =",type(data_bool))
print("data = ", data_float, ",type =",type(data_float))