在windows中安装


一。1)、安装pyinstaller需要pyWin32包（只有windows中手动安装）
    下载对应的pyWin32安装包>>地址: https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/   在该地址下载。就OK。
    需要说明的是，下载的安装包必须和你电脑安装的python版本相同。如: 我的电脑安装了python 3.4版本 32位的。那么我就需要下载对应的版本，
    就是pywin32-220.win32-py3.4.exe，可以看出来win32就是对应我电脑python版本的32位，py3.4对应我电脑中    python的版本。
    如果是64位的，那么就是amd64，注意这里说得32和64位，不是指你的电脑系统。是指python的版本有32位和64位之分。你查看你安装的python版本就OK，命令行查看（DOS）：python，会直接显示


    C:\Users\Administrator>python
    Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 19:28:18) [MSC v.1600 32 bit (In
    tel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

    win32就是指32位咯。amd64就是指64位。


    2)、下载完成，就需要点击安装了，打开pywin32-220.win32-py3.4.exe，会直接跳转到安装界面，然后安装程序会自动搜索你电脑里面的python，如果版本不对应，就无法搜索到，也就无法安装，所以下载的版本要对应。安装完毕！

    3)、python环境变量问题以及模块找不到问题。安装python如果默认系统安装，也就是安装在C盘下面，那么python程序，就会自动把环境变量配置好，如:C:\Python34\;C:\Python34\Scripts; 这个变量会直接添加到Path变量值下。
        如果你不是安装在C盘，那么你需要自己配置。也就是和上面的一样，把两个文件夹地址放到环境变量下。
        解决导入pywin32找不到模块问题： 将python安装目录下的Lib\site-packages添加到PYTHONPATH环境变量，将python安装目录Lib\site-packages\pywin32_system32下的文件拷贝到系统system32目录下，这样就可以解决导入     pywin32模块时报找不到模块问    题将python安装目录Lib\site-packages\pywin32_system32下的文件拷贝到系统system32目录下，这样就可以解决导入pywin32模块时报找不到模块问题。

二。如此就解决pywin32的问题。现在安装pyinstaller。可以直接在DOS命令行下： 
    pip install pyinstaller

三。使用pyinstaller必须在命令行中，
    1。在要打包的文件的文件夹上右键打开命令行
    2、在命令行中输入pyinstaller lianxi.py(lianxi.py是要变成。exe的py文件)
    3.生成的lianxi.exe在.\dist\lianxi.exe

    （下面的都是废话） 

'''
5）、现在就来说说pyinstaller命令的使用。使用该命令也会让你头疼的，不过相对别的打包，这是很方便的了。
     ==>先来说说该命令的参数，必须了解这些参数，才能更好的打包，使用该命令。

        -distpath=path_to_executable     //     该参数指定生成的可执行文件存放的目录，也就是生成的exe文件所在的目录，如果不指定，就默认存放在你的C盘用户文档目录下，也就是Administrator目录下dist文件夹下。
        -workpath=path_to_work_files    //     该参数指定编译中临时文件存放的目录，默认存放在Administrator目录 build文件夹下。
        -clean    //     清理编译时临时文件，也就是build文件夹下的临时文件。
        -D(简写)，-onedir(全称)     //     创建一个目录包含exe执行文件，里面还有很多依赖的文件(默认的选项)。
        -F(简写)，-onefile(全称)      //     生成单独的exe文件，而不是文件夹。解释:  就是一个单独的exe执行程序。不带其他任何文件信息。
        -c(简写)，-console，-nowindowed    //     使用控制台，就是dos窗口的形式，无界面(默认)
        -w(简写)，-windowed，-noconsole     //     使用窗口，无控制台，如: 图形化窗口程序，如果不指定-w，运行的话就会带dos窗口，如果带的话，就只有和正常的软件打开方式一样。
        -i(简写)，--icon=图标路径         //     如你的程序需要带好看的ico格式的图标，那么就带需要准备好图标，ico格式，然后加上该参数，指定图标路径。
        -p(简写)，-path             //一些你的程序所依赖的包，模块的路径，需要指定。
        -d(简写)，-debug(全称)     //      编译为debug模式，主要是获取运行中的日志信息，查看编译错误。
        -version-file=version_text_file     //     该参数为exe文件添加版本信息，版本信息可以通过运行pyi-grab_version加上要获取版本信息的exe文件的路径来生成，生成后的版本信息文件可以按需求修改并作为--version-file的参数添加到     要生成的exe文件中去
        pyinstaller -h 来查看参数


6)、示例：  我自己执行的一个写的图形化窗口程序:
                     
C:\Users\Administrator>pyinstaller -F C:\Users\Administrator\Desktop\wugui\shilian.py -p C:\Python34\Lib\tkinter;C:\Python34; -i C:\Users\Administrator\Desktop\ico\3.ico

，-F 生成单独exe执行程序。 -p 我的程序所依赖的包，和模块路径(一般都在你的python安装目录下)。-i 我的图标路径。
如果出现如下图，就说明成功。
'''

