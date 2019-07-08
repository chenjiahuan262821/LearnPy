# Linux基础操作

Linux是**多用户的网络系统**，我们可以在Linux下创建多个用户，每个用户都会有自己专属的空间。在创建用户时，系统管理员会给每个用户建立一个主目录，通常在/home/目录下，比如：用户joyce的主目录为：/home/joyce。用户对自己主目录的文件拥有所有权，可以在自己的主目录下进行相关操作。

linux的优点：免费；开源；很多软件原生是在linux下运行的，庞大社区支持，生态环境好

linux的组成：linux内核，用户和内核交互的接口shell，文件系统（ext3、ext4），第三方应用软件

命令基本格式： cmd [options] [arguments]。Linux命令格式包含三个部分，分别是：命令、选项、参数，options称为选项，arguments称为参数

注意，linux区分大小写；一般来说，options如果是单字符则在前加一个减号-，如果是单词则在前加两个减号--（如-a和--all）。

常见通配符：

- *：匹配任何字符和任何数目的字符
- ?：匹配单一数码的任何字符
- []：匹配[]之内的任意一个字符
- [!]：匹配除了括号里面内容以外的任意字符


## 常见文件、目录操作命令

### linux最基础目录与文件操作的命令（使用得最多的命令）

输入命令的时候要常用**tab**键来补全，想要之前输入过的命令可以用键盘上下箭头进行搜索

- pwd 查看当前目录
- cd 后面跟路径来切换目录
- . 表示当前目录
- .. 表示当前目录的上一级目录
- - 表示切换目录前所在的目录
- ~ 表示用户主目录的绝对路径名

> 下面的命令其实和windows下的操作类似，无非是新建文件夹（mkdir）、新建文件（touch）、复制文件夹或文件（cp）、移动文件夹或目录（mv）、删除目录或文件夹（rm）、查找文件（find）、查看文件类型（ls或ll或file或stat）、查看文件内容（cat）、压缩文件（gzip、bzip2、tar）、解压文件（gzip -d等）、查找字符（grep+正则表达）

- mkdir 在当前目录下创建一个空目录
- rmdir 要求目录为空
- touch 生成一个空文件(touch newfilename)或更改文件三种时间
- cp 复制文件或目录，如cp joyce.txt ../newnew/ 是将joyce.txt文件从当前路径复制一份到newnew文件夹里
- mv 移动文件或目录，如mv test.txt ../newnew/ 是将test.txt文件从当前路径移动到newnew文件夹里
- rm 删除文件或目录，如rm test.txt （注意rm需要谨慎使用，尤其 rm -rf XXX文件夹要格外谨慎）
- ls 显示文件或目录信息
- find 查找文件，find+目录+条件+条件值，如find . -name "*.txt"就是查找当前目录及子目录下以txt结尾的文件
- file 查看文件类型
- stat 文件属性信息
- cat 查看文本文件内容
- more 可以分页查看
- tail -10 查看文件尾部的10行
- head -20 查看文件头部的20行
- echo 把内容重定向到指定的文件中，有则打开，无则创建；其中>是覆盖模式，>>是追加模式

### 文件打包与压缩命令

常用的压缩命令：

- gzip filename
- bzip2 filename
- tar -czvf filename

常用的解压命令：

- gzip -d filename.gz
- bzip2 -d filename.bz2
- tar -xzvf filename.tar.gz


### 查找一个文本文件下的某些字符

用 grep+正则表达式 替代 ctrl+F

**常见的正则表达式**

- ^x 是以x开头的字符串
- x$ 是以x结束的字符串
- . 匹配任意一个字符，l..e 对应love、live、lone等等
- ? 匹配任意一个可选字符，xy? 对应x,xy
- * 匹配零次或多次，xy* 对应 x,xy,xyy,xyyyy等等
- + 匹配一次或多次，xy+ 对应 xy,xyy,xyyy,xyyyy等等
- [...] 匹配任意一个字符，[xyz]对应x,y,z
- ()对正则表达式分组，(xy)+对应xy,xyxy,xyxyxy等等
- {n}匹配n次，go{2}gle对应google
- {n,}匹配最少n次，go{2,}对应google,gooogle,goooole,gooooogle等等
- {n,m}匹配n到m次，go{2,4}gle对应google,gooogle,goooole
- | 或，如good|bon对应good或bon
- \转义字符，如\^对应^

**grep可以使用正则表达式搜索文本，并把匹配的行打印出来**

grep [option] PATTERN [FILE...]

注意：PATTERN 是查找条件，可以是普通字符串、可以是正则表达式；FILE 是要查找的文件，可以是用空格间隔的多个文件，也可是使用Shell的通配符在多个文件中查找PATTERN

示例：

- 显示 myfile 中第一个字符为字母的所有行，grep '^[a-zA-Z]' myfile
- 在文件 myfile 中查找包含字符串mystr在第几行，grep -n mystr myfile
- 在某一目录下循环搜索所有文件是否包含字符，grep -r mystr ./
- 列出/etc目录（包括子目录）下所有文件内容中包含字符串“root”的文件名，grep -lr mystr ./


### vim基本操作

vim filename后进入normal模式，常用的模式是insert模式和command模式。

#### 从normal模式进入insert模式：

+ i 在当前字符前插入
+ a 在当前字符后插入
+ o 在当前行的下一行插入新的一行

> 插入模式下可以进行文本编辑，通过输入i或a或o可以进入插入模式，相当于在文本编辑器进行文本编辑，该换行换行，该删除删除，之后**通过esc键退出插入模式（返回到normal模式）**。如果要保存修改，需要进入命令行模式，:w进行保存，或者:wq保存并退出。

#### 在insert模式下：

normal模式下，h、j、k、l相当于上下左右的光标移动；insert模式下，通过键盘的上下左右键实现上下左右的光标移动。

和直接文本编辑没有什么区别

ctrl + h 删除上一个输入的字符
ctrl + w 删除上一个输入的单词
ctrl + u 删除当前行

#### 从normal模式进入command模式：

:w 保存
:q 退出（:q!是不保存-强制退出）
:vs 垂直分屏
:sp 水平分屏

在分屏以后，如果要切换窗口，需要退出到normal模式：

<ctrl-w>h 切换到左边的窗口
<ctrl-w>j 切换到下边的窗口
<ctrl-w>k 切换到上边的窗口
<ctrl-w>l 切换到右边的窗口


#### 在command模式下的查询：

使用/或者?进行前向或者反向搜索，比如/cjh
使用n/N跳转到下一个或者上一个匹配