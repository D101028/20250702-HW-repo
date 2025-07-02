def main():
    userinput = input()
    result = userinput.replace(":)", "🙂").replace(":(", "🙁")
    print(result)

if __name__ == "__main__":
    main()