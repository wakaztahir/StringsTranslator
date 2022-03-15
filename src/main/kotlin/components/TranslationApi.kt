package components

import LocalAppState
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.material.RadioButton
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier

enum class TranslationApi(val displayName : String) {
    GoogleTranslate("Google Translate"),
    AWSTranslate("AWS Translate"),
    DeepTranslate("Deep Translate")
}

@Composable
fun TranslationApi(modifier : Modifier = Modifier){
    val state = LocalAppState.current

    Column(modifier = modifier) {
        TranslationApi.values().forEach {
            Row(verticalAlignment = Alignment.CenterVertically) {
                RadioButton(
                    selected = state.translationApi == it,
                    onClick = { state.translationApi = it }
                )
                Text(
                    text = it.displayName
                )
            }
        }
    }
}