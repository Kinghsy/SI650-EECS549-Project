# Instructions

首先以`.md`的格式结尾的文件是传说中的`MarkDown`文件，大家可以自行Google哪些软件可以打开这类文件。我当前使用的是Topyra，觉得还不错。


考虑到大家可能是第一次接触git吧，我写个简单的小教程。

git是用来做版本控制的，适合多人共同开发一个项目。我觉得如果没有用过可以先尝试用一下这个东西，玩玩也好，不会我可以来维护。

这里默认大家会使用命令行，讲道理`EECS280`或者说`EECS402`应该是讲过如何使用命令行的。确认你的命令行中有一个东西叫做git。可以通过`git --version`来进行查看。

在一开始的时候，可以先用`git clone https://github.com/Kinghsy/SI650-EECS549.git`先把我

然后呢，在整个项目中，会有多个branch。一个branch你可以认为是一个人的工作空间。在这个项目中，我先给四个人各自建立了一个工作空间，按照大家名字的首字母命名的，分别是hsy, ybw, hcy, ty。你们可以分别查看一下。除此之外还有一个主branch，叫做master，存放的是我们当前的总体进度。正确的开发过程应该是，每个人在自己的branch，比如我就在hsy中完成自己的开发，然后把我的开发的部分同步到master中，下次开发之前，再从master中，把别人开发的内容给同步出来，到我的branch中，在此基础上继续开发。注意一下，这里的所有的branch都是分远端和本地的。你要保证的是你同步到了远端的master上

所以，当你开发之前，请务必确定，你在自己的branch中进行了开发。`git checkout hsy`，通过这条命令可以来到`hsy`这个branch。同理，`hsy`可以换成别的。

在来到自己的branch之后，第一件事情是与master进行同步。使用的代码是`git pull origin master`。

然后你就可以开始开发啦。

然后开发完呢，你可以在自己的branch里面，使用`git status`命令查看有多少更新。然后再使用`git add ....`命令把你需要的修改的文件给加到暂存区里面，然后再用`git commit -m "here is comment"`来确认这此的更改提交。到目前为止呢，所有的更改都已经提交到了你的本地的自己的branch中，比如本地的hsy中。

然后请务必提交到远端的（这里我们使用的是github）你的branch中，对应的命令是`git push origin hsy`，请把`hsy`改成对应的你的branch名称。

如果你觉得你不会呢，请在这步骤之后告诉我，然后我会来进行merge，如果想自己进行merge呢，操作是这样子的。首先进入本地的master branch，`git checkout master`，并且确定这个`master`的版本是最新版本，也就是使用`git pull origin master`，然后将本地的你的branch和master进行merger, `git merge hsy`,注意一下其实有可能会有冲突产生，就自行尝试解决吧。然后呢再把merge完成的master给传到远端,`git push origin master`。就完成了对应的操作。

讲道理你们需要的操作基本都在这里了，你们可以适当的进行学习。git系统本身是一个非常有用的版本控制器，如果日后会大量接触代码的，有一些了解还是很好的，可以进行一下尝试。

如果有问题欢迎私戳我，讲道理我也用的不是很6哈哈哈。