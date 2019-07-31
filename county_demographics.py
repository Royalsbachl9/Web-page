import county_demographics
import numpy as np
demographicFile = open("./county_demographics.db")
demographicData = db.load(demographicFile)

demographicFile.close()

list_of_report = county_demographics.get_all_counties(test=True)
