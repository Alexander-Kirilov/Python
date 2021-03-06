n = int(input())
pieces = {}

for _ in range(n):
    data = input().split('|')
    pieces[data[0]] = {'composer': data[1], 'key': data[2]}

data = input()

while not data == "Stop":
    splited_data = data.split('|')
    command = splited_data[0]
    if command == "Add":
        piece, composer, key = splited_data[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        piece = splited_data[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        piece, new_key = splited_data[1:]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))

for piece, value in sorted_pieces:
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")
