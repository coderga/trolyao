
text = "tìm trên youtube trợ lý ảo"
dsCanXoa = ["youtube","tìm","trên"]
def replaceToSpace(text,dsCanXoa):
    for stri in dsCanXoa:
        text = text.replace(stri,"")
    return text

newText = replaceToSpace(text,dsCanXoa)
print(newText)