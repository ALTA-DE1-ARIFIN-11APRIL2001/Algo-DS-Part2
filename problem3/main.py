def playing_domino(hand, deck):
    matching_cards = []

    for card in hand:
        if card[0] == deck[0] or card[1] == deck[0]:
            matching_cards.append(card)

    if not matching_cards:
        return []

    max_sum = max([sum(card) for card in matching_cards])
    recommended_cards = [card for card in matching_cards if sum(card) == max_sum]

    if recommended_cards:
        return recommended_cards
    else:
        return []

# Contoh penggunaan:
print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # Output: [3, 4]
print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [6, 3]))  # Output: [6, 5]
print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))  # Output: []
