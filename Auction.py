""""


"""
import json


class Auction:

    config = {}
    auctions = []

    def main(self):
        # load configuration file
        self.config = self.read_json("config.json")
        # load list of auction
        self.auctions = self.read_json("input.json")
        finalResult = []
        if len(self.auctions) < 1:
            print(json.dumps(finalResult))
        else:
            # Process of each auction in the auctionList
            for auction in self.auctions:
                result = self.get_highest_bidder(auction)
                if len(result) > 0:
                    finalResult.extend(result)
            self.write_json(finalResult)
            print(finalResult)

    # Get the floor value for the site
    def get_floor_value(self, site):
        result = 0
        for c in self.config["sites"]:
            if c["name"] == site:
                result = float(c["floor"])
                break;
        return result

    # Get adjustment value of the bidder
    def get_adjustment(self, bidder):
        result = 0
        for c in self.config["bidders"]:
            if c["name"] == bidder:
                result = float(c["adjustment"])
                break
        return result

    # Get the list of allowed bidders of particular site
    def get_allowed_bidder(self, site):
        bidders = [];
        for conf in self.config["sites"]:
            if conf["name"] == site:
                bidders = conf["bidders"]
                break
        return bidders

    # Checks where it is a known user
    def is_known_bidder(self, name):
        result = False
        known_bidders = [bidder["name"] for bidder in self.config["bidders"]]
        if name in known_bidders:
            result = True
        return result

    # Read JSON file and returns list of data
    def read_json(self, file):
        data = []
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                f.close()
        except Exception as e:
            pass
        return data

    # Write output to json file
    def write_json(self, data):
        try:
            with open("output.json", 'w+') as f:
                f.write(json.dumps(data))
        except Exception as e:
            print(e)
            pass

    # Finds highest valid bidder per unit for given auction
    def get_highest_bidder(self, auction):
        result = [];
        allowedBidder = self.get_allowed_bidder(auction["site"])
        floor = self.get_floor_value(auction["site"])
        for unit in auction["units"]:
            maxBidValue = 0;
            highestBid = {};
            # make list of bids for given units; filters out units not involved in the auction
            bidsPerUnit = [bid for bid in auction["bids"] if bid["unit"] == unit]
            for bid in bidsPerUnit:
                # filters unknown and invalid bidders
                if bid["bidder"] in allowedBidder and self.is_known_bidder(bid["bidder"]) and floor <= bid["bid"]:
                    adjustment = self.get_adjustment(bid["bidder"])
                    if maxBidValue < (bid["bid"] + adjustment):
                        maxBidValue = bid["bid"]
                        highestBid = bid
            result.append(highestBid)
        return result


if __name__ == "__main__":
    auction = Auction()
    auction.main()