# coding=UTF-8


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
execArray["2551"] = 0
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
ofile.write("</style>\n")
ofile.write("<title>Giáo Lý Hội Thánh Công Giáo</title>\n")
ofile.write("</head>\n")
ofile.write("<body>\n")
ofile.write("<h3>Giáo Lý Hội Thánh Công Giáo</h3>\n")
ofile.write("<table style='width:100%;border:0px'><tr><td style='width:100%;border:0px;padding:0px;'>\n")
ofile.write("<table>\n")
ofile.write("<tr><th>Câu</th><th>Đề Tài</th></tr>\n")
ofile.write("<tr><td align='center'><a href='#0000'>Mở đầu</a></td><td><a name='L0000'>Lời mở đầu</a></td></tr>\n")


flag = 0
numbers_str = ""
with open("new/GLCG-part-1.txt") as in1:
    cnt = 0
    for line in in1:
        line = line.strip()
#        print("line {} flag {} contents {}".format(cnt, flag, line))
        cnt += 1
        if flag == 0:
            numbers_str = line
            flag = 1
        else:
            if flag == 1:
                flag = 2
            else:
                if flag == 2:
                    ofile.write("<tr><td align='center'><a href='#" + getPIndex(numbers_str) + "'>" + numbers_str + "</a></td><td><a name='L" + getPIndex(numbers_str) + "'>" + line + "</a></td></tr>\n")
                    addLabels(numbers_str)
                    flag = 3
                else:
                    flag = 0

ofile.write("</table>")



#p_index = 0
p_index_str = "0000"
exception_handling = 0
#o2 = open("temp2.txt", "w")
first_p = 1
bold_index = 0

with open("new/GLCG-part-2.txt") as in2:
    cnt = 0
    for line in in2:
#        print("cnt {} len {} text {}".format(cnt, len(line), line))
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
                            ofile.write(fixParenthesis(line[:-6]) + "<a href='#" + labelArray[int(p_index_str)] + "'><span class='med'>[Back]</span></a><br>\n")
                        else:
                            ofile.write(fixParenthesis(line) + "<br>\n")
                # regular cases
                else:
                    if len(line) < 120:
                        ofile.write("<b>" + line + "</b><br>\n")
                    else:
                        if line.endswith("[Back]"):
                            # print("{}".format(p_index_str))
                            ofile.write(fixParenthesis(line[:-6]) + "<a href='#" + labelArray[int(p_index_str)] + "'><span class='med'>[Back]</span></a><br>\n")
                        else:
                            ofile.write(fixParenthesis(line) + "<br>\n")

ofile.write("</p>\n")
ofile.write("</td></tr></table>\n")
ofile.write("</body>\n")
ofile.write("</html>\n")

ofile.close()
#o2.close()
