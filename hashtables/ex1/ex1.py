#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    for i in range(len(weights)):
        if hash_table_retrieve(ht,limit - weights[i]) is not None: # Checks ht if there is a key that has the remaning sum
            return [i , hash_table_retrieve(ht, limit - weights[i])] # If limit is reach with the 2 keys, it gets return
        hash_table_insert(ht, weights[i], i) # If the limit is not reached, insert new key/value for the next loop to reference
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")