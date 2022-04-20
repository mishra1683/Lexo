# tkinter library
from tkinter import*
# regular expression library
import re 
# main window
root = Tk()
# counter for the number of clicks
count = 0
def oneLineLexer(string):
    # print the string
    print(string)
    # if the string contains words or A-Z charachters and a number at the end, then print(identifier)
    if(re.findall(r'[A-Z|a-z]+\d?', string)):
        identifier = re.findall(r'[A-Z|a-z]+\d?', string)
        for iD in identifier:
            #print iD
            if (iD == 'if' or iD == 'for' or iD == 'else' or iD == 'print' or iD ==  'int' or iD=='float'):
                output_window.insert(END, "{key,%s}\n" % iD)
            else:
                output_window.insert(END, "{id,%s}\n" % iD)

    # if the string contains operators: =, +, or >, then print(operator)
    if(re.findall(r'(=|\+|>|<|-)', string)):
        operator = re.findall(r'(=|\+|>|<|-)', string)
        for op in operator:
            output_window.insert(END, "{op,%s}\n" % op)
    # if the string contains literals: numbers, then print(literals)
    if(re.findall(r'[^A-Z|a-z|>|\s][0-9]+', string)):
        literal = re.findall(r'[^A-Z|a-z|>|\s][0-9]+', string)
        for num in literal:
            if num[0] == "=":
                output_window.insert(END, "{num,%s}\n" % num[1:])
            else:
                output_window.insert(END, "{num,%s}\n" % num)

    # if the string contains separators: ;,(),:, "", then print(separators)
    if(re.findall(r'(;|:|\(|\)|\"|\")', string)):
        separator = re.findall(r'(;|:|\(|\)|\"|\")', string)
        for sep in separator:
            output_window.insert(END, "{sep,%s}\n" % sep)
    return

def copyInput():
    global count
    count += 1

    temp = input_window.get("1.0", END)
    textStr = temp
    textList = textStr.split("\n")
    # pass count and textList to outputText:

    outputText(count, textList)
    return
    

#Purpose: Prints the output source onto the output window.
def outputText(count, textList): 
    if count < len(textList):
       # output_window.insert(END, str(textList[count - 1])) + "\n")
        oneLineLexer(str(textList[count - 1]))
        counterLabel.config(text = count)
        #analyzeInput(textList)
    return


# Purpuse: Quits the window
def quitWindow():
    root.destroy()



# center window:
root.title("Lexo: Lexical Analyzer")
root.update_idletasks()
width = 500
height = 500
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry("{}x{}+{}+{}".format(width, height, x, y))
    
# Input Label:
inputLabel = Label(root, text = "Input Source Code:", font=("Arial", 15), fg = "black")
inputLabel.grid(row = 0, column = 0, sticky = W)

# Input Window:
input_window = Text(root, height = 10, width = 28, bg = "white", highlightbackground = "black" )
input_window.grid(row = 1, column = 0, sticky = W)


# Result button:    
result = Button(root, text = "Result", command = copyInput, font=("Arial", 15), relief=RAISED, bg="blue", fg="white")
result.grid(row = 2, pady=5, column = 1, sticky = W)


# Current Line Label:
lineLabel = Label(root, text = "Current Proccessing Line:", font=("Arial", 15), fg = "black")
lineLabel.grid(row = 3, column = 0, pady=10, sticky = W)

# Counter Label:
counterLabel = Label(root, font=("Arial", 15), fg = "red")
counterLabel.grid(row = 3, column = 1,   sticky = W)

# Output Label:
outputLabel = Label(root, text = "Output:",font=("Arial", 15), fg = "green")
outputLabel.grid(row = 0, column = 1, sticky = W)

# Output Window:
output_window = Text(root, height = 10, width = 30, bg = "white", highlightbackground = "black" )
output_window.grid(row = 1, column = 1, sticky = E)

# Keys
infoLabel = Label(root, text="id means identifiers", font=("Arial", 12), fg = "blue")
infoLabel.grid(row = 4, column = 0,  sticky = W)

infoLabel1 = Label(root, text="op means operators", font=("Arial", 12), fg = "brown")
infoLabel1.grid(row = 5, column = 0,  sticky = W)

infoLabel2 = Label(root, text="num means numerals", font=("Arial", 12), fg = "grey")
infoLabel2.grid(row = 6, column = 0, sticky = W)

infoLabel3 = Label(root, text="key means keywords", font=("Arial", 12), fg = "navy blue")
infoLabel3.grid(row = 7, column = 0, sticky = W)

infoLabel3 = Label(root, text="sep means seperator", font=("Arial", 12), fg = "red")
infoLabel3.grid(row = 8, column = 0, sticky = W)

# run main
root.mainloop()