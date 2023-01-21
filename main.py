import generate

def main():
    works = False
    count = 0
    while works == False:
        works = generate.generate()
        count += 1
        print(count)
    print(count)


if __name__ == "__main__":
    main()

