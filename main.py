from context_free_language import ContextFreeLanguage

if __name__ == "__main__":
    pda = ContextFreeLanguage()
    number_of_rules = int(input("Enter number of rules: "))

    print('Please enter the grammar: ')
    grammar = []
    for i in range(number_of_rules):
        grammar.append(input().strip())

    pda.import_grammar(grammar)
    pda.print_as_pda()

    while True:
        candidate = input("Enter a string to check if it's in the language (or :q to quit): ").strip()
        if candidate == "q":
            break
        print(f"{candidate} is {'NOT ' if not pda.is_in_language(candidate) else ''}in the language.")
