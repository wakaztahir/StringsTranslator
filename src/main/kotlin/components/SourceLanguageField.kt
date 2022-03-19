package components

import LocalAppState
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Popup
import model.TranslationLanguage

@Composable
fun SourceLanguageField(modifier: Modifier = Modifier) {

    val state = LocalAppState.current

    var listVisible by remember { mutableStateOf(false) }

    if (listVisible) {
        Popup(onDismissRequest = { listVisible = false }) {
            Box(modifier = Modifier.fillMaxSize().background(color = MaterialTheme.colors.background)) {
                Column {
                    Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            modifier = Modifier.weight(1f),
                            text = "Source Language",
                            style = MaterialTheme.typography.h5,
                        )
                        IconButton(
                            modifier = Modifier.offset(x = (-24).dp),
                            onClick = {
                                listVisible = false
                            }
                        ) {
                            Icon(
                                imageVector = Icons.Default.Close,
                                contentDescription = null
                            )
                        }
                    }
                    SingleLanguageSelectionList(
                        modifier = Modifier.padding(end = 32.dp)
                    )
                }
            }
        }
    } else {

        OutlinedButton(
            modifier = modifier,
            enabled = !state.translationRunning,
            onClick = {
                listVisible = true
            }
        ) {
            Text(text = "Source Language : ${state.sourceLang.name}")
        }

    }
}


@Composable
fun SingleLanguageSelectionList(modifier: Modifier = Modifier) {

    val state = LocalAppState.current

    LazyColumn(modifier = modifier) {
        items(TranslationLanguage.values(), key = { it.key }) { lang ->
            Row(
                modifier = Modifier.padding(horizontal = 12.dp).fillMaxWidth().clip(shape = RoundedCornerShape(6.dp))
                    .clickable { state.sourceLang = lang }, verticalAlignment = Alignment.CenterVertically
            ) {
                RadioButton(
                    selected = state.sourceLang == lang,
                    onClick = { state.sourceLang = lang }
                )
                Text(text = lang.name)
            }
        }
    }
}