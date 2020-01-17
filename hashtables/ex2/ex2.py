#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    start = "NONE"

    for t in tickets: # Insert all the tickets into ht as a key/value
        hash_table_insert(hashtable, t.source, t.destination)

    for i in range(length):
        route[i] = hash_table_retrieve(hashtable, start) # Starts by getting the ticket with "NONE" which in turn grabs the next one
        start = route[i] # Sets start to route grabbed above, which is then retrieved again

    return route
