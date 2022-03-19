import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import core.TranslationApi
import core.TranslatorState
import model.PopularLanguages
import model.StatusType
import model.TranslateStatus
import model.TranslationLanguage
import java.io.File

class AppState : TranslatorState {
    override var translationApi by mutableStateOf(TranslationApi.GoogleTranslate)
    override var sourceLang by mutableStateOf(TranslationLanguage.English)
    override var sourceFile by mutableStateOf<File?>(null)
    override var translationRunning by mutableStateOf(false)
    override var outputFile by mutableStateOf<File>(File(System.getProperty("user.home") + File.separator + "strings-export"))
    override val languagesList = mutableStateListOf<TranslationLanguage>(*PopularLanguages.toTypedArray()).apply { remove(sourceLang) }
    val statusList = mutableStateListOf<TranslateStatus>()

    // status toggles
    override var displayInfos by mutableStateOf(true)
    override var displayWarnings by mutableStateOf(true)
    override var displayErrors by mutableStateOf(true)

    @Synchronized
    override fun addStatus(status: TranslateStatus) {
        when (status.type) {
            StatusType.Info -> {
                if (!displayInfos) return
            }
            StatusType.Success -> {} // do nothing
            StatusType.Warning -> {
                if (!displayWarnings) return
            }
            StatusType.Error -> {
                if (!displayErrors) return
            }
        }
        statusList.add(status)
    }
}

