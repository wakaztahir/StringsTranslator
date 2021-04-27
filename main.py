# This is a sample Python script.

import sqlite3
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from enum import Enum

from PySide6.QtCore import Signal, QRunnable, QThreadPool, QObject, Slot
from PySide6.QtWidgets import *

from translator.awsTranslate import runAwsTranslator
from translator.googleTranslate import *
from ui.screens.langs import *
from ui.screens.mainScreen import Ui_MainWindow


class TApis(Enum):
    Google = 0
    AWS = 1
    Deep = 2


# UI Variables
screen = Ui_MainWindow()

# Translation Variables
DBPath = "caches.db"
BeingTranslated = []
ToBeTranslated = []
TranslationsDirectory = "translations"
threadPool = QThreadPool()
currentApi = TApis.Google
TranslationRunning = False
CurrentFileTranslating = None
ThreadsToUse = 1


# Translator Classes

class TranslatorSignals(QObject):
    status = Signal(str)
    onCompleted = Signal(str)
    onFailure = Signal(str)


class Translator(QRunnable):

    def __init__(self, translatorName, language):
        super().__init__()
        self.language = language
        self.signals = TranslatorSignals()
        self.name = translatorName

    @Slot()
    def run(self):
        try:
            self.signals.status.emit("starting " + self.name + " translator for " + self.language)
            self.translate()
        except Exception as e:
            print(str(e))
            self.signals.onFailure.emit(self.name + " failed for " + self.language)
            self.translatorFailed()
            self.findNew()
        finally:
            self.signals.onCompleted.emit(self.name + " translated : " + self.language)
            self.translatorSucceeded()
            self.findNew()

    def findNew(self):
        global ToBeTranslated, BeingTranslated
        shouldRunAgain = False
        for lang in ToBeTranslated:
            if not BeingTranslated.__contains__(lang):
                self.language = lang
                shouldRunAgain = True
                BeingTranslated.append(lang)
                break
        if shouldRunAgain:
            self.run()

    def translatorFailed(self):
        global ToBeTranslated, BeingTranslated, TranslationRunning
        try:
            if BeingTranslated.__contains__(self.language):
                BeingTranslated.remove(self.language)
            if ToBeTranslated.__contains__(self.language):
                ToBeTranslated.remove(self.language)
                updateCaches()
            if len(ToBeTranslated) == 0:
                TranslationRunning = False
        except Exception as e:
            print(str(e))

    def translatorSucceeded(self):
        global ToBeTranslated, BeingTranslated, TranslationRunning
        try:
            if BeingTranslated.__contains__(self.language):
                BeingTranslated.remove(self.language)
            if ToBeTranslated.__contains__(self.language):
                ToBeTranslated.remove(self.language)
                updateCaches()
            if len(ToBeTranslated) == 0:
                TranslationRunning = False
        except Exception as e:
            print(str(e))

    def translate(self):
        time.sleep(3)


class GoogleTranslate(Translator):

    def __init__(self, filePath, inputLanguage, outputlanguage):
        super().__init__("Google", outputlanguage)
        self.path = filePath
        self.inputLang = inputLanguage

    def translate(self):
        runGTranslator(self.path, self.inputLang, self.language, lambda msg: self.signals.status.emit(msg),
                       screen.outputText.text())


class AwsTranslator(Translator):

    def __init__(self, filePath, inputLanguage, outputlanguage):
        super().__init__("Aws", outputlanguage)
        self.path = filePath
        self.inputLang = inputLanguage

    def translate(self):
        runAwsTranslator(self.path, self.inputLang, self.language, lambda msg: self.signals.status.emit(msg),
                         screen.outputText.text())


class DeepTranslator(Translator):

    def __init__(self, language):
        super().__init__("Deep", language)

    def translate(self):
        time.sleep(2)


# UI Actions Listeners


def setupLanguages():
    langsNames = langs.values()
    screen.langsBox.addItems(langsNames)
    screen.langsBox.setCheckedData(tuple(langs.values()))


def setupListeners():
    screen.gTranslate.clicked.connect(onApiChanged)
    screen.awsTranslate.clicked.connect(onApiChanged)
    screen.deepTranslate.clicked.connect(onApiChanged)
    screen.translateBtn.clicked.connect(onTranslateClick)
    screen.chooseFileBtn.clicked.connect(chooseFile)
    screen.chooseSave.clicked.connect(chooseSave)
    screen.langsBox.currentTextChanged.connect(onLangsUpdated)
    screen.allCheck.stateChanged.connect(updateLangsCheck)
    screen.threadSpinner.valueChanged.connect(threadsChanged)
    screen.actionClearCaches.triggered.connect(clearCaches)


def onApiChanged():
    global currentApi
    if not TranslationRunning:
        if screen.gTranslate.isChecked():
            currentApi = TApis.Google
        elif screen.awsTranslate.isChecked():
            currentApi = TApis.AWS
        elif screen.deepTranslate.isChecked():
            currentApi = TApis.Deep
    else:
        # Translation Already Running , Unchanging
        putInformation("Avoiding API change as translation is running")
        if currentApi == TApis.Google:
            screen.gTranslate.setChecked(True)
        elif currentApi == TApis.AWS:
            screen.awsTranslate.setChecked(True)
        elif currentApi == TApis.Deep:
            screen.deepTranslate.setChecked(True)


def chooseFile():
    global CurrentFileTranslating
    file = QFileDialog().getOpenFileUrl(caption="Select strings.xml", dir="./", filter="String XML File (*.xml)")
    url = file[0]
    if url.isValid():
        screen.fileText.setText(str(url.fileName()))
        CurrentFileTranslating = url.toLocalFile()
        getCacheFor(url.toLocalFile())
    else:
        putError("Invalid / Corrupted File Selected")
        QMessageBox(QMessageBox.Warning, "Invalid File", "You selected invalid or corrupted file").exec_()


def chooseSave():
    if not TranslationRunning:
        file = QFileDialog().getExistingDirectoryUrl(caption="Select Output Directory", dir="./")
        if file.isValid():
            screen.outputText.setText((file.toLocalFile() + "/"))
        else:
            putStatus("Invalid directory")
    else:
        putStatus("Cannot update directory when translation running")


def onLangsUpdated():
    global ToBeTranslated
    data = screen.langsBox.currentData()
    updatedLangs = []
    langShorts = tuple(langs.keys())
    langLongs = tuple(langs.values())
    for langLong in data:
        updatedLangs.append(langShorts[langLongs.index(langLong)])

    ToBeTranslated = updatedLangs


def updateLangsCheck():
    global ToBeTranslated
    if screen.allCheck.isChecked():
        ToBeTranslated = langs.keys()
        updateLangs()
    else:
        ToBeTranslated = []
        screen.langsBox.clearCheckedData()


def updateLangs():
    global ToBeTranslated
    langNames = []
    for langShort in ToBeTranslated:
        langNames.append(langs.get(langShort))
    screen.langsBox.setCheckedData(langNames)


# UI Functions

def putSuccess(message):
    screen.statusBox.append("<b style='color:green'>" + message + "<b>")


def putStatus(message):
    screen.statusBox.append("<span>" + message + "</span>")


def putInformation(message):
    screen.statusBox.append("<strong>" + message + "</strong>")


def putWarning(message):
    screen.statusBox.append("<span style='color:brown'>" + message + "</span>")


def putError(message):
    screen.statusBox.append("<span style='color:red'>" + message + "</span>")


def onTranslateClick():
    global ToBeTranslated, BeingTranslated
    # Checks Before Running
    if TranslationRunning:
        putWarning("Translation already running")
        return
    if CurrentFileTranslating is None:
        putWarning("Translation file is empty")

    threadCount = ThreadsToUse
    if threadCount > threadPool.maxThreadCount():
        threadCount = threadPool.maxThreadCount()

    for threadNumber in range(threadCount):
        if threadNumber < len(ToBeTranslated):
            language = ToBeTranslated[threadNumber]
            startTranslationApi(language)
        else:
            break


# Cache Database Functions

def getCacheFor(url):
    global ToBeTranslated
    db = sqlite3.connect(DBPath)
    cursor = db.execute("SELECT * FROM caches WHERE filePath=?", [url])
    record = cursor.fetchone()
    if record is None:
        cursor.close()
        db.execute("INSERT INTO caches (filePath) VALUES (?)", [url])
        db.commit()
        putInformation("New file path inserted into database")
    else:
        ToBeTranslated = record[2].split(",")
        updateLangs()
        putInformation("Cache Found")


def clearCaches():
    global TranslationRunning, ToBeTranslated
    if not TranslationRunning:
        db = sqlite3.connect(DBPath)
        db.execute("DELETE FROM caches")
        db.commit()
        ToBeTranslated = tuple(langs.keys())
        updateLangs()
    else:
        putInformation("Won't clear caches during translation")


def updateCaches():
    db = sqlite3.connect(DBPath)
    db.execute("UPDATE caches SET languages=? WHERE filePath=?", [",".join(ToBeTranslated), CurrentFileTranslating])
    db.commit()


# Internal Functions

def threadsChanged():
    global ThreadsToUse
    try:
        threadNumber = int(screen.threadSpinner.text())
        if not TranslationRunning:
            if threadNumber > 0:
                ThreadsToUse = threadNumber
            else:
                raise ValueError()
        else:
            raise ValueError()
    except Exception:
        putWarning("Either Translating or Invalid Value")
        screen.threadSpinner.setValue(ThreadsToUse)


def startTranslationApi(language):
    global currentApi, TranslationRunning

    TranslationRunning = True

    # Finding Api
    translator = None
    if currentApi is TApis.Google:
        translator = GoogleTranslate(CurrentFileTranslating, screen.sourceText.text(), language)
    elif currentApi is TApis.AWS:
        translator = AwsTranslator(CurrentFileTranslating, screen.sourceText.text(), language)
    elif currentApi is TApis.Deep:
        translator = DeepTranslator(language)

    # Starting Thread
    if translator is None:
        putError("Unknown Api")
    else:
        if not BeingTranslated.__contains__(language):
            BeingTranslated.append(language)
        translator.signals.status.connect(putStatus)
        translator.signals.onFailure.connect(putWarning)
        translator.signals.onCompleted.connect(putSuccess)
        threadPool.start(translator)


# Main Program Runner

def main():
    app = QApplication()
    window = QMainWindow()
    screen.setupUi(window)
    setupLanguages()
    setupListeners()
    window.show()
    app.exec_()


main()
