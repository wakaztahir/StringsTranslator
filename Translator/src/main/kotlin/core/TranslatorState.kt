package core

import model.TranslateStatus
import model.TranslationLanguage
import java.io.File

interface TranslatorState {
    var translationApi: TranslationApi
    var sourceLanguage: TranslationLanguage
    var sourceFile: File?
    var translationRunning: Boolean
    var outputFile: File
    val languagesList: MutableList<TranslationLanguage>

    // status toggles
    var displayInfos: Boolean
    var displayWarnings: Boolean
    var displayErrors: Boolean

    fun addStatus(status: TranslateStatus)
}

