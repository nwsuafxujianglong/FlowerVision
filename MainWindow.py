
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 260, 491, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 50, 491, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 110, 491, 121))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.widget1)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_1.clicked.connect(self.choose_file_1)
        self.pushButton_2.clicked.connect(self.choose_file_2)
        self.pushButton_3.clicked.connect(self.choose_file_3)
        self.pushButton_4.clicked.connect(self.choose_file_4)
        self.pushButton.clicked.connect(self.run)

    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self,'选择文件','','*')
        return filename

    def show_image(self, filename, label):
        image = QImage(filename)
        image = image.scaled(label.width(), label.height())
        label.setPixmap(QPixmap.fromImage(image))

    def choose_file_1(self):
        filename = self.choose_file()
        self.show_image(filename, self.label_1)
        self.path1 = filename

    def choose_file_2(self):
        filename = self.choose_file()
        self.show_image(filename, self.label_2)
        self.path2 = filename

    def choose_file_3(self):
        filename = self.choose_file()
        self.show_image(filename, self.label_3)
        self.path3 = filename

    def choose_file_4(self):
        filename = self.choose_file()
        self.show_image(filename, self.label_4)
        self.path4 = filename

    def run(self):
        from skimage import io,transform
        import tensorflow as tf
        import numpy as np

        flower_dict = {0:'dasiy',1:'dandelion',2:'roses',3:'sunflowers',4:'tulips'}

        w=100
        h=100
        c=3

        def read_one_image(path):
            img = io.imread(path)
            img = transform.resize(img,(w,h))
            return np.asarray(img)

        with tf.Session() as sess:
            data = []
            data1 = read_one_image(self.path1)
            data2 = read_one_image(self.path2)
            data3 = read_one_image(self.path3)
            data4 = read_one_image(self.path4)
            data.append(data1)
            data.append(data2)
            data.append(data3)
            data.append(data4)

            saver = tf.train.import_meta_graph('F:/Python/ComputerVision/CvData/flowers/model.ckpt.meta')
            saver.restore(sess,tf.train.latest_checkpoint('F:/Python/ComputerVision/CvData/flowers/'))

            graph = tf.get_default_graph()
            x = graph.get_tensor_by_name("x:0")
            feed_dict = {x:data}

            logits = graph.get_tensor_by_name("logits_eval:0")

            classification_result = sess.run(logits,feed_dict)

            #print(classification_result)
   
            #print(tf.argmax(classification_result,1).eval())
  
            output = []
            output = tf.argmax(classification_result,1).eval()
            for i in range(len(output)):
                print("Number",i+1,"Flowers:"+flower_dict[output[i]])

            self.label_6.setText(flower_dict[output[0]])
            self.label_5.setText(flower_dict[output[1]])
            self.label_7.setText(flower_dict[output[2]])
            self.label_8.setText(flower_dict[output[3]])
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "识别"))
        self.pushButton_1.setText(_translate("MainWindow", "选择图片1"))
        self.pushButton_2.setText(_translate("MainWindow", "选择图片2"))
        self.pushButton_3.setText(_translate("MainWindow", "选择图片3"))
        self.pushButton_4.setText(_translate("MainWindow", "选择图片4"))

