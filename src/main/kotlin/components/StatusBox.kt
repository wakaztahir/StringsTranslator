package components

import LocalAppState
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.material.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import model.StatusType
import model.TranslateStatus

@Composable
fun StatusBox(modifier: Modifier = Modifier) {

    val state = LocalAppState.current

    val listState = rememberLazyListState()

    Box(modifier = modifier) {
        LazyColumn(state = listState, modifier = Modifier.fillMaxSize()) {
            items(state.statusList) { status ->
                StatusDisplay(status)
            }
        }
        Row(modifier = Modifier.align(Alignment.TopEnd)) {
            Checkbox(
                checked = state.displayInfos, onCheckedChange = {  state.displayInfos = it },
                colors = CheckboxDefaults.colors(uncheckedColor = Color.Blue, checkedColor = Color.Blue),
            )
            Checkbox(
                checked = state.displayWarnings, onCheckedChange = {  state.displayWarnings = it },
                colors = CheckboxDefaults.colors(uncheckedColor = Color.Yellow, checkedColor = Color.Yellow),
            )
            Checkbox(
                checked = state.displayErrors, onCheckedChange = {  state.displayErrors = it },
                colors = CheckboxDefaults.colors(uncheckedColor = Color.Red, checkedColor = Color.Red),
            )
        }
    }

    LaunchedEffect(state.statusList.size){
        kotlin.runCatching {
            if(listState.firstVisibleItemIndex > state.statusList.size * 0.75){
                listState.animateScrollToItem(listState.layoutInfo.totalItemsCount - 1)
            }
        }
    }
}

@Composable
fun StatusDisplay(status: TranslateStatus) {
    Text(
        modifier = Modifier.padding(16.dp),
        text = status.message,
        color = when (status.type) {
            StatusType.Info -> Color.Blue
            StatusType.Success -> Color.Green
            StatusType.Warning -> Color(0xFFcc3300)
            StatusType.Error -> Color.Red
        },
        style = MaterialTheme.typography.caption
    )
}