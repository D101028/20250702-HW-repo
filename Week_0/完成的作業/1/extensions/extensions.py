userinput = input("File name: ")

ext = userinput.split(".")[-1].lower()

if ext in ("gif", "jpg", "jpeg", "png"):
    print(f"image/{ext}")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/txt")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
