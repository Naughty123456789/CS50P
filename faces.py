def main():
    x=input("")
    final=convert(x)
    print(final)


def convert(s):
    if ":)" in s:
        return s.replace(":)","🙂")
    if ":(" in s:
        return s.replace(":(","🙁")


if __name__ == "__main__":
    main()
