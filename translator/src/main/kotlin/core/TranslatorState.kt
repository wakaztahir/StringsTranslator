package core

import model.TranslateStatus
import model.TranslationLanguage
import java.io.File

interface TranslatorState {
    val translationApi: TranslationApi
    val sourceLang: TranslationLanguage
    val sourceFile: File?
    var translationRunning: Boolean
    var outputFile: File
    val languagesList: MutableList<TranslationLanguage>

    // status toggles
    val displayInfos: Boolean
    val displayWarnings: Boolean
    val displayErrors: Boolean

    fun addStatus(status: TranslateStatus)
}

