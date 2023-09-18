#!/usr/bin/env python3

import json
import os
import requests

url = os.getenv("GRAPHQL_URL")
headers = { 'Content-Type': 'application/json' }

listing_search_payload = "query { listingSearch(filter: { page: 1 pageSize: 250 sort: LIST_PRICE }) { entries { id hotCar priceBadge predictedPriceDifference } totalEntries totalPages } }"
listing_search_response = requests.request("GET", url, headers=headers, data = listing_search_payload)
json_response = json.loads(listing_search_response.text)
entries = json_response.get('data').get('listingSearch').get('entries')
for entry in entries:
	listing_id = entry.get('id')
	print(listing_id)
	listing_details_payload = "query { listingDetails(listingId: \"%s\") { id inventory { id listPrice stockNumber dealer { name address { streetAddress1 city state zipCode } phones { areaCode localNumber phoneType } } } } }"%(listing_id)
	listing_details_response = requests.request("GET", url, headers=headers, data = listing_details_payload)
	print(listing_details_response.text)
