from listingapi.adapters.sql_alchemy_listing_repository.models import (
    ListingModel,
    PriceModel,
)
from listingapi.domain import entities


class ListingMapper:
    @staticmethod
    def from_entity_to_model(listing: entities.ListingEntity) -> ListingModel:
        listing_model = ListingModel(
            name=listing.name,
            street_address=listing.postal_address.street_address,
            postal_code=listing.postal_address.postal_code,
            city=listing.postal_address.city,
            country=listing.postal_address.country,
            description=listing.description,
            building_type=listing.building_type,
            price=listing.latest_price_eur,
            surface_area_m2=listing.surface_area_m2,
            rooms_count=listing.rooms_count,
            bedrooms_count=listing.bedrooms_count,
            contact_phone_number=listing.contact_phone_number,
        )
        return listing_model

    @staticmethod
    def from_model_to_dict(listing: ListingModel) -> dict:
        listing_dict = {
            "id": listing.id,
            "name": listing.name,
            "postal_address": {
                "street_address": listing.street_address,
                "postal_code": listing.postal_code,
                "city": listing.city,
                "country": listing.country,
            },
            "description": listing.description,
            "building_type": listing.building_type,
            "latest_price_eur": listing.price,
            "surface_area_m2": listing.surface_area_m2,
            "rooms_count": listing.rooms_count,
            "bedrooms_count": listing.bedrooms_count,
            "contact_phone_number": listing.contact_phone_number,
            "created_date": listing.created_date.isoformat(),
            "updated_date": listing.updated_date.isoformat(),
        }
        return listing_dict


class PriceMapper:
    @staticmethod
    def from_entity_to_model(price: entities.PriceEntity) -> dict:
        price_model = PriceModel(
            listing_id=price.listing_id,
            price=price.price_eur,
        )

        return price_model

    @staticmethod
    def from_model_to_dict(price: PriceModel) -> dict:
        price_dict = {
            "price_eur": price.price,
            "created_date": price.created_date.isoformat(),
        }
        return price_dict
