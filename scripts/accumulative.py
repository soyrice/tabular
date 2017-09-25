## Based off of example at http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_F3F8CD77A9F647ABBA678A76ADB86E15

## Goal: calculate the percent increase of a numeric field
## Example use case: identify the rate of temperate increase as weather stations move inland
## Steps:
#	1. save the current value as "lastValue"
# 	2. define the value in the next row as "newValue"
#	3. calculate the percent change between the two values

## Example list of field value (replace to try out various numbers):
fieldValue = [50.5, 50.6, 55.7, 60, 70.1]

## Code Block:
lastValue = 0
def percentIncrease(newValue):
    global lastValue
    if lastValue:
        percentage = ((newValue - lastValue) / lastValue)  * 100
    else: 
        percentage = 0
    lastValue = newValue
    return percentage


## Expression:
#	In ArcGIS, the expression will be: 
#	percentIncrease(float(!fieldname!))

#	In a standard Python editor, exclaimation points are uncessary
#		and we have to iterate over each value in the list (ArcGIS does this automatically
#		for the selected field, !fieldname!)
for value in fieldValue :
	percentage = percentIncrease(value)
	print(percentage)