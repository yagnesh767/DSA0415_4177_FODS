import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5, 6],
    'location': ['Kanchipuram','Guindy','Guindy','Adambakam','Adambakam','Kanchipuram'],
    'bedrooms': [3,5,4,2,6,6],
    'area_sqft': [1500, 2500, 1800, 1200, 3000,4500],
    'listing_price': [500000, 750000, 600000, 400000, 850000,950000]
}
property_data = pd.DataFrame(data)
average_listing_price = property_data.groupby('location')['listing_price'].mean()
print("Average listing price of properties in each location:")
print(average_listing_price)
num_properties_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]
print("\nNumber of properties with more than four bedrooms:")
print(num_properties_more_than_four_bedrooms)
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nThe property with the largest area:")
print(largest_area_property)
