### 11.03 log
1. 看__1天搞定深度学习__文档

### 11.04 log
1. 看__1天搞定深度学习__文档
2. 配置[Keras深度学习框架](http://www.jianshu.com/p/b8a703df5318)

### 11.07 log
1. 看__1天搞定深度学习__文档P61-P114
	* 利用Keras框架识别手写体案例	define a set of funtion→goodness of funtion→pick the best funtion
	* Tips for Training DNN 
		* Choosing proper loss
		* Mini-batch(分批处理)
		* New activation function(rectified linear function，f(x)=max(0,x))
		* Adaptive Learning Rate(Set the learning rate η carefully)
		* Momentum(一定几率避免陷入局部最小和saddle point)
2. 学习[MarkDown语法](https://coding.net/help/doc/project/markdown.html#section-7)

### 11.08 log
1. 看__1天搞定深度学习__文档P115-P148
	* A solution for Overfitting
		* Early Stopping
		* Weight Decay(prunes out the useless link)
		* Dropout(Each time before updating the parameters 
		 _Each neuron has p% to dropout_ 
		_Using the new network for training_)
		* Network Structure(CNN is a very good example)
2. 看[计算机网络知识](http://www.jianshu.com/p/21b5cbac0849)		

## 11.09 log
1. 看__1天搞定深度学习__文档P149-P195
	* CNN for image
		* Do almost the same thing They can use the same set of parameters
		* Subsampling the pixels will not change the object
	    * eg.CNN for playing Go	
	* RNN
	* Bidirectional RNN

## 11.10 log
1. 看__1天搞定深度学习__文档
	* LSTM	
2. 看论文__改进BP神经网络在物体识别中的应用__

## 11.11 log
1. 看论文__改进BP神经网络在物体识别中的应用__
	* BP网络结构的改进
		* 隐层节点数 = (输入层节点数 + max(输出层节点数，待分类识别的物体类别数)) /2
		* 隐含层各神经元增加自反馈，考虑了上次迭代权值的影响，具有更好的适应性和泛化能力
	* BP算法的改进
		* 改变步长: 在误差变化较缓和处，合理加大步长来加快收敛速度; 在误差变化较急剧处，适当减小步
长以保证其精度。
		* 加入 γ{_p\^i }因子 
	* 提取物体特征：修正不变矩方法	
	* 用 Coil-20 图像数据库进行实验
2. 学习[Keras框架相关知识](http://www.open-open.com/lib/view/open1430982565991.html)	
	* Keras里的模块
		* Optimizers 包含了一些优化的方法，比如最基本的随机梯度下降SGD,Adagrad、Adadelta、RMSprop、Adam,一些新的方法以后也会被不断添加进来
		* Objectives 目标函数模块，keras提供了mean_squared_error，mean_absolute_error ，squared_hinge，hinge，binary_crossentropy，categorical_crossentropy这几种目标函数。	
		* Activations 激活函数模块，keras提供了linear、sigmoid、hard_sigmoid、tanh、softplus、relu、 softplus，另外softmax也放在Activations模块里
		* Initializations 参数初始化模块，在添加layer的时候调用init进行初始化。keras提供了uniform、lecun_uniform、normal、orthogonal、zero、glorot_normal、he_normal这几种。
		* layers 模块包含了core、convolutional、recurrent、advanced_activations、normalization、embeddings这几种layer。
		* Preprocessing 预处理模块，包括序列数据的处理，文本数据的处理，图像数据的处理。重点看一下图像数据的处理，keras提供了 ImageDataGenerator函数,实现data augmentation，数据集扩增，对图像做一些弹性变换，比如水平翻转，垂直翻转，旋转等。
		* Models 最主要的模块，模型。上面定义了各种基本组件，model是将它们组合起来。
	* 机器学习的一些[实例](https://github.com/wepe/MachineLearning)	

## 11.12 log
1. 看利用keras框架构建一个三个卷积层的CNN的例子
2. 运行一个案例CNN识别手写字符 （minist数据库）
	遇到的问题：spyder无论什么代码都报错

## 11.13 log
1. 看[keras中文文档]（http://keras-cn.readthedocs.io/en/latest/）
2. 运行案例时总是失败，估计是环境的问题，重新安装了系统

## 11.14 log
1. 看[keras中文文档](http://keras-cn.readthedocs.io/en/latest/)
2. 配置相关环境

## 11.15 log
1. 看__keras中文文档__
	* Keras有两种类型的模型，顺序模型（Sequential）和泛型模型（Model）

## 11.16 log
1. 用keras搭建了一个简单的神经网络[__代码__](https://github.com/i-am-js/test/blob/master/HandwritingRecognition.py)
2. 了解[云机器人相关知识](https://en.wikipedia.org/wiki/Cloud_robotics)

## 11.17log
1. 看论文**云机器人概念架构与关键技术研究综述**
2. 研究机器人抓取的[代码](https://github.com/i-am-js/test/tree/69dec52b8345012a77ba43bcb909c5b1c9d5559a/PickRubbishTest)

## 11.18.log
1. 看论文**基于视觉伺服的仿人机器人智能抓取技术研究** 2013 硕士
- 论文对目标图像图像的进行边缘检测，通过圆拟合得到质心坐标，放弃传统的单目视觉定位目标定位的方法，文中改进的采用BP神经网络得到目标质心坐标和目标相对于摄像机的坐标之间的关系

## 11.21.log
1. 看论文**基于视觉伺服的仿人机器人智能抓取技术研究** 2013 硕士
2. 修改小论文

## 11.22.log
1. 看论文 **基于模糊控制的NAO机器人目标跟踪与抓取**
- 文中在是机器人摄像头成像平面垂直的方向上加了一个摄像头，组成一个视觉系统
2. 研究机器人抓取的代码
3. [学习python多线程知识](http://www.runoob.com/python/python-multithreading.html)
- Python通过两个标准库thread和threading提供对线程的支持

## 11.23.log
1. 研究机器人抓取的代码

## 11.24.log
1. 研究机器人抓取的代码并写注释
2. 修改小论文
## 11.28.log
1. 制作开题报告的幻灯片

## 11.29.log
1. 制作开题报告的幻灯片
2. [系统学习sublime的使用](http://www.imooc.com/learn/40/)
3. 看论文 **Integration of the Humanoid Robot Nao inside a Smart
Home: A Case Study**

## 11.30.log
1. 修改开题报告的幻灯片
2. 看论文 **Integration of the Humanoid Robot Nao inside a Smart
Home: A Case Study**