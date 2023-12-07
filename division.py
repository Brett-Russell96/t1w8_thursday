# try except block - try catch block

class NegativeError(Exception):
    pass


try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n < 0 or d < 0:
        raise NegativeError("No Negative numbers please")

    q = n / d

    print(q)

# except Exception as e: # converts exception to variable e
#     print(type(e)) # type will express the type of exception caught
#     print("Denominator cannot be zero")
except ZeroDivisionError:
    print("Denominator cannot be zero")
# better practice to express expected exceptons.
except ValueError:
    print("please type numbers only")

except NegativeError:
    print("Please don't input negative numbers")

except Exception as e:
    print(e)
    print("Something went wrong")

else:
    # whenever try block is successfully executed without throwing any exceptions.
    print("I am else block")

finally:
    # this will run at the end regardless of whether an error is thrown
    print("I am finally block")




print("The end of the program")


# file handling example
# try:
    # open a file
    # try to do something
    # write into the file - it may throw error
    # close file
# except:
    # do something to handle the error
# finally:
    # close the file
