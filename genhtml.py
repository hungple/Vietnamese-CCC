# coding=UTF-8

#() - tuple
#A tuple is a sequence of items that can't be changed (immutable).

#[] - list
#A list is a sequence of items that can be changed (mutable).

#{} - dictionary or set
#A dictionary is a list of key-value pairs, with unique keys (mutable).

execArray = {}
execArray["0009"] = 0
execArray["0027"] = 1
execArray["0033"] = 0
execArray["0065"] = 2
execArray["0076"] = 1
execArray["0077"] = 1
execArray["0120"] = 0
execArray["0126"] = 0
execArray["0300"] = 1
execArray["0395"] = 0
execArray["0430"] = 2
execArray["0484"] = 1
execArray["0571"] = 1
execArray["0610"] = 1
execArray["0619"] = 1
execArray["0631"] = 1
execArray["0688"] = 0
execArray["0714"] = 0
execArray["0771"] = 1
execArray["0782"] = 1
execArray["0815"] = 0
execArray["0821"] = 0
execArray["1093"] = 1
execArray["1135"] = 1
execArray["1266"] = 0
execArray["1303"] = 0
execArray["1331"] = 0
execArray["1346"] = 0
execArray["1358"] = 0
execArray["1381"] = 0
execArray["1496"] = 0
execArray["1532"] = 0
execArray["1600"] = 0
execArray["1625"] = 1
execArray["1697"] = 0
execArray["1698"] = 0
execArray["1712"] = 0
execArray["1716"] = 2
execArray["1718"] = 1
execArray["1720"] = 1
execArray["1736"] = 0
execArray["1748"] = 0
execArray["1750"] = 1
execArray["1763"] = 1
execArray["1780"] = 0
execArray["1789"] = 0
execArray["1800"] = 0
execArray["1831"] = 0
execArray["1833"] = 0
execArray["1857"] = 0
execArray["1868"] = 0
execArray["1892"] = 0
execArray["1893"] = 0
execArray["1919"] = 0
execArray["1945"] = 0
execArray["1982"] = 0
execArray["1985"] = 0
execArray["2019"] = 0
execArray["2029"] = 0
execArray["2082"] = 0
execArray["2136"] = 0
execArray["2137"] = 0
execArray["2142"] = 0
execArray["2160"] = 1
execArray["2161"] = 0
execArray["2167"] = 0
execArray["2174"] = 0
execArray["2211"] = 0
execArray["2243"] = 0
execArray["2247"] = 1
execArray["2258"] = 1
execArray["2309"] = 0
execArray["2313"] = 0
execArray["2330"] = 0
execArray["2331"] = 0
execArray["2392"] = 1
execArray["2395"] = 0
execArray["2401"] = 1
execArray["2464"] = 1
execArray["2508"] = 0
execArray["2509"] = 0
execArray["2520"] = 1
execArray["2529"] = 0
execArray["2551"] = 1
execArray["2552"] = 0
execArray["2613"] = 0
execArray["2676"] = 0
execArray["2694"] = 0
execArray["2759"] = 1
execArray["2768"] = 0
execArray["2814"] = 0

def getMyString(num):
    s = "0000"
    if num < 10:
        s = "000" + str (num)
    else:
        if num < 100:
            s = "00" + str (num)
        else:
            if num < 1000:
                s = "0" + str (num)
            else:
                s = str (num)
    return s

# inStr = "4 - 9"
# return "0004"
def getPIndex(inStr):
    mList = inStr.split(" - ")
    firstNumStr = mList[0]
    s = "0000"
    if len(firstNumStr) == 1:
        s = "000" + firstNumStr
    else:
        if len(firstNumStr) == 2:
            s = "00" + firstNumStr
        else:
            if len(firstNumStr) == 3:
                s = "0" + firstNumStr
            else:
                s = firstNumStr
    return s


labelArray = {}
labelArray[0] = "L0000"
#labelArray[1] = "L0000"
# numbers_str = "4 - 10"
def addLabels(numbers_str):
    mList = numbers_str.split(" - ")
    # mList[0] holds "4"
    # mList[0] holds "10"
    firstNumStr = mList[0]
    firstNum = int(firstNumStr)
    secondNumStr = mList[1]
    secondNum = int(secondNumStr)

    label = "L" + getMyString(firstNum)
    for x in range(firstNum, secondNum + 1):
        #print("x {} label {}".format(x, label))
        labelArray[x] = label


def fixParenthesis(inStr):
    newStr = inStr.replace('[','(')
    newStr2 = newStr.replace(']',')')

    # lower case for any ()
    newStr3 = newStr2.replace("(","<span class='tiny'>(")
    newStr4 = newStr3.replace(")",")</span>")
    return newStr4



ofile = open("out/new.html", "w")

ofile.write("<!DOCTYPE html>\n")
ofile.write("<html>\n")
ofile.write("<head>\n")
ofile.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>\n")
ofile.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
ofile.write("<style>\n")
ofile.write("table, th, td {\n")
ofile.write("border: 1px solid orange;\n")
ofile.write("border-collapse: collapse;\n")
ofile.write("padding: 3px;\n")
ofile.write("}\n")
ofile.write(".pi {font-weight:bold; color:blue}\n")
ofile.write(".tiny {font-size:small;}\n")
ofile.write(".med {font-size:medium;}\n")
ofile.write("p {font-size:large;}\n")

ofile.write("/* Style the tab */\n")
ofile.write(".tab {overflow: hidden; border: 1px solid #ccc; background-color: #f1f1f1;}\n")
ofile.write("/* Style the buttons inside the tab */\n")
ofile.write(".tab button {background-color: inherit; float: left; border: none; outline: none; cursor: pointer; padding: 14px 16px; transition: 0.3s; font-size: 17px;}\n")
ofile.write("/* Change background color of buttons on hover */\n")
ofile.write(".tab button:hover {background-color: #ddd;}\n")
ofile.write("/* Create an active/current tablink class */\n")
ofile.write(".tab button.active {background-color: #ccc;}\n")
ofile.write("/* Style the tab content */\n")
ofile.write(".tabcontent {display: none; padding: 6px 12px; -webkit-animation: fadeEffect 1s; animation: fadeEffect 1s;}\n")
ofile.write("/* Fade in tabs */\n")
ofile.write("@-webkit-keyframes fadeEffect { from {opacity: 0;} to {opacity: 1;}}\n")
ofile.write("@keyframes fadeEffect { from {opacity: 0;} to {opacity: 1;}}\n")

ofile.write("</style>\n")
ofile.write("<title>Giáo Lý Hội Thánh Công Giáo</title>\n")
ofile.write("</head>\n")

ofile.write("<body>\n")
ofile.write("<h3>Giáo Lý Hội Thánh Công Giáo</h3>\n")

#ofile.write("<table style='width:100%;border:0px'><tr><td style='width:100%;border:0px;padding:0px;'>\n")
ofile.write("<table style='width:550px;border:0px'><tr><td style='width:100%;border:0px;padding:0px;'>\n")
ofile.write("  <div class='tab'>\n")
ofile.write("    <button class=\"tablinks\" onclick=\"openTab(event, 'Tab1')\" id=\"defaultOpen\">Mục lục</button>\n")
ofile.write("    <button class=\"tablinks\" onclick=\"openTab(event, 'Tab2')\">Số câu</button>\n")
ofile.write("  </div>\n")
ofile.write("</td></tr></table>\n")
ofile.write("  <div id='Tab1' class='tabcontent'>\n")

numbers_str = ""
with open("new/table-content.txt") as in3:
    for line in in3:
        line = line.strip()
        mList = line.split("[")
        #mList[1] = '26]'' or '27-49]'
        mList2 = mList[1].split("-")
        indStr = ""
        if mList2[0].endswith("]"):
            #print("numberStr: {}".format(mList2[0][:-1]))
            indStr = mList2[0][:-1]
        else:
            #print("numberStr: {}".format(mList2[0]))
            indStr = mList2[0]
        ofile.write(mList[0] + "<a href='#" + getPIndex(indStr) + "'>[" + mList[1] + "</a><br>\n")

ofile.write("  </div>\n")

ofile.write("  <div id='Tab2' class='tabcontent'>\n")

ofile.write("<table>\n")
ofile.write("<tr><th>Câu</th><th>Đề Tài</th></tr>\n")
ofile.write("<tr><td width=101 align='center'><a href='#0000'>Mở đầu</a></td><td><a name='L0000'>Lời mở đầu</a></td></tr>\n")


numbers_str = ""
with open("new/GLCG-part-1.txt") as in1:
    for line in in1:
        line = line.strip()
        if len(line)>3:
            if line[0].isdigit():
                numbers_str = line
                #print("number line {}".format(numbers_str))
            else:
                ofile.write("<tr><td align='center'><a href='#" + getPIndex(numbers_str) + "'>" + numbers_str + "</a></td><td><a name='L" + getPIndex(numbers_str) + "'>" + line + "</a></td></tr>\n")
                addLabels(numbers_str)

ofile.write("</table>\n")

ofile.write("  </div>\n")

tfile = open("new/GLCG-part-2.txt", "w")
tempfile = open("new/GLCG-part-2-a.txt")
tfile.write(tempfile.read())
tempfile.close()
tempfile = open("new/GLCG-part-2-b.txt")
tfile.write(tempfile.read())
tempfile.close()
tempfile = open("new/GLCG-part-2-c.txt")
tfile.write(tempfile.read())
tempfile.close()
tfile.close()

#p_index = 0
p_index_str = "0000"
exception_handling = 0
#o2 = open("temp2.txt", "w")
first_p = 1
bold_index = 0

with open("new/GLCG-part-2.txt") as in2:
    cnt = 0
    for line in in2:
        # print("cnt {} len {} text {}".format(cnt, len(line), line))
        cnt += 1

        line = line.strip()

        # check paragraph index number
#        llen = len(line.strip())
#        if line.find(p_index_str) >= 0:
#            print("{}".format(p_index_str))
#            o2.write(p_index_str + "\n")
#            p_index += 1
#            p_index_str = getMyString(p_index)

        # print out to find rule for exception to bold the text
#        if llen > 5 and llen < 120:
#            print("{}".format(line))
#            o2.write(line)

        if len(line) == 4 and line.isdigit():
            if first_p == 1:
                first_p = 0
            else:
                ofile.write("</p>\n")
            ofile.write("<p>\n")
            ofile.write("<span class='pi'><a name='" + line + "'>" + line + "</a></span><br>\n")
            p_index_str = line
            bold_index = 0
        else:
            if len(line) > 4:
                # special exeception cases:
                if p_index_str in execArray:
                    if bold_index < execArray[p_index_str]:
                        ofile.write("<b>" + line + "</b><br>\n")
                        bold_index += 1
                    else:
                        if line.endswith("[Back]"):
                            # ofile.write(fixParenthesis(line[:-6]) + "<a href='#" + labelArray[int(p_index_str)] + "'><span class='med'>[Back]</span></a><br>\n")
                            ofile.write(fixParenthesis(line[:-6]) + "<br>\n")
                        else:
                            ofile.write(fixParenthesis(line) + "<br>\n")
                # regular cases
                else:
                    if len(line) < 120:
                        ofile.write("<b>" + line + "</b><br>\n")
                    else:
                        if line.endswith("[Back]"):
                            # print("xxx {}".format(p_index_str))
                            # ofile.write(fixParenthesis(line[:-6]) + "<a href='#" + labelArray[int(p_index_str)] + "'><span class='med'>[Back]</span></a><br>\n")
                            ofile.write(fixParenthesis(line[:-6]) + "<br>\n")
                        else:
                            ofile.write(fixParenthesis(line) + "<br>\n")

ofile.write("</p>\n")
#ofile.write("</td></tr></table>\n")
ofile.write("<script>\n")
ofile.write("function openTab(evt, tabName) {\n")
ofile.write("    var i, tabcontent, tablinks;\n")
ofile.write("    tabcontent = document.getElementsByClassName('tabcontent');\n")
ofile.write("    for (i = 0; i < tabcontent.length; i++) {\n")
ofile.write("        tabcontent[i].style.display = 'none';\n")
ofile.write("    }\n")
ofile.write("    tablinks = document.getElementsByClassName('tablinks');\n")
ofile.write("    for (i = 0; i < tablinks.length; i++) {\n")
ofile.write("        tablinks[i].className = tablinks[i].className.replace(' active', '');\n")
ofile.write("    }\n")
ofile.write("    document.getElementById(tabName).style.display = 'block';\n")
ofile.write("    evt.currentTarget.className += ' active';\n")
ofile.write("}\n")
ofile.write("// Get the element with id=\"defaultOpen\" and click on it\n")
ofile.write("document.getElementById(\"defaultOpen\").click();\n")
ofile.write("</script>\n")

ofile.write("</body>\n")
ofile.write("</html>\n")

ofile.close()
#o2.close()
