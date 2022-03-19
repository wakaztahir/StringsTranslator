package core

enum class TranslationApi(val displayName : String) {
    GoogleTranslate("Google Translate"),
    AWSTranslate("AWS Translate"),
    DeepTranslate("Deep Translate")
}
