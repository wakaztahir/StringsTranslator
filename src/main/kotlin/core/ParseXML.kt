package core

import org.simpleframework.xml.*
import org.simpleframework.xml.core.Persister
import java.io.File

fun parseXML(file : File): Map<String, String> {
    val serializer: Serializer = Persister()
    val xmlStream = file.inputStream()
    val stringsContainer = serializer.read(StringsContainer::class.java, xmlStream)
    xmlStream.close()
    return stringsContainer?.map ?: error("strings map is null")
}


@Root(name = "resources")
class StringsContainer {
    @field:ElementMap(entry = "string", key = "name", attribute = true, inline = true)
    lateinit var map: Map<String, String>
}