def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<=len(s)<=6:
        
        for i in range(len(s)):
            if s[0].isalpha() ==False or s[1].isalpha()==False:
                return False
            elif s[i].isdigit():
                if not s[i:].isdigit():
                    return False

                if s[i-1].isalpha() and s[i]== "0":
                    return False

            elif s[i] in ["?","!",".",",",":",";"]:
                return False

        return True


    else:
        return False











main()