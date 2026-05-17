import pytest
from JenkinsTesting import realfile as rf

def testmath():
   assert rf.addtwonums(1,2) == 3