def split_by_lines(text: str):
    words = text.split(" ")
    characters = 0
    for word in words:
        characters = max(characters, len(word))

    characters += 4
    print("*"*characters)

    for word in words:
        print(f"* {word}{' '*(characters - len(word)-3)}*")

    print("*"*characters)


if __name__ == "__main__":
    split_by_lines(text="¿Qué te parece el reto?")
