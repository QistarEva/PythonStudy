#encoding:utf-8


js=['反派','角色','角色中的其他','男主角','女主角','配角']
jq=['发展','结局','剧情','开头','泪点','笑点']
st=['动作','画面','镜头','视听','试听效果中的其他','音乐']
zz=['编剧','出品公司','导演','选景','制作']
zt=['风格','题材内容','主题']
CD={'角色':js,'剧情':jq,'视听':st,'主题':zt,'制作':zz}

name = raw_input('输入用户名：')
path = '/home/' + name + '/作业/'

def forone( file , key2 , c ):
    with open(path + '词典/' + file + '/' + key2, 'r') as e:  # 打开key2关注点的词典
        for line in e.readlines():  # 按行读取关键词词典，每次读取一个关键词
            d = str(line.strip('\n').strip(' '))  # 用d储存去掉换行符和空格的关键词

            if d in c:  # 若该评论中出现关键词
               return True

def go():
    with open(path + '结果报告.txt', 'a') as note:  # 打开输出文本文件

        for file in CD.keys():  # 通过循环获取字典的key，循环读取类别名
            f = 0

            print  '\n' + file + ':'  # 输出   关注类：
            note.write('\n' + file + ':' + '\n'.encode('utf-8'))  # 写入   关注类：

            for key in CD[file]:  # 通过循环获取list中的元素，循环获取关注点名
                k = 0

                if key != '试听效果中的其他':
                    key2 = key + '.txt'
                else:
                    key2 = key

                with open(path + '太空旅客.txt', 'r') as t:  # 打开原文本《太空旅客》
                    for text in t.xreadlines():  # 按行读取《太空旅客》，每次读取一条评论
                        c = str(text)  # 用c储存str格式的《太空旅客》评论

                        if forone(file, key2, c) == True:
                            k = k + 1  # 则k+1，关注点+1

                print '    ' + key + ':' + str(k)  # 输出 关键词：关注数（k）

                note.write('    ' + key + ':' + str(k) + '\n'.encode('utf_8'))  # 写入文档  关键词：关注数

go()