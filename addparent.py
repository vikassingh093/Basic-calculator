class add:
  def __init__(self):
    print "Two number which you want"
   
  def addnumbers(self):
    firstnumber= int(raw_input("first"))
    secondnumber= int(raw_input("second"))
    Sum =  firstnumber + secondnumber
    print "Here's your result" ,Sum

add1 =  add()
add1.addnumbers()
