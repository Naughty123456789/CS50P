def main():
    x=input("")
    final=convert(x)
    print(final)


def convert(s):

    return s.replace(":)","🙂").replace(":(","🙁")




if __name__ == "__main__":
    main()
