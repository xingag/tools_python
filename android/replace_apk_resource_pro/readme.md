# 替换 APK 里面的资源

## 思路

1. 使用 `apktool.jar` 解压 `apk`
2. 替换资源
3. 利用 `apktool.jar` 重新打包
4. 使用 `jarsigner` 对 `apk` 进行重新签名
5. 打包成 `exe` 可执行文件



## 解压

```
def __unzip_apk(self):
        """
        解压当前目录下的apk文件
        :return:
        """
        # 文件名称，包含后缀名
        file_name = get_current_folder_file('apk')

        # 文件名称，不包含后缀名
        file_name_pre = file_name.split('.')[0]

        os.system('java -jar apktool.jar d %s' % file_name)

        print('第1步：解压成功~')

        return file_name_pre
```



## 替换资源

```
def __replace_source(self, file_name_pre):
        """
        替换资源
        @:param file_name_pre  文件夹的名称
        :return:
        """
        print('生成文件夹的名字是:%s' % file_name_pre)

        # 重命令当前目录下的文件
        rename_current_file("png", self.file_name)

        # 待替换的完成路径是
        logo_file_path = './%s/res/drawable-mdpi/logo_white.png' % file_name_pre

        # 开始替换文件
        replace_file('./%s' % self.file_name, logo_file_path)

        print('第2步：替换资源图片成功~')
```



## 重新打包

```
def __rezip_apk(self, folder_name):
        """
        重新打包成apk
        @:param folder_name 文件夹的名称  source
        :return:
        """

        # 重新打包成apk
        os.system('java -jar apktool.jar b %s -o %s' % (folder_name, self.target_apk_name))

        # 删除临时文件夹
        shutil.rmtree('./%s/' % folder_name)

        print('第3步：重新打包成功~')
```



## 重新签名

```
def __re_sign(self):
        """
        重新签名
        :return:
        """
        # 重新签名
        cmd = 'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore **.keystore -storepass ** %s **' % self.target_apk_name
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)

        # 输入参数
        p.communicate(input=b'nantian')
        print('第4步：重新签名成功~')
```



## 可执行文件

使用 [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe)  生成可执行文件。

