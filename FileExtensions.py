EXTENSIONS = {
    "MSOFFICE":[".pptx",".xlsx",".docx",".accdb",".pub",".xls",".ppt",".doc"],
    "VIDEO":[".mp4",".flv",".mov",".avi",".3g2",".3gp",".h264",".m4v",".mkv",".mpg",".mpeg",".rm",".swf",".vob",".wmv"],
    "AUDIO":[".wav",".mp3",".flac",".wma",".ogg",".mid",".midi",".cda",".aif"],
    "COMPRESSION":[".rar",".zip",".tar",".tar.gz",".z",".7z"],
    "DATA":[".csv",".dat",".db",".dbf",".log",".mdb",".accdb",".sav",".sql",".json",".xml",".yaml"],
    "IMAGES":[".ai",".png",".bmp",".gif",".ico",".jpeg",".jpg",".psd",".svg",".tif",".tiff"],
    "PROGRAMMING":[".py",".h",".html",".htm",".css",".js",".vbs",".c",".cpp",".cs",".json",".xml",".yaml",".cgi",".pl",".cer",".asp",".aspx",".cfm",".jsp",".php",".rss",".xhtml"],

}
def get_extension_categories(ext):
    cats = []
    for key,val in EXTENSIONS.items():
        for item in val:
            if item == ext.lower():
                cats.append(key)
    return cats
