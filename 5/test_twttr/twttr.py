def main():
    word = input('Input: ')
    twttr = shorten(word)
    print(twttr)

def shorten(word):
    output = ''
    for i in range(len(word)):
        if word[i].lower() in 'aeiou':
            continue
        output += word[i]
    return output

if __name__ == "__main__":
    main()
