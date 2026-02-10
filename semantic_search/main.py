from scripts.semantic_search import main

while True:
    print("\n1. Semantic Search")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        main(input("Query: "))
    else:
        break
