def humanize(txt):
    #allowed_chars = {"0","1","2","3","4","5","6","7","8","9","-","=","+","/","*"," "}
    finaltext=''
    splittxt=txt.replace(" ","")
    cleantxt=splittxt
    allowed = "0123456789-+*/= "
    for char in allowed:
        cleantxt = cleantxt.replace(char,"")
    if len(cleantxt)==0:
        splittxt = splittxt.replace("=", " equals ")
        splittxt = splittxt.replace("+", " plus ")
        splittxt = splittxt.replace("-", " minus ")
        splittxt = splittxt.replace("*", " times ")
        splittxt = splittxt.replace("/", " divided by ")
        splittxt = splittxt.split()
        for piece in splittxt:
            if piece.isdigit():
                piece = numeric(piece)
            else:
                piece = piece + ' '
            finaltext = finaltext + piece
    else:
        return ("invalid input")
    return finaltext

def numeric(num):
    numbers = {2 : '',
               5 : 'thousand ',
               8 : 'million ',
               11 : 'billion ',
               14 : 'trillion ',
               17 : 'quadrillion ',
               20 : 'quintillion ',
               23 : 'sextillion ',
               26 : 'septillion '}
    ln=len(str(num))
    d=0
    text=''

    if num == '0':
        text = 'zero '
    else:
        while d<ln:
            if (d-ln)%3==0:
                if num[d]=='1':
                    text=text + "one hundred "
                if num[d]=='2':
                    text=text + "two hundred "
                if num[d]=='3':
                    text=text + "three hundred "
                if num[d]=='4':
                    text=text + "four hundred "
                if num[d]=='5':
                    text=text + "five hundred "
                if num[d]=='6':
                    text=text + "six hundred "
                if num[d]=='7':
                    text=text + "seven hundred "
                if num[d]=='8':
                    text=text + "eight hundred "
                if num[d]=='9':
                    text=text + "nine hundred "
                d=d+1
            else:
                if ((num[d] == '0') and (num[d+1] != '0')):
                    if ((num[d-1] > '0') and (d>0)):
                        text = text + "and "
                    if num[d+1] == '1':
                        text = text + "one "
                    if num[d+1] == '2':
                        text = text + "two "
                    if num[d+1] == '3':
                        text = text + "three "
                    if num[d+1] == '4':
                        text = text + "four "
                    if num[d+1] == '5':
                        text = text + "five "
                    if num[d+1] == '6':
                        text = text + "six "
                    if num[d+1] == '7':
                        text = text + "seven "
                    if num[d+1] == '8':
                        text = text + "eight "
                    if num[d+1] == '9':
                        text = text + "nine "
                if (num[d] != '0'):
                    if (d>0) and (int(num[d-1])) in range(1,9):
                        text = text + "and "
                    q=(ln % 3)
                    if (num[d]=='1') and not (((ln % 3) == 1) and (d == 0)):
                        if num[d+1]=='0':
                            text = text + "ten "
                        if num[d+1]=='1':
                            text = text + "eleven "
                        if num[d+1]=='2':
                            text = text + "twelve "
                        if num[d+1]=='3':
                            text = text + "thirteen "
                        if num[d+1]=='4':
                            text = text + "fourteen "
                        if num[d+1]=='5':
                            text = text + "fourteen "
                        if num[d+1]=='6':
                            text = text + "sixteen "
                        if num[d+1]=='7':
                            text = text + "seventeen "
                        if num[d+1]=='8':
                            text = text + "eighteen "
                        if num[d+1]=='9':
                            text = text + "nineteen "
                    elif((d!=0)or((d-ln-1)%3==0)):
                        if num[d] == '2':
                            text = text + 'twenty'
                        if num[d] == '3':
                            text = text + 'thirty'
                        if num[d] == '4':
                            text = text + 'forty'
                        if num[d] == '5':
                            text = text + 'fifty'
                        if num[d] == '6':
                            text = text + 'sixty'
                        if num[d] == '7':
                            text = text + 'seventy'
                        if num[d] == '8':
                            text = text + 'eighty'
                        if num[d] == '9':
                            text = text + 'ninety'
                        if num[d + 1] == '0':
                            text = text + " "
                        if num[d + 1] == '1':
                            text = text + "-one "
                        if num[d + 1] == '2':
                            text = text + "-two "
                        if num[d + 1] == '3':
                            text = text + "-three "
                        if num[d + 1] == '4':
                            text = text + "-four "
                        if num[d + 1] == '5':
                            text = text + "-five "
                        if num[d + 1] == '6':
                            text = text + "-six "
                        if num[d + 1] == '7':
                            text = text + "-seven "
                        if num[d + 1] == '8':
                            text = text + "-eight "
                        if num[d + 1] == '9':
                            text = text + "-nine "
                    elif(d==0):
                        d=d-1
                        if num[d + 1] == '1':
                            text = text + "one "
                        if num[d + 1] == '2':
                            text = text + "two "
                        if num[d + 1] == '3':
                            text = text + "three "
                        if num[d + 1] == '4':
                            text = text + "four "
                        if num[d + 1] == '5':
                            text = text + "five "
                        if num[d + 1] == '6':
                            text = text + "six "
                        if num[d + 1] == '7':
                            text = text + "seven "
                        if num[d + 1] == '8':
                            text = text + "eight "
                        if num[d + 1] == '9':
                            text = text + "nine "
                #for very big numbers
                if (((int(num[d]))>0)or((int(num[d+1]))>0)or((int(num[d-1]))>0)):
                    size = ln-d
                    text = text + str(numbers.get(size))
                d=d+2
    return text

print(humanize("3 *-4=-1 42-1+1+12345678-0"))
