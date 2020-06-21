from guizero import App, Text, PushButton
app = App("SWECOE GUI Prototype Build 1")
text = Text(app)

def Button1():
    text.value = """June 21, 2020
https://github.com/isthisausername125/SWECOE"""
    
A = PushButton(app, text="About", command=Button1)

app.display()

