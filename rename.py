import os
list_data=os.listdir('./')
import re
re_if_kinh = re.compile(r'\[打包下载\]需解压重命名album目录\[(.*?)\]为\[(.*?)\]')
#下下来的文件名有时改名信息包含.mp4.mp4
match_mp4 = re.compile(r'.*?\.mp4')
for name in list_data:
    result = re_if_kinh.match(name)
    if result:
        filename = match_mp4.match(result.group(1)).group(0)
        os.rename('./album/'+filename, './album/'+result.group(2))