# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 创建一个文件，状态可写入
        fout=open('output.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        #fout.write("<table>")
        fout.write("<a>")
        # Python默认编码： ascii 需要改成‘utf-8’
        for data in self.datas:
            #fout.write("<tr>")
            #fout.write("<td>%s</td>"% data['url'])
            #fout.write("<td>%s</td>"% data['title'])
            #fout.write("<td>%s</td>"% data['summary'])
            #fout.write("</tr>")

            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])

        #fout.write("</table>")
        fout.write("</a>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()