newExp = True
while newExp == True :

  fieldValue = 'test' #raw_input("Enter a field value to alter: ")

  def fieldValueType(fieldValue) :
    try :
      fieldValue = float(fieldValue)
      return fieldValue
    except :
      return fieldValue

  def editSomeText(fieldValue) :
    textExp = '''
    Your field value is: {}
    
    !fieldname![0] returns the first character: {}
    !fieldname![-2] returns the last second-to-last characters: {}
    !fieldname![0:3] returns the first through third characters: {}
    !fieldname!.rstrip() removes all whitespace: {}
    !fieldname!.capitalize() capitalizes the first letter of each word: {}
    !fieldname!.lower() converts all characters to lowercase: {}
    !fieldname!.upper() converts all characters to uppercase: {}
    '''.format(fieldValue, fieldValue[0], fieldValue[-2], fieldValue[0:2], fieldValue.rstrip(), 
      fieldValue.capitalize(), fieldValue.lower(), fieldValue.upper())

    return textExp
    
  def doSomeMath(fieldValue) :
    mathExp = '''
    Your field value is: {}
    
    !fieldname! + 5 adds 5 to the number: {}
    !fieldname! - 6 subtracts 6 from the number: {}
    !fieldname! * 2 multiples the number by two: {}
    !fieldname! / 3 divides the number by three: {}
    round(!fieldname!, 2) rounds the number to two decimal places: {}
    '''.format(fieldValue, fieldValue+5, fieldValue-6, fieldValue*2, fieldValue/3, round(fieldValue, 2))

    return mathExp

  fieldValue = fieldValueType(fieldValue)

  if type(fieldValue) == str :
    textExp = editSomeText(fieldValue)
    print(textExp)
  elif type(fieldValue) == float :
    mathExp = doSomeMath(fieldValue)
    print mathExp

  newExp = False