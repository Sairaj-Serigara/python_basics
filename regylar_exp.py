# regexr website
import re
pattern=r"[A-Z]+ummy"
text="""Lorem Ipsum is simply Dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy 
text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Summy it has survived not
 only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s 
 with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
 PageMaker including versions of Lorem Ipsum
"""
# macth=re.search(pattern,text)
# print(macth)

matches=re.finditer(pattern,text)
for i in matches:
    # print(i)
    print(i.span())