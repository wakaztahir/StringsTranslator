import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.runtime.snapshots.SnapshotStateList
import components.TranslationApi
import model.TranslateStatus
import model.TranslationLanguage
import java.io.File

class AppState {
    var translationApi by mutableStateOf(TranslationApi.GoogleTranslate)
    var sourceLanguage by mutableStateOf(TranslationLanguage.English)
    var sourceFile by mutableStateOf<File?>(null)
    var translationRunning  by mutableStateOf(false)
    var outputFile by mutableStateOf<File?>(null)
    val languagesList = mutableStateListOf<TranslationLanguage>()
    val statusList = mutableStateListOf<TranslateStatus>()

    @Synchronized
    fun addStatus(status: TranslateStatus){
        statusList.add(status)
    }
}

