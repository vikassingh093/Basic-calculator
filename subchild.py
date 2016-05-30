import addparent

class sub(addparent.add):
  
  def subresult(self):
    Sub = sub.firstnumber - sub.secondnumber
    print "Here's is the subtration result" , Sub
  

sub1 = sub()
sub1.addnumbers()
sub1.subresult()
  
