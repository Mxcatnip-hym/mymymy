import string
from openpyxl import load_workbook
import jieba
import matplotlib.pyplot as plt
import wordcloud

txt = ""
singer_count = {}
wb = load_workbook("./data.xlsx")
sheet = wb.active

flag = True
for row in sheet:
    if flag:
        flag = False
        continue
    singer = row[1].value
    try:
        txt += row[3].value+" "
    except:
        continue
    if singer not in singer_count:
        singer_count[singer] = 1
    else:
        singer_count[singer] += 1
# 歌手出现的次数取前10
singer_count = sorted(list(singer_count.items()), key=lambda x:x[1], reverse=True)[0:10]
plt.rcParams["font.sans-serif"] = "SimHei"
plt.figure(figsize=(10, 8))
plt.title("酷狗TOP500出现频次前10歌手")
x, y = [info[0] for info in singer_count], [info[1] for info in singer_count]
for i in range(len(y)):
    plt.text(x= i, y=y[i], s = '%d' % y[i], color="r")
plt.xlabel("出现歌手")
plt.ylabel("出现次数")
plt.bar(x, y)
plt.show()
# 生成词云图
words = jieba.lcut(txt)
tmp = []
for word in words:
    word = word.strip()
    if len(word)==0 or len(word)==1:
        continue
    if word in "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏.":
        continue
    if word in string.punctuation+" ":
        continue
    if word in ["作词", "编曲", "制作", "作曲"]:
        continue
    tmp.append(word)
txt = " ".join(tmp)
wc = wordcloud.WordCloud(font_path="./font.ttf", background_color="white")
img = wc.generate(text=txt)
plt.title("歌词词云图")
plt.imshow(img)
plt.show()







