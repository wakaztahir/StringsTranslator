package core

import AppState
import io.ktor.client.call.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.Job
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.joinAll
import kotlinx.coroutines.launch
import model.StatusType
import model.TranslateStatus
import model.TranslationLanguage

suspend fun AppState.googleTranslate() = coroutineScope {
    translationRunning = true

    addStatus(TranslateStatus(type = StatusType.Info, message = "Google Translate running"))

    val translatingLanguages: MutableList<TranslationLanguage> = languagesList

    if (sourceFile == null) {
        addStatus(TranslateStatus(type = StatusType.Error, message = "Source file hasn't been selected"))
        translationRunning = false
        return@coroutineScope
    }

    if (translatingLanguages.size == 0) {
        addStatus(
            TranslateStatus(
                type = StatusType.Warning,
                message = "You haven't selected any languages to translate"
            )
        )
        translationRunning = false
        return@coroutineScope
    }

    if (outputFile == null) {
        addStatus(TranslateStatus(type = StatusType.Warning, message = "You haven't selected any output file"))
        translationRunning = false
        return@coroutineScope
    }

    val langMap = parseXML(sourceFile!!)

    while (translatingLanguages.isNotEmpty()) {
        val translatingLanguage = translatingLanguages.first()
        googleTranslate(toLanguage = translatingLanguage, langMap = langMap)
        translatingLanguages.remove(translatingLanguage)
    }

    translationRunning = false
}

suspend fun AppState.googleTranslate(toLanguage: TranslationLanguage, langMap: Map<String, String>) = coroutineScope {

    val translateMap = langMap.toMutableMap()
    val translatedMap = mutableMapOf<String, String>()

    val maxLangThreads = 4

    val jobs = mutableListOf<Job>()

    fun launchLanguageCoroutines() {
        for (i in 0 until minOf(translateMap.size, maxLangThreads)) {

            val translateKey = translateMap.keys.elementAt(i)

            val job = launch(IO) {
                val toTranslate = translateMap[translateKey]
                val translated: String? = kotlin.runCatching {
                    if (toTranslate != null) {
                        googleTranslate(srcLanguage = sourceLanguage, toLanguage = toLanguage, toTranslate)
                    } else {
                        null
                    }
                }.onFailure {
                    addStatus(TranslateStatus(type = StatusType.Error, message = it.message.toString()))
                }.getOrNull()

                if (translated != null) {
                    addStatus(
                        TranslateStatus(
                            type = StatusType.Info,
                            message = "$translateKey : $toTranslate --> $translated"
                        )
                    )
                    translateMap.remove(translateKey)
                    translatedMap[translateKey] = translated
                } else {
                    addStatus(
                        TranslateStatus(
                            type = StatusType.Warning,
                            message = "Translation failed for language ${toLanguage.name} , item : $toTranslate"
                        )
                    )
                }
            }

            jobs.add(job)
        }

        if(jobs.size > 0){
            jobs.last().invokeOnCompletion {
                jobs.clear()
                if(translateMap.isNotEmpty()) {
                    launchLanguageCoroutines()
                }else {

                }
            }
        }
    }

    launchLanguageCoroutines()

    joinAll()


    if (translatedMap.size == langMap.size) {
        addStatus(
            TranslateStatus(
                type = StatusType.Success,
                message = "Translation for language $toLanguage has completed"
            )
        )
        saveLanguage(language = toLanguage, langMap = translatedMap)
    } else {
        addStatus(
            TranslateStatus(
                type = StatusType.Warning,
                message = "Some keys from the language ${toLanguage.name} haven't been translated"
            )
        )
    }
}

suspend fun googleTranslate(
    srcLanguage: TranslationLanguage,
    toLanguage: TranslationLanguage,
    toTranslate: String
): String {
    val base = "https://translate.google.com"
    val url = base + "/m?sl=" + srcLanguage.key + "&tl=" + toLanguage.key + "&q=" + toTranslate.replace(" ", "+")

    val response = client.get<HttpResponse>(url) {

    }

    val payload = response.receive<String>()
    val start = """<div class="result-container">"""
    val end = "</div>"
    val startIndex = payload.indexOf(start)

    val translation =
        payload.substring(startIndex + start.length, payload.indexOf(startIndex = startIndex, string = end))

    return translation
}