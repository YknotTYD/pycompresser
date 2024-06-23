import browser
from pycompresser import Compresser

def change_link_to(data):
    browser.document["link"].href="data:text/plain;charset=utf-8,"+browser. window.encodeURIComponent(data)

def update_link():

    text=str(browser.document["aqua"].value.result)
    old_lenght=len(text.encode("utf-8"))

    text=Compresser.compile(text)
    new_lenght=len(text.encode("utf-8"))
    
    change_link_to(text)

    browser.document["blue0"].textContent=f"{old_lenght:,}".replace(",","_")
    browser.document["blue1"].textContent=f"{new_lenght:,}".replace(",","_")
    browser.document["blue2"].textContent="-"+str(round(100-(new_lenght/old_lenght)*100,3))+"%"
    
    browser.document["linkl"].style.display="flex"
    
def aqua(event):

    if not hasattr(browser.document["aqua"],"value"):
        return(None)
    
    browser.document["linkl"].style.display="none"
    browser.window.setTimeout(update_link(),1)
    
browser.document["button"].onclick=aqua