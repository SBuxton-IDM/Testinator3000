import re
import sys
def countFuncLength(fileName):
    fname = fileName
    countDict = {}
    currentFunction = "StartingLines"
    countDict[currentFunction] = 0
    with open(fname, 'r') as f:
        for line in f:
            if "def" in line:
                currentFunction = line.replace("def ", "")
                currentFunction = currentFunction.replace("():\n", "")
                countDict[currentFunction] = 0
            elif line != "\n":
                # Checking for comments
                if not ("#" in line and re.search(r'(.*)\#', line) == None):
                    countDict[currentFunction]+=1
            
        print("Here is your length report: \n")
        for key in countDict:
            print(f"   {key}: {countDict[key]} \n")

def tracefunc(frame, event, arg, indent=[0]):
      if event == "call":
          indent[0] += 2
          print("-" * indent[0] + "> call function", frame.f_code.co_name)
      elif event == "return":
          print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
          indent[0] -= 2
      return tracefunc

# Usage example
print("Here is your function report: ")
sys.setprofile(tracefunc)
countFuncLength("test_analysis.py")
