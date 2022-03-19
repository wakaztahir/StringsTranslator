package core

import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.features.*
import model.StatusType
import model.TranslateStatus

val client = HttpClient(CIO) {
    install(HttpTimeout)
}

suspend fun TranslatorState.beginTranslate() {
    when (translationApi) {
        TranslationApi.GoogleTranslate -> googleTranslate()
        TranslationApi.AWSTranslate -> awsTranslate()
        TranslationApi.DeepTranslate -> deepTranslate()
    }
}

suspend fun TranslatorState.awsTranslate() {
    addStatus(TranslateStatus(type = StatusType.Warning, message = "AWS Translate not implemented yet"))
}

suspend fun TranslatorState.deepTranslate() {
    addStatus(TranslateStatus(type = StatusType.Warning, message = "AWS Translate not implemented yet"))
}