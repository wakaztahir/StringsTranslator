package core

import AppState
import components.TranslationApi
import io.ktor.client.*
import io.ktor.client.engine.cio.*
import model.StatusType
import model.TranslateStatus

val client = HttpClient(CIO)

suspend fun AppState.beginTranslate() {
    when (translationApi) {
        TranslationApi.GoogleTranslate -> googleTranslate()
        TranslationApi.AWSTranslate -> awsTranslate()
        TranslationApi.DeepTranslate -> deepTranslate()
    }
}

suspend fun AppState.awsTranslate() {
    addStatus(TranslateStatus(type = StatusType.Warning, message = "AWS Translate not implemented yet"))
}

suspend fun AppState.deepTranslate() {
    addStatus(TranslateStatus(type = StatusType.Warning, message = "AWS Translate not implemented yet"))
}