from collections import defaultdict

def most_popular_toys(toys, n_toys, quotes):

    toys_set = set(toys)
    toys_counter = defaultdict(int)

    for quote in quotes:
        words_in_quote = set(quote.lower().split(" "))
        toys_in_quote = words_in_quote.intersection(toys_set)
        for toy in toys_in_quote:
            toys_counter[toy] += 1

    assert len(quotes) == sum(toys_counter.values())

#    print("toys counter", toys_counter)
#    print(toys_counter.items())
#    print(type(toys_counter.items()))
#    print(list(toys_counter.items()))

    # sort toys counter
    top_toys = sorted(toys_counter.items(), key=lambda x: x[1], reverse = True)

    print("top toys", top_toys)

    if len(top_toys) >= n_toys:
        return [x[0] for x in top_toys[:n_toys]]
    else:
        return [x[0] for x in top_toys[:]]

toys = ["elmo", "batman", "tonka", "nerf", "nfl", "nba", "barbie", "yoda", "chewie", "disney"]
n_toys = 3

quotes = ["I would like a tickle me elmo",
          "Batman is so cool",
          "I gave Tonka as a gift",
          "Not as good as the Nerf I had as a kid",
          "The NFL kiddie football is really nice",
          "Jaden wants an NBA hoop",
          "The dog likes chewing on the Chewie",
          "The cat scratches the Disney pillow",
          "The Barbie Doll House was very desired",
          "The Yoda backpack was very well received",
          "Clifford the Red Dog was more liked than Elmo",
          "She also like the Barbie corvette",
          "Chewie made very fun sounds",
          "The Chewie mask went viral",
          "He chose the Chewie halloween costume",
          "The Barbie for President was sold out"]

print("returned top toys", most_popular_toys(toys, n_toys, quotes))
