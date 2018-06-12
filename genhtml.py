# coding=UTF-8

execArray = {}
execArray["0009"] = 0
execArray["0027"] = 1
execArray["0065"] = 2
execArray["0076"] = 1
execArray["0077"] = 1
execArray["0126"] = 0
execArray["0300"] = 1
execArray["0395"] = 0
execArray["0425"] = 1
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
execArray["2160"] = 1
execArray["2161"] = 0
execArray["2167"] = 0
execArray["2211"] = 0
execArray["2243"] = 0
execArray["2247"] = 1
execArray["2258"] = 1
execArray["2309"] = 0
execArray["2313"] = 0
execArray["2330"] = 0
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

ofile = open("test1.html", "w")

ofile.write("<!DOCTYPE html>\n")
ofile.write("<html>\n")
ofile.write("<head>\n")
ofile.write("<style>\n")
ofile.write("table, th, td {\n")
ofile.write("border: 1px solid orange;\n")
ofile.write("border-collapse: collapse;\n")
ofile.write("}\n")
ofile.write("</style>\n")
ofile.write("<title>Vietname CCC</title>\n")
ofile.write("</head>\n")
ofile.write("<body>\n")
ofile.write("<h3>Giáo Lý Hội Thánh Công Giáo</h3>\n")
ofile.write("<table>\n")
ofile.write("<tr><th>Câu</th><th>Đề Tài</th></tr>\n")



flag = 0
first_word = ""
with open("in1.txt") as in1:
    cnt = 0
    for line in in1:
#        print("line {} flag {} contents {}".format(cnt, flag, line))
        cnt += 1
        if flag == 0:
            first_word = line
            flag = 1
        else:
            if flag == 1:
                flag = 2
            else:
                if flag == 2:
                    ofile.write("<tr><td>" + first_word.strip() + "</td><td>" + line.strip() + "</td></tr>\n")
                    flag = 3
                else:
                    flag = 0

ofile.write("</table>")



#p_index = 0
p_index_str = "0000"
exception_handling = 0
o2 = open("temp2.txt", "w")
first_p = 1

with open("in2.txt") as in2:
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

#        if llen > 5 and llen < 120:
#            print("{}".format(line))
#            o2.write(line)

        if len(line) == 4:
            if first_p == 1:
                first_p = 0
            else:
                ofile.write("</p>\n")
            ofile.write("<p>\n")
            ofile.write("<span style='color:blue'>" + line + "</span><br>\n")
            p_index_str = line
        else:
#            if line in execArray:
#                print("p_index {} value {}".format(line, execArray[line]))
#                o2.write(execArray[line])
#            if len(line) > 5:
#                if len(line) > 100:
#                    ofile.write("<span>" + line.strip() + "</span><br>\n")
#                else:
#                    ofile.write("<span style='font-weight:bold'>" + line.strip() + "</span><br>\n")
            if len(line) > 4:
                ofile.write(line + "<br>\n")
ofile.write("</p>")
ofile.write("</body>")
ofile.write("</html>")

ofile.close()
o2.close()
