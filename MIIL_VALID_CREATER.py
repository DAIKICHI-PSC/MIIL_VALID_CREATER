# -*- coding: utf-8 -*-

import os #OS関連処理用モジュールの読込
import sys #システム関連処理用モジュールの読込
import time #時間関連処理用モジュールの読込
import numpy as np #行列処理用モジュールの読込
import math as mt #各種計算用モジュールの読込
import cv2 #画像処理用モジュールの読込
import glob #ファイルパス一括取得用モジュールの読込
from PySide2 import QtCore, QtGui, QtWidgets #GUI関連処理用モジュールの読込
from MIIL_VALID_CREATER_GUI import Ui_MainWindow #QT Designerで作成し変換したファイルの読込
from getRectanglePos import getRectanglePos #２点の何れかが選択領域の開始点（左上）になり、終点（左下）になるか判定し、さらに終点が指定した範囲にあるかるか確認するライブラリ

#####グローバル変数########################################
capLoop = 0 #動画を表示中か判定するフラグ

######フレームワーク以外のグローバル変数変数########################################
DirPath = "" #写真が保存してあるフォルダパスを記憶
SettingDataDir = "" #領域生データ保存用フォルダ
AnnotationDir = "" #アノテーションデータ保存用フォルダ

SettingList1 = [] #画像内の各認識対象物の領域情報保存用リスト
CurPic1 = "" #読込んだ画像データ
CurPicWidath1 = 0 #読込んだ画像の横サイズを記憶
CurPicHeight1 = 0 #読込んだ画像の縦サイズを記憶
LWEventCancel1 = 0 #リストウィジットのイベントキャンセル用フラグ

SettingList2 = [] #画像内の各認識対象物の領域情報保存用リスト
CurPic2 = "" #読込んだ画像データ
CurPicWidath2 = 0 #読込んだ画像の横サイズを記憶
CurPiHeight2 = 0 #読込んだ画像の縦サイズを記憶
LWEventCancel2 = 0 #リストウィジットのイベントキャンセル用フラグ

SettingList3 = [] #画像内の各認識対象物の領域情報保存用リスト
CurPic3 = "" #読込んだ画像データ
CurPicWidath3 = 0 #読込んだ画像の横サイズを記憶
CurPiHeight3 = 0 #読込んだ画像の縦サイズを記憶
LWEventCancel3 = 0 #リストウィジットのイベントキャンセル用フラグ

TrainData = "" #トレーニングデータパス一覧ファイルまでのパスを記憶
ValidData = "" #教師データパス一覧ファイルまでのパスを記憶

#####各種処理用関数########################################
#=====メインループ処理========================================
##########
#リストウィジットで選択されている写真に領域を描画して表示する処理
##########
def mainLoop():

    global DirPath
    global CurPic1
    global CurPicWidath1
    global CurPicHeight1
    global CurPic2
    global CurPicWidath2
    global CurPicHeight2
    global CurPic3
    global CurPicWidath3
    global CurPicHeight3

    while(capLoop == 1):
        frame1 = np.copy(CurPic1) #画像データをnumyでコピー
        frame2 = np.copy(CurPic2) #画像データをnumyでコピー
        frame3 = np.copy(CurPic3) #画像データをnumyでコピー
        if capLoop == 1: #画像表示モードか確認
            #!!!!!!!!!!openCVの処理は此処で行う!!!!!!!!!!

            currentListIndex1 = win.ui.listWidget1.currentRow() #リスウィジットの現在の行番号を記憶
            currentListIndex2 = win.ui.listWidget2.currentRow() #リスウィジットの現在の行番号を記憶
            currentListIndex3 = win.ui.listWidget3.currentRow() #リスウィジットの現在の行番号を記憶

            if len(SettingList1) > 0: #認識対象物の領域データが配列にあるか確認
                for x in SettingList1: #領域データ毎に処理
                    ROW, LABEL,TX, TY, BX, BY = x.split(',') #領域データを取得
                    cv2.rectangle(frame1, (int(TX), int(TY)), (int(BX), int(BY)), (0, 255, 0), 1) #領域を画像データに書込み
                    font_size = 1 #フォントサイズを設定
                    font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                    cv2.putText(frame1, LABEL,(int(TX) + 2, int(TY) - 2),font, font_size,(0,255,0),1) #認識対象物のラベルを画像データに書込み
            elif currentListIndex1 != -1: #認識対象物の領域データがない場合
                cv2.rectangle(frame1, (0, 0), (CurPicWidath1 - 1, CurPicHeight1 - 1), (0, 0, 255), 1) #画像データ画像外周に領域を書込み
                font_size = 1 #フォントサイズを設定
                font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                cv2.putText(frame1, 'EXCLUDE', (10, 20),font, font_size,(0,0,255),1) #除外の文字を画像データに書込み

            if len(SettingList2) > 0: #認識対象物の領域データが配列にあるか確認
                for x in SettingList2: #領域データ毎に処理
                    ROW, LABEL,TX, TY, BX, BY = x.split(',') #領域データを取得
                    cv2.rectangle(frame2, (int(TX), int(TY)), (int(BX), int(BY)), (0, 255, 0), 1) #領域を画像データに書込み
                    font_size = 1 #フォントサイズを設定
                    font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                    cv2.putText(frame2, LABEL,(int(TX) + 2, int(TY) - 2),font, font_size,(0,255,0),1) #認識対象物のラベルを画像データに書込み
            elif currentListIndex2 != -1: #認識対象物の領域データがない場合
                cv2.rectangle(frame2, (0, 0), (CurPicWidath2 - 1, CurPicHeight2 - 1), (0, 0, 255), 1) #画像データ画像外周に領域を書込み
                font_size = 1 #フォントサイズを設定
                font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                cv2.putText(frame2, 'EXCLUDE', (10, 20),font, font_size,(0,0,255),1) #除外の文字を画像データに書込み

            if len(SettingList3) > 0: #認識対象物の領域データが配列にあるか確認
                for x in SettingList3: #領域データ毎に処理
                    ROW, LABEL,TX, TY, BX, BY = x.split(',') #領域データを取得
                    cv2.rectangle(frame3, (int(TX), int(TY)), (int(BX), int(BY)), (0, 255, 0), 1) #領域を画像データに書込み
                    font_size = 1 #フォントサイズを設定
                    font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                    cv2.putText(frame3, LABEL,(int(TX) + 2, int(TY) - 2),font, font_size,(0,255,0),1) #認識対象物のラベルを画像データに書込み
            elif currentListIndex3 != -1: #認識対象物の領域データがない場合
                cv2.rectangle(frame3, (0, 0), (CurPicWidath3 - 1, CurPicHeight3 - 1), (0, 0, 255), 1) #画像データ画像外周に領域を書込み
                font_size = 1 #フォントサイズを設定
                font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                cv2.putText(frame3, 'EXCLUDE', (10, 20),font, font_size,(0,0,255),1) #除外の文字を画像データに書込み

            app.processEvents() #ループ中にストックされたＯＳの処理を実行（ボタン処理のタイミング確認用）
            if capLoop == 1: #画像表示モードか確認
                if currentListIndex1 != -1: #認識対象物の領域データが配列にあるか確認
                    cv2.imshow("FILE",frame1) #画像を表示
                else:
                    try:
                        cv2.destroyWindow("FILE") #認識対象物の領域データがない場合は画像を消去
                    except:
                        pass
                if currentListIndex2 != -1: #認識対象物の領域データが配列にあるか確認
                    cv2.imshow("TRAIN",frame2) #画像を表示
                else:
                    try:
                        cv2.destroyWindow("TRAIN") #認識対象物の領域データがない場合は画像を消去
                    except:
                        pass
                if currentListIndex3 != -1: #認識対象物の領域データが配列にあるか確認
                    cv2.imshow("VALID",frame3) #画像を表示
                else:
                    try:
                        cv2.destroyWindow("VALID") #認識対象物の領域データがない場合は画像を消去
                    except:
                        pass
        else:
            break
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        app.processEvents()

#####Pysideのウィンドウ処理クラス########################################
class MainWindow1(QtWidgets.QMainWindow): #QtWidgets.QMainWindowを継承
#=====GUI用クラス継承の定型文========================================
    def __init__(self, parent = None): #クラス初期化時にのみ実行される関数（コンストラクタと呼ばれる）
        super(MainWindow1, self).__init__(parent) #親クラスのコンストラクタを呼び出す（親クラスのコンストラクタを再利用したい場合）　指定する引数は、親クラスのコンストラクタの引数からselfを除いた引数
        self.ui = Ui_MainWindow() #uiクラスの作成。Ui_MainWindowのMainWindowは、QT DesignerのobjectNameで設定した名前
        self.ui.setupUi(self) #uiクラスの設定
        #-----シグナルにメッソドを関連付け----------------------------------------
        self.ui.listWidget1.currentRowChanged.connect(self.listWidget1_changed) #listWidget1_changedは任意
        self.ui.listWidget2.currentRowChanged.connect(self.listWidget2_changed) #listWidget2_changedは任意
        self.ui.listWidget3.currentRowChanged.connect(self.listWidget3_changed) #listWidget3_changedは任意
        QtCore.QObject.connect(self.ui.pushButton1, QtCore.SIGNAL("clicked()"), self.pushButton1_clicked) #pushButton1_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton2, QtCore.SIGNAL("clicked()"), self.pushButton2_clicked) #pushButton2_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton3, QtCore.SIGNAL("clicked()"), self.pushButton3_clicked) #pushButton1_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton4, QtCore.SIGNAL("clicked()"), self.pushButton4_clicked) #pushButton4_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton5, QtCore.SIGNAL("clicked()"), self.pushButton5_clicked) #pushButton5_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton6, QtCore.SIGNAL("clicked()"), self.pushButton6_clicked) #pushButton6_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton7, QtCore.SIGNAL("clicked()"), self.pushButton7_clicked) #pushButton7_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton8, QtCore.SIGNAL("clicked()"), self.pushButton8_clicked) #pushButton8_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton9, QtCore.SIGNAL("clicked()"), self.pushButton9_clicked) #pushButton9_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton10, QtCore.SIGNAL("clicked()"), self.pushButton10_clicked) #pushButton10_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton11, QtCore.SIGNAL("clicked()"), self.pushButton11_clicked) #pushButton11_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton12, QtCore.SIGNAL("clicked()"), self.pushButton12_clicked) #pushButton12_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton13, QtCore.SIGNAL("clicked()"), self.pushButton13_clicked) #pushButton13_clickedは任意
        QtCore.QObject.connect(self.ui.pushButton14, QtCore.SIGNAL("clicked()"), self.pushButton14_clicked) #pushButton14_clickedは任意

#=====ウィジットのシグナル処理用メッソド========================================
    #-----listWidget1用イベント処理----------------------------------------
    ##########
    #リストウィジットの行が変更されたら新たに選択されたアイテムの情報を読込む
    ##########
    def listWidget1_changed(self):

        global SettingDataDir
        global SettingList1
        global CurPic1
        global CurPicWidath1
        global CurPicHeight1

        currentListIndex = self.ui.listWidget1.currentRow() #リストウィジットの現在選択されている行番号を取得
        if LWEventCancel1 == 0 and currentListIndex != -1: #listWidget1のイベント処理が可能な場合
            SettingList1.clear() #配列をクリア
            picpath = DirPath + '/' + self.ui.listWidget1.currentItem().text() + '.jpg' #画像までのパスを記憶
            if os.path.isfile(picpath): #ファイルが存在するか確認
                CurPic1 = cv2.imread(picpath) #画像を読込む
                CurPicHeight1 = CurPic1.shape[0] #画像の高さを取得
                CurPicWidath1 = CurPic1.shape[1] #画像の幅を取得
                filepath = SettingDataDir + '/' + self.ui.listWidget1.currentItem().text() + '.set' #画像に対応する領域データまでのパスを取得
                if os.path.isfile(filepath): #ファイルが存在するか確認
                    #####ファイル名のみの取得
                    f = open(filepath, "r") #ファイルの読み込み開始
                    text = f.readlines() #データをリスト配列に格納（改行コードも含む）
                    f.close() #ファイルの読み込み終了
                    if len(text) > 0: #配列にデータがあるか確認
                        for setting in text: #配列からデータを個別に取得
                            SettingList1.append(setting.replace("\n", "")) #データから改行コードを削除後に領域データとしてリスト配列に追加
                    else:
                        msgbox = QtWidgets.QMessageBox(self)
                        msgbox.setWindowTitle("MVC")
                        msgbox.setText("Something is wrong with setting data.") #メッセージボックスのテキストを設定
                        ret = msgbox.exec_() #メッセージボックスを表示
                    #####
            else:
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("MVC")
                msgbox.setText("Something is wrong with picture data.") #メッセージボックスのテキストを設定
                ret = msgbox.exec_() #メッセージボックスを表示

    #-----listWidget2用イベント処理----------------------------------------
    ##########
    #リストウィジットの行が変更されたら新たに選択されたアイテムの情報を読込む
    ##########
    def listWidget2_changed(self):

        global SettingDataDir
        global SettingList2
        global CurPic2
        global CurPicWidath2
        global CurPicHeight2

        currentListIndex = self.ui.listWidget2.currentRow() #リストウィジットの現在選択されている行番号を取得
        if LWEventCancel2 == 0 and currentListIndex != -1: #listWidget1のイベント処理が可能な場合
            SettingList2.clear() #配列をクリア
            picpath = DirPath + '/' + self.ui.listWidget2.currentItem().text() + '.jpg' #画像までのパスを記憶
            if os.path.isfile(picpath): #ファイルが存在するか確認
                CurPic2 = cv2.imread(picpath) #画像を読込む
                CurPicHeight2 = CurPic2.shape[0] #画像の高さを取得
                CurPicWidath2 = CurPic2.shape[1] #画像の幅を取得
                filepath = SettingDataDir + '/' + self.ui.listWidget2.currentItem().text() + '.set' #画像に対応する領域データまでのパスを取得
                if os.path.isfile(filepath): #ファイルが存在するか確認
                    #####ファイル名のみの取得
                    f = open(filepath, "r") #ファイルの読み込み開始
                    text = f.readlines() #データをリスト配列に格納（改行コードも含む）
                    f.close() #ファイルの読み込み終了
                    if len(text) > 0: #配列にデータがあるか確認
                        for setting in text: #配列からデータを個別に取得
                            SettingList2.append(setting.replace("\n", "")) #データから改行コードを削除後に領域データとしてリスト配列に追加
                    else:
                        msgbox = QtWidgets.QMessageBox(self)
                        msgbox.setWindowTitle("MVC")
                        msgbox.setText("Something is wrong with setting data.") #メッセージボックスのテキストを設定
                        ret = msgbox.exec_() #メッセージボックスを表示
                    #####
            else:
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("MVC")
                msgbox.setText("Something is wrong with picture data.") #メッセージボックスのテキストを設定
                ret = msgbox.exec_() #メッセージボックスを表示

    #-----listWidget3用イベント処理----------------------------------------
    ##########
    #リストウィジットの行が変更されたら新たに選択されたアイテムの情報を読込む
    ##########
    def listWidget3_changed(self):

        global SettingDataDir
        global SettingList3
        global CurPic3
        global CurPicWidath3
        global CurPicHeight3

        currentListIndex = self.ui.listWidget3.currentRow() #リストウィジットの現在選択されている行番号を取得
        if LWEventCancel3 == 0 and currentListIndex != -1: #listWidget1のイベント処理が可能な場合
            SettingList3.clear() #配列をクリアー
            picpath = DirPath + '/' + self.ui.listWidget3.currentItem().text() + '.jpg' #画像までのパスを記憶
            if os.path.isfile(picpath): #ファイルが存在するか確認
                CurPic3 = cv2.imread(picpath) #画像を読込む
                CurPicHeight3 = CurPic3.shape[0] #画像の高さを取得
                CurPicWidath3 = CurPic3.shape[1] #画像の幅を取得
                filepath = SettingDataDir + '/' + self.ui.listWidget3.currentItem().text() + '.set' #画像に対応する領域データまでのパスを取得
                if os.path.isfile(filepath): #ファイルが存在するか確認
                    #####ファイル名のみの取得
                    f = open(filepath, "r") #ファイルの読み込み開始
                    text = f.readlines() #データをリスト配列に格納（改行コードも含む）
                    f.close() #ファイルの読み込み終了
                    if len(text) > 0: #配列にデータがあるか確認
                        for setting in text: #配列からデータを個別に取得
                            SettingList3.append(setting.replace("\n", "")) #データから改行コードを削除後に領域データとしてリスト配列に追加
                    else:
                        msgbox = QtWidgets.QMessageBox(self)
                        msgbox.setWindowTitle("MVC")
                        msgbox.setText("Something is wrong with setting data.") #メッセージボックスのテキストを設定
                        ret = msgbox.exec_() #メッセージボックスを表示
                    #####
            else:
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("MVC")
                msgbox.setText("Something is wrong with picture data.") #メッセージボックスのテキストを設定
                ret = msgbox.exec_() #メッセージボックスを表示

    #-----pushButton1用イベント処理----------------------------------------
    ##########
    #写真の表示を開始する
    ##########
    def pushButton1_clicked(self):
        global capLoop
        if self.ui.lineEdit1.text() == "": #パラメータファイルが選択されているか確認
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("Please set file path.") #メッセージボックスのテキストを設定
            ret = msgbox.exec_() #メッセージボックスを表示
        else:
            self.ui.pushButton1.setEnabled(False)
            self.ui.pushButton2.setEnabled(True)
            self.ui.pushButton3.setEnabled(False)
            if capLoop == 0:
                capLoop = 1 #ループ中とする
                mainLoop() #メインループ用関数を実行

    #-----pushButton2用イベント処理----------------------------------------
    ##########
    #写真の表示を終了する
    ##########
    def pushButton2_clicked(self):
        global capLoop
        if capLoop == 1:
            capLoop = 0 #ループ中ではないとする
            time.sleep(0.2)
        self.ui.pushButton1.setEnabled(True)
        self.ui.pushButton2.setEnabled(False)
        self.ui.pushButton3.setEnabled(True)
        #cap.release()
        cv2.destroyAllWindows() #画像表示用のウィンドウを全て閉じる。

    #-----pushButton3用イベント処理----------------------------------------
    ##########
    #パラメータファイルの読込
    #写真ファイル（学習データと教師データに使用されていない物）・学習データファイル・教師データファイルを各リストウィジットに一覧表示する
    ##########
    def pushButton3_clicked(self):
        global DirPath #写真が保存してあるフォルダパスを記憶
        global SettingDataDir
        global AnnotationDir
        global LWEventCancel1
        global LWEventCancel2
        global LWEventCancel3
        global TrainData
        global ValidData

    #####ファイル読込み
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",'prm File (*.prm)') #パラメータファイルを選択
        if filepath: #ファイルが存在するか確認
            f = open(filepath, "r") #ファイルの読み込み開始
            textList1 = ""
            textList1 = f.readlines() #テキストを一行ずつ配列として読込む（行の終わりの改行コードも含めて読込む）
            f.close() #ファイルの読み込み終了
            if ("train = " in textList1[1]) == False: #パラメータファイル内にtrain = の記述がない場合の処理
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("MVC")
                msgbox.setText("Wrone file read.")
                ret = msgbox.exec_()
            else: #パラメータファイル内にtrain = の記述がある場合の処理
                textList1[1] = textList1[1].replace("\n", "") #データから改行コードを削除
                textList1[1] = textList1[1].replace("\r", "") #データから改行コードを削除
                textList1[1] = textList1[1].replace("train = ", "") #データからtrain = を削除
                TrainData = textList1[1] #学習データ一覧ファイルまでのパスを設定
                textList1[2] = textList1[2].replace("\n", "") #データから改行コードを削除
                textList1[2] = textList1[2].replace("\r", "") #データから改行コードを削除
                textList1[2] = textList1[2].replace("valid = ", "") #データからvalid = を削除
                ValidData = textList1[2] #教師データ一覧ファイルまでのパスを設定

                if os.path.isfile(TrainData): #ファイルが存在するか確認
                    f = open(TrainData, "r") #ファイルの読み込み開始
                    textList2 = ""
                    textList2 = f.readlines() #学習データ一覧から各ファイルパスを読込（行の終わりの改行コードも含めて読込む）
                    f.close() #ファイルの読み込み終了
                else: #ファイルが存在しない場合
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setWindowTitle("MVC")
                    msgbox.setText("Something is wrong with training data path in parameter file.")
                    ret = msgbox.exec_()

                if os.path.isfile(ValidData): #ファイルが存在するか確認
                    f = open(ValidData, "r") #ファイルの読み込み開始
                    textList3 = ""
                    textList3 = f.readlines() #教師データ一覧から各ファイルパスを読込（行の終わりの改行コードも含めて読込む）
                    f.close() #ファイルの読み込み終了
                else: #ファイルが存在しない場合
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setWindowTitle("MVC")
                    msgbox.setText("Something is wrong with valid data path in parameter file.")
                    ret = msgbox.exec_()

                SplitPath = textList2[0].rsplit('/', 1) #読込んだテキストの一覧の一行目から、ディレクトリのパスを取得
                DirPath = SplitPath[0] #ディレクトリのパスを取得
                if DirPath == "": #ディレクトリのパスがない場合の処理
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setWindowTitle("MVC")
                    msgbox.setText("No data found.")
                    ret = msgbox.exec_()
                else: #ディレクトリのパスがある場合の処理
                    LWEventCancel1 = 1 #listWidget1のイベント発生時に処理をしないようにする。
                    LWEventCancel2 = 1 #listWidget2のイベント発生時に処理をしないようにする。
                    LWEventCancel3 = 1 #listWidget3のイベント発生時に処理をしないようにする。
                    self.ui.listWidget1.clear() #リストウィジットのアイテムをクリア
                    self.ui.listWidget2.clear() #リストウィジットのアイテムをクリア
                    self.ui.listWidget3.clear() #リストウィジットのアイテムをクリア
                    self.ui.lineEdit1.setText(DirPath) #フォルダパスを表示

                    DN = DirPath.rsplit('/', 1) #フォルダパスの文字列右側から指定文字列で分割
                    SettingDataDir = DN[0] + '/' + DN[1] + '_setting' #セッティングデータを格納するフォルダまでのパスを記憶

                    NumList1 = [] #ファイルの連番名記憶用リスト
                    FileList = glob.glob(DirPath + '/*.jpg') #フォルダ内の各ファイルパスをリスト形式で取得
                    for FN in FileList: #各JPGファイルパスを取得
                        FN1 = FN.rsplit(".", 1) #ファイルパスの文字列右側から指定文字列で分割
                        FN1[0] = FN1[0].replace('\\', '/') #globのバグを修正
                        if os.path.isfile(FN1[0] + '.txt') == False: #JPGファイルと同じ名前のTXTファイルがない場合の処理
                            f = open(FN1[0] + '.txt', "w") #ファイルの書き込み開始
                            f.write('') #空ファイルとして書込み
                            f.close() #ファイルの書き込み終了
                        FN2 = FN1[0].rsplit('/', 1) #ファイルパスの文字列右側から指定文字列で分割
                        NumList1.append(int(FN2[1])) #ファイルの連番名を取得
                    NumList1.sort() #データの並びを連番にする

                    NumList2 = [] #ファイルの連番名記憶用リスト
                    f = open(TrainData, "r")  #ファイルの読み込み開始
                    textList1 = ""
                    textList1 = f.readlines() #パラメータ内のtrainパスからファイルパスを読込（行の終わりの改行コードも含めて読込む）
                    f.close() #ファイルの読み込み終了
                    if len(textList1) > 0: #ファイルパスが一つ以上あるか確認
                        for x in textList1: #ファイルパスを一行ずつ取得
                            x = x.replace("\n", "") #データから改行コードを削除
                            x = x.replace("\r", "") #データから改行コードを削除
                            y = x.rsplit(".", 1) #拡張子前の.で文字列を分離
                            z = y[0].rsplit("/", 1) #ファイル名前の/で文字列を分離
                            NumList2.append(int(z[1])) #学習データをして使用するファイル名をリスト配列に追加
                            NumList1.remove(int(z[1])) #学習データとして使用するファイル名をファイル一覧から削除
                        NumList2.sort() #データの並びを連番にする

                    NumList3 = [] #ファイルの連番名記憶用リスト
                    f = open(ValidData, "r")  #ファイルの読み込み開始
                    textList2 = ""
                    textList2 = f.readlines() #パラメータ内のtrainパスからファイルパスを読込（行の終わりの改行コードも含めて読込む）
                    f.close() #ファイルの読み込み終了
                    if len(textList2) > 0: #ファイルパスが一つ以上あるか確認
                        for x in textList2: #ファイルパスを一行ずつ取得
                            x = x.replace("\n", "") #データから改行コードを削除
                            x = x.replace("\r", "") #データから改行コードを削除
                            y = x.rsplit(".", 1) #拡張子前の.で文字列を分離
                            z = y[0].rsplit("/", 1) #ファイル名前の/で文字列を分離
                            NumList3.append(int(z[1])) #教師データをして使用するファイル名をリスト配列に追加
                            NumList1.remove(int(z[1])) #教師データとして使用するファイル名をファイル一覧から削除
                        NumList3.sort() #データの並びを連番にする

                    if len(NumList1) > 0: #ファイルパスが一つ以上あるか確認
                        for x in NumList1: #ファイルパスを一行ずつ取得
                            self.ui.listWidget1.addItem(str(x)) #リストウィジットにアイテムとして追加
                        LWEventCancel1 = 0 #listWidget1のイベント発生時に処理を行うようにする
                        self.ui.listWidget1.setCurrentRow(0) #リストウィジットの最初のアイテムを選択
                    else:
                        LWEventCancel1 = 0 #listWidget1のイベント発生時に処理を行うようにする

                    if len(NumList2) > 0: #ファイルパスが一つ以上あるか確認
                        for x in NumList2: #ファイルパスを一行ずつ取得
                            self.ui.listWidget2.addItem(str(x)) #リストウィジットにアイテムとして追加
                        LWEventCancel2 = 0 #listWidget2のイベント発生時に処理を行うようにする
                        self.ui.listWidget2.setCurrentRow(0) #リストウィジットの最初のアイテムを選択
                    else:
                        LWEventCancel2 = 0 #listWidget2のイベント発生時に処理を行うようにする

                    if len(NumList3) > 0: #ファイルパスが一つ以上あるか確認
                        for x in NumList3: #ファイルパスを一行ずつ取得
                            self.ui.listWidget3.addItem(str(x)) #リストウィジットにアイテムとして追加
                        LWEventCancel3 = 0 #listWidget3のイベント発生時に処理を行うようにする
                        self.ui.listWidget3.setCurrentRow(0) #リストウィジットの最初のアイテムを選択
                    else:
                        LWEventCancel3 = 0 #listWidget3のイベント発生時に処理を行うようにする

    #-----pushButton4用イベント処理----------------------------------------
    ##########
    #listWidget1のアイテムをlistWidget2に移動
    ##########
    def pushButton4_clicked(self):
        currentListIndex = self.ui.listWidget1.currentRow() #リストウィジットの現在の行番号を取得
        if currentListIndex == -1: #リストウィジットのアイテムが選択されていない場合
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data selected.")
            ret = msgbox.exec_()
        else: #リストウィジットのアイテムが選択されている場合
            self.ui.listWidget2.addItem(self.ui.listWidget1.currentItem().text()) #listWidget1のアイテムをlistWidget2に追加
            self.ui.listWidget1.takeItem(self.ui.listWidget1.currentRow()) #listWidget1のアイテムを削除
            self.ui.listWidget2.setCurrentRow(self.ui.listWidget2.count() - 1) #listWidget2の最後のアイテムを選択
            text = ""
            for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(TrainData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了

    #-----pushButton5用イベント処理----------------------------------------
    ##########
    #listWidget1のアイテムをlistWidget3に移動
    ##########
    def pushButton5_clicked(self):
        currentListIndex = self.ui.listWidget1.currentRow() #リストウィジットの現在の行番号を取得
        if currentListIndex == -1: #リストウィジットのアイテムが選択されていない場合
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data selected.")
            ret = msgbox.exec_()
        else: #リストウィジットのアイテムが選択されている場合
            self.ui.listWidget3.addItem(self.ui.listWidget1.currentItem().text()) #listWidget1のアイテムをlistWidget3に追加
            self.ui.listWidget1.takeItem(self.ui.listWidget1.currentRow()) #listWidget1のアイテムを削除
            self.ui.listWidget3.setCurrentRow(self.ui.listWidget3.count() - 1) #listWidget3の最後のアイテムを選択
            text = ""
            for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(ValidData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了

    #-----pushButton6用イベント処理----------------------------------------
    ##########
    #listWidget2のアイテムをlistWidget3に移動
    ##########
    def pushButton6_clicked(self):
        currentListIndex = self.ui.listWidget2.currentRow() #リストウィジットの現在の行番号を取得
        if currentListIndex == -1: #リストウィジットのアイテムが選択されていない場合
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data selected.")
            ret = msgbox.exec_()
        else: #リストウィジットのアイテムが選択されている場合
            self.ui.listWidget3.addItem(self.ui.listWidget2.currentItem().text()) #listWidget2のアイテムをlistWidget3に追加
            self.ui.listWidget2.takeItem(self.ui.listWidget2.currentRow()) #listWidget2のアイテムを削除
            self.ui.listWidget3.setCurrentRow(self.ui.listWidget3.count() - 1) #listWidget3の最後のアイテムを選択
            text = ""
            for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(TrainData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close()
            text = ""
            for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(ValidData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了

    #-----pushButton7用イベント処理----------------------------------------
    ##########
    #listWidget2のアイテムをlistWidget1に移動
    ##########
    def pushButton7_clicked(self):
        currentListIndex = self.ui.listWidget2.currentRow() #リストウィジットの現在の行番号を取得
        if currentListIndex == -1: #リストウィジットのアイテムが選択されていない場合
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data selected.")
            ret = msgbox.exec_()
        else: #リストウィジットのアイテムが選択されている場合
            self.ui.listWidget1.addItem(self.ui.listWidget2.currentItem().text()) #listWidget2のアイテムをlistWidget1に追加
            self.ui.listWidget2.takeItem(self.ui.listWidget2.currentRow()) #listWidget2のアイテムを削除
            self.ui.listWidget1.setCurrentRow(self.ui.listWidget1.count() - 1) #listWidget3の最後のアイテムを選択
            text = ""
            for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(TrainData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了

    #-----pushButton8用イベント処理----------------------------------------
    ##########
    #listWidget3のアイテムをlistWidget2に移動
    ##########
    def pushButton8_clicked(self):
        currentListIndex = self.ui.listWidget3.currentRow() #リストウィジットの現在の行番号を取得
        if currentListIndex == -1: #リストウィジットのアイテムが選択されていない場合
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data selected.")
            ret = msgbox.exec_()
        else: #リストウィジットのアイテムが選択されている場合
            self.ui.listWidget2.addItem(self.ui.listWidget3.currentItem().text()) #listWidget3のアイテムをlistWidget2に追加
            self.ui.listWidget3.takeItem(self.ui.listWidget3.currentRow()) #listWidget3のアイテムを削除
            self.ui.listWidget2.setCurrentRow(self.ui.listWidget2.count() - 1) #listWidget2の最後のアイテムを選択
            text = ""
            for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(TrainData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了
            text = ""
            for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(ValidData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了

    #-----pushButton9用イベント処理----------------------------------------
    ##########
    #listWidget3のアイテムをlistWidget1に移動
    ##########
    def pushButton9_clicked(self):
        currentListIndex = self.ui.listWidget3.currentRow() #リストウィジットの現在の行番号を取得
        if currentListIndex == -1: #リストウィジットのアイテムが選択されていない場合
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data selected.")
            ret = msgbox.exec_()
        else: #リストウィジットのアイテムが選択されている場合
            self.ui.listWidget1.addItem(self.ui.listWidget3.currentItem().text()) #listWidget3のアイテムをlistWidget1に追加
            self.ui.listWidget3.takeItem(self.ui.listWidget3.currentRow()) #listWidget3のアイテムを削除
            self.ui.listWidget1.setCurrentRow(self.ui.listWidget1.count() - 1) #listWidget1の最後のアイテムを選択
            text = ""
            for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg\n" #リストウィジットのアイテムをファイルパスとしてリスト配列に追加
            f = open(ValidData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了

    #-----pushButton10用イベント処理----------------------------------------
    ##########
    #listWidget1のアイテムを整列
    ##########
    def pushButton10_clicked(self):
        if self.ui.listWidget1.count() > 0: #リストウィジットのアイテムが一つ以上あるか確認
            text = []
            for CurRow in range(self.ui.listWidget1.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text.append(int(self.ui.listWidget1.item(CurRow).text())) #リストウィジットのアイテムを数値としてリスト配列に追加
            text.sort() #数値を整列
            self.ui.listWidget1.clear() #リストウィジットの全アイテムを削除
            for x in text: #リスト配列から各要素を取得
                self.ui.listWidget1.addItem(str(x)) #リストウィジットにアイテムを追加
            self.ui.listWidget1.setCurrentRow(0) #リストウィジットの最初のアイテムを選択
        else:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data.")
            ret = msgbox.exec_()

    #-----pushButton11用イベント処理----------------------------------------
    ##########
    #listWidget2のアイテムを整列
    ##########
    def pushButton11_clicked(self):
        if self.ui.listWidget2.count() > 0: #リストウィジットのアイテムが一つ以上あるか確認
            text = []
            for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text.append(int(self.ui.listWidget2.item(CurRow).text())) #リストウィジットのアイテムを数値としてリスト配列に追加
            text.sort() #数値を整列
            self.ui.listWidget2.clear() #リストウィジットの全アイテムを削除
            for x in text: #リスト配列から各要素を取得
                self.ui.listWidget2.addItem(str(x)) #リストウィジットにアイテムを追加
            text = ""
            for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg\n" #数値をファイルパスとしてリスト配列に追加
            f = open(TrainData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了
            self.ui.listWidget2.setCurrentRow(0) #リストウィジットの最初のアイテムを選択
        else:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data.")
            ret = msgbox.exec_()

    #-----pushButton12用イベント処理----------------------------------------
    ##########
    #listWidget3のアイテムを整列
    ##########
    def pushButton12_clicked(self):
        if self.ui.listWidget3.count() > 0: #リストウィジットのアイテムが一つ以上あるか確認
            text = []
            for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text.append(int(self.ui.listWidget3.item(CurRow).text())) #リストウィジットのアイテムを数値としてリスト配列に追加
            text.sort() #数値を整列
            self.ui.listWidget3.clear() #リストウィジットの全アイテムを削除
            for x in text: #リスト配列から各要素を取得
                self.ui.listWidget3.addItem(str(x)) #リストウィジットにアイテムを追加
            text = ""
            for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                text = text + DirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg\n" #数値をファイルパスとしてリスト配列に追加
            f = open(ValidData, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルの書き込み
            f.close() #ファイルの書き込み終了
            self.ui.listWidget3.setCurrentRow(0) #リストウィジットの最初のアイテムを選択
        else:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MVC")
            msgbox.setText("No data.")
            ret = msgbox.exec_()

    #-----pushButton13用イベント処理----------------------------------------
    ##########
    #領域が描画された写真を選択したフォルダに全て保存
    ##########
    def pushButton13_clicked(self):
        msgbox = QtWidgets.QMessageBox(self)
        ret = msgbox.question(None, "MVC", "Save pictures with region to a folder?\nNOTICE : PLEASE CHOOSE A FOLDER WITH SINGLE BYTE CHARACTORS.", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) #選択用メッセージボックスを表示
        if ret == QtWidgets.QMessageBox.Yes: #メッセージボックスでYESが選択された場合
            DistDirPath = QtWidgets.QFileDialog.getExistingDirectory(self) #ディレクトリを選択
            if DistDirPath: #ディレクトリが選択されたか確認
                tmpSettingList2 = []
                for CurRow in range(self.ui.listWidget2.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                    picpath = DirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg" #アイテムをファイルパスとしてリスト配列に追加
                    if os.path.isfile(picpath): #ファイルが存在するか確認
                        tmpCurPic2 = cv2.imread(picpath) #画像を読込む
                        tmpCurPicHeight2 = CurPic2.shape[0] #画像の高さを取得
                        tmpCurPicWidath2 = CurPic2.shape[1] #画像の幅を取得
                        filepath = SettingDataDir + '/' + self.ui.listWidget2.item(CurRow).text() + '.set' #画像に対応する領域データまでのパスを取得
                        text = ""
                        if os.path.isfile(filepath): #ファイルが存在するか確認
                            #####ファイル名のみの取得
                            f = open(filepath, "r") #ファイルの読み込み開始
                            text = f.readlines() #データをリスト配列に格納（改行コードも含む）
                            f.close() #ファイルの読み込み終了
                        tmpSettingList2.clear() #配列をクリア
                        if len(text) > 0: #配列にデータがあるか確認
                            for setting in text: #配列からデータを個別に取得
                                tmpSettingList2.append(setting.replace("\n", "")) #データから改行コードを削除後に領域データとしてリスト配列に追加
                        if len(tmpSettingList2) > 0: #認識対象物の領域データが配列にあるか確認
                            for x in tmpSettingList2: #領域データ毎に処理
                                ROW, LABEL,TX, TY, BX, BY = x.split(',') #領域データを取得
                                cv2.rectangle(tmpCurPic2, (int(TX), int(TY)), (int(BX), int(BY)), (0, 255, 0), 1) #領域を画像データに書込み
                                font_size = 1 #フォントサイズを設定
                                font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                                cv2.putText(tmpCurPic2, LABEL,(int(TX) + 2, int(TY) - 2),font, font_size,(0,255,0),1) #認識対象物のラベルを画像データに書込み
                        else: #認識対象物の領域データがない場合
                            cv2.rectangle(tmpCurPic2, (0, 0), (tmpCurPicWidath2 - 1, tmpCurPicHeight2 - 1), (0, 0, 255), 1) #画像データ画像外周に領域を書込み
                            font_size = 1 #フォントサイズを設定
                            font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                            cv2.putText(tmpCurPic2, 'EXCLUDE', (10, 20),font, font_size,(0,0,255),1) #除外の文字を画像データに書込み
                        cv2.imwrite(DistDirPath + "/" + self.ui.listWidget2.item(CurRow).text() + ".jpg", tmpCurPic2) #写真を保存

    #-----pushButton14用イベント処理----------------------------------------
    ##########
    #領域が描画された写真を選択したフォルダに全て保存
    ##########
    def pushButton14_clicked(self):
        global SettingDataDir #領域生データ保存用フォルダ
        msgbox = QtWidgets.QMessageBox(self)
        ret = msgbox.question(None, "MVC", "Save pictures with region to a folder?\nNOTICE : PLEASE CHOOSE A FOLDER WITH SINGLE BYTE CHARACTORS.", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) #選択用メッセージボックスを表示
        if ret == QtWidgets.QMessageBox.Yes: #メッセージボックスでYESが選択された場合
            DistDirPath = QtWidgets.QFileDialog.getExistingDirectory(self) #ディレクトリを選択
            if DistDirPath: #ディレクトリが選択されたか確認
                tmpSettingList3 = []
                for CurRow in range(self.ui.listWidget3.count()): #リストウィジットのアイテムの数だけループ（１からアイテム数までではなく、０からアイテム数の一つ手前まで）
                    picpath = DirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg" #アイテムをファイルパスとしてリスト配列に追加
                    if os.path.isfile(picpath): #ファイルが存在するか確認
                        tmpCurPic3 = cv2.imread(picpath) #画像を読込む
                        tmpCurPicHeight3 = CurPic3.shape[0] #画像の高さを取得
                        tmpCurPicWidath3 = CurPic3.shape[1] #画像の幅を取得
                        filepath = SettingDataDir + '/' + self.ui.listWidget3.item(CurRow).text() + '.set' #画像に対応する領域データまでのパスを取得
                        text = ""
                        if os.path.isfile(filepath): #ファイルが存在するか確認
                            #####ファイル名のみの取得
                            f = open(filepath, "r") #ファイルの読み込み開始
                            text = f.readlines() #データをリスト配列に格納（改行コードも含む）
                            f.close() #ファイルの読み込み終了
                        tmpSettingList3.clear() #配列をクリア
                        if len(text) > 0: #配列にデータがあるか確認
                            for setting in text: #配列からデータを個別に取得
                                tmpSettingList3.append(setting.replace("\n", "")) #データから改行コードを削除後に領域データとしてリスト配列に追加
                        if len(tmpSettingList3) > 0: #認識対象物の領域データが配列にあるか確認
                            for x in tmpSettingList3: #領域データ毎に処理
                                ROW, LABEL,TX, TY, BX, BY = x.split(',') #領域データを取得
                                cv2.rectangle(tmpCurPic3, (int(TX), int(TY)), (int(BX), int(BY)), (0, 255, 0), 1) #領域を画像データに書込み
                                font_size = 1 #フォントサイズを設定
                                font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                                cv2.putText(tmpCurPic3, LABEL,(int(TX) + 2, int(TY) - 2),font, font_size,(0,255,0),1) #認識対象物のラベルを画像データに書込み
                        else: #認識対象物の領域データがない場合
                            cv2.rectangle(tmpCurPic3, (0, 0), (tmpCurPicWidath3 - 1, tmpCurPicHeight3 - 1), (0, 0, 255), 1) #画像データ画像外周に領域を書込み
                            font_size = 1 #フォントサイズを設定
                            font = cv2.FONT_HERSHEY_PLAIN #フォントを設定
                            cv2.putText(tmpCurPic3, 'EXCLUDE', (10, 20),font, font_size,(0,0,255),1) #除外の文字を画像データに書込み
                        cv2.imwrite(DistDirPath + "/" + self.ui.listWidget3.item(CurRow).text() + ".jpg", tmpCurPic3) #写真を保存

#=====メインウィンドウのイベント処理========================================
    #-----ウィンドウ終了イベントのフック----------------------------------------
    def closeEvent(self, event): #event.accept() event.ignore()で処理を選択可能
        global capLoop
        if capLoop == 1: #ループ実行中の場合
            event.ignore() #メインウィンドウの終了イベントをキャンセル
        else: #ループが実行中でない場合
            event.accept() #メインウィンドウの終了イベントを実行

#####メイン処理（グローバル）########################################
#=====メイン処理定型文========================================
if __name__ == '__main__': #C言語のmain()に相当。このファイルが実行された場合、以下の行が実行される（モジュールとして読込まれた場合は、実行されない）
    app = QtWidgets.QApplication(sys.argv) #アプリケーションオブジェクト作成（sys.argvはコマンドライン引数のリスト）
    win = MainWindow1() #MainWindow1クラスのインスタンスを作成
    win.show() #ウィンドウを表示　win.showFullScreen()やwin.showEvent()を指定する事でウィンドウの状態を変える事が出来る
    sys.exit(app.exec_()) #引数が関数の場合は、関数が終了するまで待ち、その関数の返値を上位プロセスに返す
