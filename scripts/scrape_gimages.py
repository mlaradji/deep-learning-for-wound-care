# Obtained from https://github.com/DtCarrot/sg-food-ml.

no_images_per_class = 100

import os

# Define scraper
import time
from google_images_download import google_images_download   #importing the library
response = google_images_download.googleimagesdownload()   #class instantiation
def scrape_images(keyword_list):
    for keyword in keyword_list:
        arguments = {
            "keywords": keyword, 
            "limit": no_images_per_class, 
            "print_urls": True,
            "chromedriver": 'drivers/chromedriver',
        }
        paths = response.download(arguments)
        #print(paths)
        # Set a delay
        time.sleep(5)


# Engine to scrap images
wound_dict = {
  'abdominal_wounds': 'abdominal wound',
  'burns': 'burn wound',
  'epidermolysis_bullosa': 'epidermolysis bullosa',
  'extravasation_wound_images': 'extravasation wound',
  'foot_ulcers': 'foot ulcer',
  'haemangioma': 'haemangioma',
  'leg_ulcer_images': 'leg ulcer',
  'malignant_wound_images': 'malignant wound',
  'meningitis': 'meningitis',
  'miscellaneous': 'miscellaneous',
  'orthopaedic_wounds': 'orthopaedic wound',
  'pilonidal_sinus': 'pilonidal sinus',
  'pressure_ulcer_images_a': 'pressure ulcer',
  'pressure_ulcer_images_b': 'pressure ulcer',
  'toes': 'toe wound'
}

wound_list = wound_dict.values()

if __name__ == "__main__":
    # Loop through the list of images
    scrape_images(wound_list)
