from collections import Counter

def count_item_and_sort(items):
    item_counts = Counter(items)

    sorted_items = sorted(item_counts.items(), key=lambda x: x[1])

    result = []

    for item, count in sorted_items:
        result.append(f"{item}->{count}")

    return " ".join(result)

if __name__ == "__main__": 
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"])) 
    # "golang->1 ruby->2 js->4" 
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"])) 
    # "C->1 D->2 B->3 A->4" 
    print(count_item_and_sort(["basketball", "football", "tenis"])) 
    # "basketball->1 football->1 tenis->1"