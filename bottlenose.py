import bottlenose

amazon = bottlenose.Amazon('AKIAJHX3JO2RPYRT6BGA','vA/k1nDIn35Sk/Wk0LlzvsPsb9wfiSTsyOWjtX0H','proyeamazo-21')

xml = amazon.ItemSearch(SearchIndex="VideoGames", ResponseGroup="ItemAttributes, Offers", Keywords="")
