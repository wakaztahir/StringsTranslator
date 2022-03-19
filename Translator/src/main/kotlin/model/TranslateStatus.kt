package model

enum class StatusType {
    Info,
    Success,
    Warning,
    Error,
}

data class TranslateStatus(
    val type : StatusType,
    val message : String
)