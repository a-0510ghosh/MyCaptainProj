# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:12:43 2023

@author: g_sha
"""

import requests
from bs4 import BeautifulSoup
import pandas

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/"
page_num_MAX = 3
scraped_info_list = []

for page_num in range(1,page_num_MAX):
    url = oyo_url + str(page_num)
    print("get request for:" +url)
    req=requests.get(oyo_url +str(page_num))
    content=req.content
    
    
    soup = BeautifulSoup(content, "html.parser")

    all_hotels= soup.find_all("div",{"class":"hotelCardListing"}) 

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_name=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
        hotel_address=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_price=hotel.find("span",{"class":"listingPrice_finalPrice"}).text
        
        
        try:
            hotel_rating=hotel.find("span",{"class":"hotelRating_ratingSummary"}).text
        except AttributeError:
            pass
        
        
        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})
        
        
        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-smd-textEllipsis"}).text)
            
            
        hotel_dict["name"] = hotel_name
        hotel_dict["address"] = hotel_address
        hotel_dict["price"] = hotel_price
        if "hotel_rating" in locals():
            hotel_dict["rating"] = hotel_rating
        else:
            hotel_dict["rating"] = None
        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
        
        scraped_info_list.append(hotel_dict)
        
dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv", index=False)




