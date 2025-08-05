def is_prime(num):
    if num % 1 == 0 and num % num ==0 and num%5 == 0 :
        return "False"
    elif num % 1 == 0 and num % num ==0:
        print("True")
    else:
        print("False")

print(is_prime(75))