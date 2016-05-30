class add:
  firstnumber = 0
  secondnumber = 0
  def __init__(self):
    print "Two number which you want"
   
  def addnumbers(self):
    add.firstnumber= int(raw_input("first"))
    add.secondnumber= int(raw_input("second"))

  def result (self):
    Sum =  add.firstnumber + add.secondnumber
    print "Here's your result" ,Sum

add1 =  add()
add1.addnumbers()
add1.result()
