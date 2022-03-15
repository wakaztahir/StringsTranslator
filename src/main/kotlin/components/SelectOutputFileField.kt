package components

import LocalAppState
import androidx.compose.foundation.border
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicText
import androidx.compose.material.Icon
import androidx.compose.material.IconButton
import androidx.compose.material.MaterialTheme
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Search
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.awt.ComposeWindow
import androidx.compose.ui.unit.dp
import model.StatusType
import model.TranslateStatus
import java.awt.FileDialog
import java.io.File

@Composable
fun SelectOutputFileField(modifier: Modifier = Modifier) {

    val state = LocalAppState.current

    val fileDialog = FileDialog(ComposeWindow(), "Select Source File")

    Row(
        modifier = modifier,
        horizontalArrangement = Arrangement.Center,
        verticalAlignment = Alignment.CenterVertically
    ) {
        BasicText(
            modifier = Modifier.weight(1f)
                .border(2.dp, color = MaterialTheme.colors.onBackground.copy(.05f), shape = RoundedCornerShape(8.dp))
                .padding(12.dp)
                .horizontalScroll(rememberScrollState()),
            text = "Output : " + state.outputFile.path.toString(),
            style = MaterialTheme.typography.caption
        )
        Spacer(Modifier.width(8.dp))
        IconButton(
            onClick = {
                fileDialog.mode = FileDialog.SAVE
                fileDialog.isVisible = true
                if (fileDialog.file != null) {
                    val file = File(fileDialog.file)
                    kotlin.runCatching {
                        state.outputFile = File(file.absolutePath.substring(0,file.absolutePath.lastIndexOf("/") + 1))
                    }.onFailure {
                        state.addStatus(TranslateStatus(type = StatusType.Error,message = it.message.toString() + "\n" + it.stackTraceToString()))
                    }
                }
            }
        ) {
            Icon(
                imageVector = Icons.Default.Search,
                contentDescription = null
            )
        }
    }
}
