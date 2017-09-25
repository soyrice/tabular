## Based off of example at http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_11EAB368A53B4D1C9618A58A1B09F9D0

## Goal: reclassify a numeric field
## Example use case: convert a lake's dissolved oxygen measurements into four categories of species habitability
## Steps: 
#	1. if the field value is between 0 and 10, reclassify field with the value 1
# 	2. if the field value is between 10 and 20, reclassify field with the value 2
#	3. if the field value is between 20 and 30, reclassify field with the value 3
#	4. if the field value is between 30 and 40, reclassify field with the value 4

## Example field value (replace to try out various numbers):
fieldValue = 31

## Code Block:
def Reclass(fieldValue):
    if (fieldValue >= 0 and fieldValue <= 10):
        return 1
    elif (fieldValue > 10 and fieldValue <= 20):
        return 2
    elif (fieldValue > 20 and fieldValue <= 30):
        return 3
    elif (fieldValue > 30):
        return 4

## Expression:
#	In ArcGIS, the expression will be: 
#	Reclass(!fieldValue!)

#	In a standard Python editor, exclaimation points are uncessary:
category = Reclass(fieldValue)
print(category)

