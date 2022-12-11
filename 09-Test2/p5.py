def f(first_letter,last_letter):
    import re
    file=open("test.txt","r",encoding="utf-8",newline="")
    plik=file.read()

    code=r"\b"+first_letter+r"[a-z]*"+last_letter+r"\b"

    find=re.findall(code,plik)

    result=len(find)
    print(find)
    print(result)

    file.close()

    return result
        

f("w","d")