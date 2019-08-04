#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    diff = []
    for i in weights:
        diff.append(limit-i)

    ans = []

    for i in diff:
        if hash_table_retrieve(ht, i) != None:
            ans.append(i)
    
    if len(ans) == 2:
        ans.sort()
        x = hash_table_retrieve(ht, ans[0])
        y = hash_table_retrieve(ht, ans[1])
        if x == y:
            indices = [i for i, x in enumerate(weights) if x == ans[0]]
            return (indices[1], indices[0])
        if x > y:
            return (x, y)
        else:
            return (y, x)
    else:
        return None




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
# print(answer_3[0]==3)


