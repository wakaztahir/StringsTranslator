package core

import AppState
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import model.StatusType
import model.TranslateStatus
import model.TranslationLanguage
import java.io.File

suspend fun AppState.saveLanguage(
    language: TranslationLanguage,
    langMap : Map<String,String>
){
    val folderName = "values-${language.key}"
    var file = outputFile?.resolve("./$folderName/strings.xml")

    if(file?.exists() == false) {
        withContext(Dispatchers.IO) {
            file?.createNewFile()
        }
    }

    if(file == null || !file.canWrite()) {
        file = withContext(Dispatchers.IO) {
            File.createTempFile("strings-${language.key}", ".xml")
        }
        addStatus(TranslateStatus(type = StatusType.Warning,message = "Output File Path undefined , set to temporary file ${file.absolutePath}"))
    }

    if(file == null) error("File is null")

    val writer = file.bufferedWriter()

    withContext(Dispatchers.IO) {
        writer.write("""<?xml version="1.0" encoding="utf-8"?>${"\n"}""")
        writer.write("<resources>\n")
        langMap.forEach {
            writer.write("""<string name="${it.key}">${it.value}</string>${"\n"}""")
        }
        writer.write("</resources>")
        writer.close()

        addStatus(TranslateStatus(type = StatusType.Success,message = "${language.name} has been translated and saved successfully"))
    }
}