import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.runtime.snapshots.SnapshotStateList
import components.TranslationApi
import model.PopularLanguages
import model.StatusType
import model.TranslateStatus
import model.TranslationLanguage
import java.io.File
import java.nio.file.FileSystems

class AppState {
    var translationApi by mutableStateOf(TranslationApi.GoogleTranslate)
    var sourceLanguage by mutableStateOf(TranslationLanguage.English)
    var sourceFile by mutableStateOf<File?>(null)
    var translationRunning  by mutableStateOf(false)
    var outputFile by mutableStateOf<File>(FileSystems.getDefault().getPath("").toAbsolutePath().toFile().resolve("strings/"))
    val languagesList = mutableStateListOf<TranslationLanguage>(*PopularLanguages.toTypedArray()).apply { remove(sourceLanguage) }
    val statusList = mutableStateListOf<TranslateStatus>()

    // status toggles
    var displayInfos by mutableStateOf(true)
    var displayWarnings by mutableStateOf(true)
    var displayErrors by mutableStateOf(true)

    @Synchronized
    fun addStatus(status: TranslateStatus){
        when(status.type){
            StatusType.Info -> { if(!displayInfos) return }
            StatusType.Success -> {  } // do nothing
            StatusType.Warning ->  { if(!displayWarnings) return }
            StatusType.Error ->  { if(!displayErrors) return }
        }
        statusList.add(status)
    }
}

