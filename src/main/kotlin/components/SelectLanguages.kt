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
fun SelectLanguages(modifier : Modifier = Modifier){

    val state = LocalAppState.current

    var listVisible by remember { mutableStateOf(false) }

    if (listVisible) {
        Popup(onDismissRequest = { listVisible = false }) {
            Box(modifier = Modifier.fillMaxSize().background(color = MaterialTheme.colors.background)) {
                Column {
                    Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            modifier = Modifier.weight(1f),
                            text = "Select Languages",
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
                    Row(horizontalArrangement = Arrangement.Center) {
                        OutlinedButton(onClick = {
                            state.languagesList.addAll(TranslationLanguage.values())
                            state.languagesList.remove(state.sourceLanguage)
                        }){
                            Text(text = "Select All")
                        }
                        Spacer(modifier = Modifier.width(4.dp))
                        OutlinedButton(onClick = {
                            state.languagesList.clear()
                        }){
                            Text(text = "Deselect All")
                        }
                    }
                    MultipleLanguageSelectionList(
                        modifier = Modifier.padding(end = 32.dp),
                        isSelected = { state.languagesList.contains(it) },
                        onSelectDeselect = { lang,select->
                            if(select && !state.languagesList.contains(lang)){
                                state.languagesList.add(lang)
                            }else if(!select && state.languagesList.contains(lang)){
                                state.languagesList.remove(lang)
                            }
                        }
                    )
                }
            }
        }
    } else {
        OutlinedButton(
            modifier = modifier,
            onClick = {
                listVisible = true
            }
        ) {
            Text(text = "${state.languagesList.size} Languages Selected")
        }
    }

}


@Composable
fun MultipleLanguageSelectionList(
    modifier: Modifier = Modifier,
    isSelected : (TranslationLanguage)->Boolean,
    onSelectDeselect : (TranslationLanguage, Boolean)->Unit
) {
    LazyColumn(modifier = modifier) {
        items(TranslationLanguage.values()) { lang ->
            Row(modifier = Modifier.padding(horizontal = 12.dp).fillMaxWidth().clip(shape = RoundedCornerShape(6.dp)).clickable { onSelectDeselect(lang,!isSelected(lang)) },verticalAlignment = Alignment.CenterVertically) {
                Checkbox(
                    checked = isSelected(lang),
                    onCheckedChange = { onSelectDeselect(lang,it) }
                )
                Text(text = lang.name)
            }
        }
    }
}