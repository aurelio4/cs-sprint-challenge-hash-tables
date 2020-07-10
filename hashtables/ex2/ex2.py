#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickets_by_source = {}
    route = []

    for ticket in tickets:
        tickets_by_source[ticket.source] = ticket
    
    curr = tickets_by_source["NONE"]

    while 0 < 1:
        route.append(curr.destination)

        if curr.destination == "NONE":
            break

        curr = tickets_by_source[curr.destination]
    
    return route