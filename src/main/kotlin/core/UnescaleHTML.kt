package core

import java.io.StringWriter


object StringUtils {

    private val ESCAPES = arrayOf(
        arrayOf("\"", "quot"),
        arrayOf("&", "amp"),
        arrayOf("<", "lt"),
        arrayOf(">", "gt"),
        arrayOf("\u00A0", "nbsp"),
        arrayOf("\u00A1", "iexcl"),
        arrayOf("\u00A2", "cent"),
        arrayOf("\u00A3", "pound"),
        arrayOf("\u00A4", "curren"),
        arrayOf("\u00A5", "yen"),
        arrayOf("\u00A6", "brvbar"),
        arrayOf("\u00A7", "sect"),
        arrayOf("\u00A8", "uml"),
        arrayOf("\u00A9", "copy"),
        arrayOf("\u00AA", "ordf"),
        arrayOf("\u00AB", "laquo"),
        arrayOf("\u00AC", "not"),
        arrayOf("\u00AD", "shy"),
        arrayOf("\u00AE", "reg"),
        arrayOf("\u00AF", "macr"),
        arrayOf("\u00B0", "deg"),
        arrayOf("\u00B1", "plusmn"),
        arrayOf("\u00B2", "sup2"),
        arrayOf("\u00B3", "sup3"),
        arrayOf("\u00B4", "acute"),
        arrayOf("\u00B5", "micro"),
        arrayOf("\u00B6", "para"),
        arrayOf("\u00B7", "middot"),
        arrayOf("\u00B8", "cedil"),
        arrayOf("\u00B9", "sup1"),
        arrayOf("\u00BA", "ordm"),
        arrayOf("\u00BB", "raquo"),
        arrayOf("\u00BC", "frac14"),
        arrayOf("\u00BD", "frac12"),
        arrayOf("\u00BE", "frac34"),
        arrayOf("\u00BF", "iquest"),
        arrayOf("\u00C0", "Agrave"),
        arrayOf("\u00C1", "Aacute"),
        arrayOf("\u00C2", "Acirc"),
        arrayOf("\u00C3", "Atilde"),
        arrayOf("\u00C4", "Auml"),
        arrayOf("\u00C5", "Aring"),
        arrayOf("\u00C6", "AElig"),
        arrayOf("\u00C7", "Ccedil"),
        arrayOf("\u00C8", "Egrave"),
        arrayOf("\u00C9", "Eacute"),
        arrayOf("\u00CA", "Ecirc"),
        arrayOf("\u00CB", "Euml"),
        arrayOf("\u00CC", "Igrave"),
        arrayOf("\u00CD", "Iacute"),
        arrayOf("\u00CE", "Icirc"),
        arrayOf("\u00CF", "Iuml"),
        arrayOf("\u00D0", "ETH"),
        arrayOf("\u00D1", "Ntilde"),
        arrayOf("\u00D2", "Ograve"),
        arrayOf("\u00D3", "Oacute"),
        arrayOf("\u00D4", "Ocirc"),
        arrayOf("\u00D5", "Otilde"),
        arrayOf("\u00D6", "Ouml"),
        arrayOf("\u00D7", "times"),
        arrayOf("\u00D8", "Oslash"),
        arrayOf("\u00D9", "Ugrave"),
        arrayOf("\u00DA", "Uacute"),
        arrayOf("\u00DB", "Ucirc"),
        arrayOf("\u00DC", "Uuml"),
        arrayOf("\u00DD", "Yacute"),
        arrayOf("\u00DE", "THORN"),
        arrayOf("\u00DF", "szlig"),
        arrayOf("\u00E0", "agrave"),
        arrayOf("\u00E1", "aacute"),
        arrayOf("\u00E2", "acirc"),
        arrayOf("\u00E3", "atilde"),
        arrayOf("\u00E4", "auml"),
        arrayOf("\u00E5", "aring"),
        arrayOf("\u00E6", "aelig"),
        arrayOf("\u00E7", "ccedil"),
        arrayOf("\u00E8", "egrave"),
        arrayOf("\u00E9", "eacute"),
        arrayOf("\u00EA", "ecirc"),
        arrayOf("\u00EB", "euml"),
        arrayOf("\u00EC", "igrave"),
        arrayOf("\u00ED", "iacute"),
        arrayOf("\u00EE", "icirc"),
        arrayOf("\u00EF", "iuml"),
        arrayOf("\u00F0", "eth"),
        arrayOf("\u00F1", "ntilde"),
        arrayOf("\u00F2", "ograve"),
        arrayOf("\u00F3", "oacute"),
        arrayOf("\u00F4", "ocirc"),
        arrayOf("\u00F5", "otilde"),
        arrayOf("\u00F6", "ouml"),
        arrayOf("\u00F7", "divide"),
        arrayOf("\u00F8", "oslash"),
        arrayOf("\u00F9", "ugrave"),
        arrayOf("\u00FA", "uacute"),
        arrayOf("\u00FB", "ucirc"),
        arrayOf("\u00FC", "uuml"),
        arrayOf("\u00FD", "yacute"),
        arrayOf("\u00FE", "thorn"),
        arrayOf("\u00FF", "yuml")
    )
    private const val MIN_ESCAPE = 2
    private const val MAX_ESCAPE = 6
    private val lookupMap: HashMap<String, CharSequence> = HashMap()

    init {
        for (seq in ESCAPES) lookupMap[seq[1]] = seq[0]
    }

    fun unescapeHtml3(input: String): String {
        var writer: StringWriter? = null
        val len = input.length
        var i = 1
        var st = 0
        while (true) {
            // look for '&'
            while (i < len && input[i - 1] != '&') i++
            if (i >= len) break

            // found '&', look for ';'
            var j = i
            while (j < len && j < i + MAX_ESCAPE + 1 && input[j] != ';') j++
            if (j == len || j < i + MIN_ESCAPE || j == i + MAX_ESCAPE + 1) {
                i++
                continue
            }

            // found escape
            if (input[i] == '#') {
                // numeric escape
                var k = i + 1
                var radix = 10
                val firstChar = input[k]
                if (firstChar == 'x' || firstChar == 'X') {
                    k++
                    radix = 16
                }
                try {
                    val entityValue = input.substring(k, j).toInt(radix)
                    if (writer == null) writer = StringWriter(input.length)
                    writer.append(input.substring(st, i - 1))
                    if (entityValue > 0xFFFF) {
                        val chrs = Character.toChars(entityValue)
                        writer.write(chrs[0].code)
                        writer.write(chrs[1].code)
                    } else {
                        writer.write(entityValue)
                    }
                } catch (ex: NumberFormatException) {
                    i++
                    continue
                }
            } else {
                // named escape
                val value = lookupMap[input.substring(i, j)]
                if (value == null) {
                    i++
                    continue
                }
                if (writer == null) writer = StringWriter(input.length)
                writer.append(input.substring(st, i - 1))
                writer.append(value)
            }

            // skip escape
            st = j + 1
            i = st
        }
        if (writer != null) {
            writer.append(input.substring(st, len))
            return writer.toString()
        }
        return input
    }

    fun unescapeForStrings(input: String): String {
        return unescapeHtml3(input).let {
            if (it == "'") "\\'" else it
        }
    }
}