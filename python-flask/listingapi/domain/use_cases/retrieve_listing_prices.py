from listingapi.domain import ports


class RetrieveListingPrices:
    def __init__(self, listing_repository: ports.ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing_id: int) -> list[dict]:
        prices = self.listing_repository.get_all_prices(listing_id)
        return prices
