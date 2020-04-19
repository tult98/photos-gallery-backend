from photos.models import Photo
import csv

with open('clean_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Photo(url=row['image_url'])
        p.save()