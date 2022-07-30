def main():
    file=input("File name:").lower().strip()

    if file.endswith(".gif"):
        print("image/gif")

    elif file.endswith(".pdf"):
        print("application/pdf")

    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")





main()