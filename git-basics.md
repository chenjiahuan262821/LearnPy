
### 学习Git最最基本的用法

---

写在最前：

最近，在唐亮哥哥的怂恿下，决定好好利用github~找到廖雪峰的git教程，学习一下最最基本的用法——**创建仓库repository、把文件添加到仓库里面、文件管理修改以及版本进退、远程仓库与克隆、创建与合并分支。**

---

安装git以后，在开始菜单找到git Bash, 进行基本的设置。按照教程的原话是，“因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。”

	git config -h  #这是help的意思，看git config后面跟什么命令来实现目的
	git config -l  #这是list的意思，把配置的信息都列出来，包括上面提到的名字与Email地址

上面主要是为了查看唐亮哥哥帮我设置过没有（然而没有），那么接下去进行设置，具体的代码是：

	git config --global user.name "MyName" #设置username
	git config --global user.email"email@exmaple.com" #设置Email地址

**1. 创建仓库repository**

首先，选择一个合适的地方，创建一个空目录。教程原文有特别提醒“如果你使用Windows系统，为了避免遇到各种莫名其妙的问题，请确保目录名（包括父目录）不包含中文。”（突然明白为何唐亮之前提醒我用来博客的文件夹和文件名都用英文命名了~）

	mkdir LearnPy #创建一个空目录
	cd LeanPy #定位到这个目录
	pwd #显示当前路径是 e:/jadechen_blog/jadechen3.github.com/LearnPy

其次，要把这个仓库LearnPy设置成可以通过git管理，输入下面这个就ok了：

	git init

然后LearnPy此时是一个当前路径下的一个空仓库，对应的还会有一个隐藏的.git目录（用ls -ah可以看见），这是git用于跟踪管理仓库的，不能手动修改里面的东西（那就让它一直隐藏着吧...）。

**2. 把文件添加到repository里面**

按照教程，编写一个readme.txt文件，放在LearnPy的目录下。随后，通过**git add**命令将文件添加到对应的仓库。此时，通过**git commit**将文件提交到仓库，跟-m"describe what you did"描述这次提交的内容或意图等说明情况。
	
	git add readme.txt #把工作区里的一个或多个文件添加到暂存区
	git commit -m"created a new repo and wrote a readme file" #把暂存区的文件添加到repo并作说明以便追踪与管理

*关于git add: 后面可以跟多个文件（比如git add AA.py BB.md CC.txt）；也可以跟文件夹（比如git add file/）；也可以是当前目录下的所有东西（git add .）*

**3. 文件管理修改以及版本进退**

（1）修改文件与提交

此时我对LearnPy目录下的readme文件进行更改，在内容中给它加上一个日期（Date:2019/04/20）。仓库中的文本文件发生变化，git是可以追踪的，通过**git status**我们可以看到仓库中文件的状态——是否被更改过、新版本是否已经上传。

	git status #看到仓库中文件状态，告诉我们文件是否被修改与提交
	git diff readme.txt #对比文件前后查看哪儿发生了改动，也就是具体的修改内容

	git add readme.txt 
	git commit -m"add date" #确认无误后可以提交啦~

（2）版本进退

仓库中readme.txt有新旧两个版本了，但是我睡醒一觉就不太记得两个版本分别是什么样子。那么就可以向版本控制系统寻求帮助啦！

	git log #返回仓库中每一个版本及提交日期，顺序由近至远，以提交时的description作为提示

我们提交的每一个版本，git都会给它一个commit id，git知道现在是哪一个版本并把HEAD指针停留在那里，我们可以通过控制HEAD指向不同的版本id，实现版本的切换进退（原教程中的“时光机”）——上一个版本是HEAD^，上两个版本是HEAD^^,上100个版本是HEAD~100。用到的指令是**git reset**。

	git reset --hard HEAD^ #退回到上一个版本了
	cat readme.txt #查看当前版本的内容，确认一下
	git log #会惊奇地发现新的版本不在日志里，仿佛从来没有存在过

退回到上一个版本了，却发现还是新版本好，那就通过**git reflog**（它记录了我每一次的命令），找回新版本的commit id 然后HEAD指向那个id就好啦。

	git reflog #显示我每一次的commit id，以提交的description作提示

找到新版本"add date"的commit id是0d6fc77（输入前面几位就好），然后HEAD指向它。

	git reset --hard 0d6f #这样就回到新版本

（3）删除与还原文件

现在LearnPy工作区与仓库里都有一个readme.txt文件，我想把它删除了。
	
	rm readme.txt #在工作区里把文件删去了，此时工作区与仓库状态不一致
	git status #会告诉我test.txt被删除了。接下去，a)如果是误删可以还原，b)如果是真心想删除那就把仓库里也删去

	git checkout -- test.txt #a)注意是--并且文件名前有一个空格，这命令是用仓库里的版本替换工作区版本，无论工作区是修改还是删除，都可以替换或还原。

	git rm readme.txt #b)这就是把仓库里的文件也删去，那工作区与仓库都没有了这个文件

---
小总结：

1）提交工作区的文件，用**git add**与**git commit**两步。

2）修改文件直接在工作区修改即可，通过**git status**查看是否发生改变但还没提交新版本，通过**git diff**查看具体改动的地方。

3）返回之前的版本，通过**git log**查看版本顺序，通过**git reset --hard HEAD^**返回。

4）返回之后的版本，通过**git reflog**查看每一次的commit id，通过**git reset --hard [commit id]**就可以回到之后的版本，同样可以通过这个方法回到之前的版本呢。

5）工作区删除文件**rm**，仓库删除文件**git rm**。

6）在工作区误删但仓库仍有，则可以通过**git checkout -- [file]**还原到工作区。

---

**4.远程仓库与克隆**

（1）创建SSH key

已注册GitHub账号，本地Git仓库和GitHub仓库之间的传输是通过SSH加密的~在新设备上要创建一个SSH key才能实现联系。

	ssh-keygen -t rsa -C "Email@example.com" 

输入上面代码，之后一路回车，完成后可以在"用户"主目录里找到.ssh目录，里面有id-rsa和id-rsa.pub两个文件，那么SSH Key创建完成。登陆GitHub，"Account settings"->"SSH Keys"，任意Title，在Key文本框里粘贴id_rsa.pub文件的内容，确认添加SSH Key就完成啦。

*Github允许添加多个Key，只要把每台电脑的Key都添加到Github就可以在那些电脑上git push了。*

（2）在Github上建远程仓库并与本地关联

目标：目前在本地已经建立了一个LearnPy的仓库，想在GitHub创建一个备份仓库，两个仓库进行远程同步。

做法：在github右上角create new repository，命名“LearnPy”，创建后github会提示“push an existing repository from the command line”的代码（如下），复制粘贴到git Bash中就好啦（此时git Bash的路径应该是本地的LearnPy文件夹）

	git remote add origin https://github.com/[github帐户名]/LearnPy.git
	git push -u origin master #第一次推送到github要加-u

在GitHub中LearnPy这个仓库里可以看到和本地一样的内容了~从此以往，只要本地工作区通过git add和git commit作了提交，就可以通过命令**git push**更新到github：

	git push origin master

（3）将远程仓库克隆到本地

当前我在github上有一个远程仓库Hello-World，然而换了新电脑后本地是没有的，所以学习把它克隆到本地，用的命令是**git clone**。

	git clone https://github.com/[github帐户名]/Hello-world.git
	
由于没有返回上一级目录，运行完git clone的代码后在本地LearnPy文件夹里有一个Hello-World文件夹，所以要记住cd到合适的目录再克隆。

---

小总结：

1）创建SSH key，并添加到Github上实现关联

2）把本地仓库备份到github，先在gihub上创建一个同名仓库，第一次需要在本地仓库目录下输入两行代码（github上创建后有提示），从此以后的更新只需**git push**就可以了。

3）把远程仓库克隆到本地，先cd到合适的目录，使用**git clone**可以了，如果在远程上有更新而本地还没有更新，用**git pull origin master**（分支名master或source）就好了。

---

**5.创建与合并分支**

以上，都是在使用仓库内仅有的master分支，这是仓库的主分支，十分重要，而当多人协作的时候总不能大家同时都修改这一分支吧，所以创建额外的分支也十分重要。

	git checkout -b source #创建source分支并切换到source分支，自己创建的分支可以随意命名
	git branch #查看当前分支，命令会返回所有分支并在当前分支前面会标一个*号

现在已经创建并且切换到source分支了，后续可以通过git add、git commit进行操作，将本地工作区的文件上传到分支source上。

接下去，就看是要保存这个分支还是要合并到master上了。

（1）如果是要保存这个分支并上传到远程github仓库：
	
	git push origin source #上传到远程的source分支

（2）如果是要合并到master上并且不要这个source分支了：
	
	git checkout master #切换回master分支
	git merge source #将source分支的内容合并到master分支上
	git branch -d source #将source分支删除，它完成使命了


小总结：

查看分支：git branch；创建分支source：git branch source；切换分支：git checkout source；创建并切换分支：git checkout -b source；合并分支source到当前分支：git merge source；删除分支source：git branch -d source；将分支source推送到远程：git push origin source。

---


至此，这些基本功能应该能够满足我的需求了。

要继续去学CFA了，接下去的日子一定要好好努力阿！冲鸭！








	



