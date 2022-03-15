package core

import AppState
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import model.StatusType
import model.TranslateStatus
import model.TranslationLanguage
import java.io.BufferedWriter
import java.io.File

suspend fun AppState.saveLanguage(
    language: TranslationLanguage,
    langMap : Map<String,String>
){
    val folderName = "values-${language.key}"
    val parentDir = outputFile.resolve(folderName + File.separator)
    var file = parentDir.resolve("strings.xml")

    if(!file.exists()) {
        withContext(Dispatchers.IO) {
            kotlin.runCatching { parentDir.mkdirs() }.onFailure { it.printStackTrace() }
            kotlin.runCatching { file.createNewFile() }.onFailure { it.printStackTrace() }
        }
    }

    if(!file.canWrite()) {
        file = withContext(Dispatchers.IO) {
            File.createTempFile("strings-${language.key}", ".xml")
        }
        addStatus(TranslateStatus(type = StatusType.Warning,message = "Output File Path undefined , set to temporary file ${file.absolutePath}"))
    }

    val stream = kotlin.runCatching { file.outputStream() }.getOrNull() ?: withContext(Dispatchers.IO) {
        file.createNewFile()
    }.let { file.outputStream() }
    val streamWriter = stream.writer()
    val writer = BufferedWriter(streamWriter)

    withContext(Dispatchers.IO) {
        writer.write("""<?xml version="1.0" encoding="utf-8"?>${"\n"}""")
        writer.write("<resources>\n")
        langMap.forEach {
            writer.write("""<string name="${it.key}">${it.value}</string>${"\n"}""")
        }
        writer.write("</resources>")
        writer.close()
        streamWriter.close()
        stream.close()

        addStatus(TranslateStatus(type = StatusType.Success,message = "${language.name} has been translated and saved successfully"))
    }
}