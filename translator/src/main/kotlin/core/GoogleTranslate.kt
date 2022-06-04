package core

import io.ktor.client.call.*
import io.ktor.client.features.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import kotlinx.coroutines.*
import model.StatusType
import model.TranslateStatus
import model.TranslationLanguage

suspend fun TranslatorState.googleTranslate() = coroutineScope {
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

    val langMap = parseXML(sourceFile!!)

    while (translatingLanguages.isNotEmpty()) {
        val translatingLanguage = translatingLanguages.first()
        addStatus(
            TranslateStatus(
                type = StatusType.Info,
                message = "Beginning Translation For Language ${translatingLanguage.name}"
            )
        )
        googleTranslate(toLanguage = translatingLanguage, langMap = langMap)
        translatingLanguages.remove(translatingLanguage)
    }

    translationRunning = false
}

suspend fun TranslatorState.googleTranslate(toLanguage: TranslationLanguage, langMap: Map<String, String>) = coroutineScope {

    val translateMap = langMap.toMutableMap()
    val translatedMap = mutableMapOf<String, String>()

    val maxLangThreads = 12

    suspend fun launchLanguageCoroutines() {

        val jobs = mutableListOf<Job>()
        val totalJobs = minOf(translateMap.size, maxLangThreads)

        for (i in 0 until totalJobs) {

            val translateKey = translateMap.keys.elementAt(i)

            val job = launch {
                val toTranslate = translateMap[translateKey]
                var translated: String? = kotlin.runCatching {
                    if (toTranslate != null) {
                        googleTranslate(srcLanguage = sourceLang, toLanguage = toLanguage, toTranslate)
                    } else {
                        null
                    }
                }.onFailure {
                    addStatus(TranslateStatus(type = StatusType.Error, message = it.message.toString()))
                }.getOrNull()

                translated = translated?.let { StringUtils.unescapeForStrings(toLanguage,it) }

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

        jobs.joinAll()

        if (translateMap.isEmpty()) {
            if (translatedMap.size != langMap.size) {
                addStatus(
                    TranslateStatus(
                        type = StatusType.Warning,
                        message = "Some keys from the language ${toLanguage.name} haven't been translated"
                    )
                )
            }
            addStatus(
                TranslateStatus(
                    type = StatusType.Success,
                    message = "Translation for language $toLanguage has completed"
                )
            )
            jobs.clear()
            saveLanguage(language = toLanguage, langMap = translatedMap)
        } else {
            jobs.clear()
            launchLanguageCoroutines()
        }
    }

    launchLanguageCoroutines()
}

suspend fun googleTranslate(
    srcLanguage: TranslationLanguage,
    toLanguage: TranslationLanguage,
    toTranslate: String
): String {
    val base = "https://translate.google.com"
    val url = base + "/m?sl=" + srcLanguage.key + "&tl=" + toLanguage.key + "&q=" + toTranslate.replace(" ", "+")

    val response = withContext(Dispatchers.IO) {
        client.get<HttpResponse>(url) {
            this.timeout {
                this.connectTimeoutMillis = 6000
                this.requestTimeoutMillis = 6000
            }
        }
    }

    val payload = response.receive<String>()

    val start = """<div class="result-container">"""
    val end = "</div>"
    val startIndex = payload.indexOf(start)

    return payload.substring(startIndex + start.length, payload.indexOf(startIndex = startIndex, string = end))
}