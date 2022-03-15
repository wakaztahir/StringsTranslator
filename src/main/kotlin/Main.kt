// Copyright 2000-2021 JetBrains s.r.o. and contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
import androidx.compose.material.MaterialTheme
import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.OutlinedButton
import androidx.compose.material.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.WindowState
import androidx.compose.ui.window.application
import components.*
import core.beginTranslate
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

val LocalAppState = staticCompositionLocalOf<AppState> { error("app state uninitialized") }

@Composable
@Preview
fun App() {
    MaterialTheme {

        var currentApi by remember { mutableStateOf(TranslationApi.GoogleTranslate) }
        val appState = AppState()

        val scope = rememberCoroutineScope()

        CompositionLocalProvider(LocalAppState provides appState) {
            Column(modifier = Modifier.padding(16.dp)) {
                TranslationApi(modifier = Modifier.fillMaxWidth())
                SourceLanguageField(modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp))
                Spacer(Modifier.height(4.dp))
                SelectFileField(modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp))
                SelectOutputFileField(modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp))
                SelectLanguages(modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp))
                StatusBox(modifier = Modifier.fillMaxWidth().height(200.dp).padding(12.dp).clip(RoundedCornerShape(6.dp)).background(color = MaterialTheme.colors.onBackground.copy(.05f)))
                OutlinedButton(
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp),
                    onClick = {
                        scope.launch(Dispatchers.IO) {  appState.beginTranslate()}
                    },
                    enabled = !appState.translationRunning
                ){
                    Text(
                        text = "Begin Translate",
                    )
                }
            }
        }
    }
}

fun main() = application {
    Window(onCloseRequest = ::exitApplication,state = WindowState(width = 400.dp,height = 660.dp),title = "Strings Translator") {
        App()
    }
}
