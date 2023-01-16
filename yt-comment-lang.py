import langdetect as ld
import os
import googleapiclient.discovery
import argparse
from dotenv import load_dotenv

def make_results(response, lang_count):
    results = ""
    results += "Total: " + str(len(response["items"])) + "\n"
    lang_count = dict(sorted(lang_count.items(), key = lambda item: item[1], reverse = True))
    for lang in lang_count:
        if (lang_count[lang] != 0):
             results += (str(langs_full[lang]) + ": " + str(lang_count[lang]) + "\n")
    return results

def main():
    #parse arguments
    parser = argparse.ArgumentParser(description = "Analyze language use in the comments of a YouTube video")
    parser.add_argument("parentId", help = "URL or Id of the video")
    parser.add_argument("-o", "--output", help = "Direct output to file")
    args = parser.parse_args()


    #connect to YouTube API
    load_dotenv()
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE_DEVELOPER_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        parentId=args.parentId
    )
    
    response = request.execute() 
    
    LANGS = ["af", "ar", "bg", "bn", "ca", "cs", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "gu", "he", "hi", "hr", "hu", "id", "it", "ja", "kn", "ko", "lt", "lv", "mk", "ml", "mr",
            "ne", "nl", "no", "pa", "pl", "pt", "ro", "ru", "sk", "sl", "so", "sq", "sv", "sw", "ta", "te", "th", "tl", "tr", "uk", "ur", "vi", "zh-cn", "zh-tw"]
    LANGS_FULL = {"af":"Afrikaans", "ar":"Arabic", "bg":"Bulgarian", "bn":"Bengali",
        "ca":"Catalan", "cs":"Czech", "cy":"Welsh", "da":"Danish", "de":"German", "el":"Greek",
        "en":"English", "es":"Spanish", "et":"Estonian", "fa":"Farsi", "fi":"Finnish", "fr":"French",
        "gu":"Gujarati", "he":"Hebrew", "hi":"Hindi", "hr":"Croatian", "hu":"Hungarian", "id":"Indonesian",
        "it":"Italian", "ja":"Japanese", "kn":"Kannada", "ko":"Korean", "lt":"Lithuanian", "lv":"Latvian",
        "mk":"Macedonian", "ml":"Malayalam", "mr":"Marathi",
        "ne":"Nepali", "nl":"Dutch", "no":"Norwegian", "pa":"Punjabi", "pl":"Polish", "pt":"Portuguese",
        "ro":"Romanian", "ru":"Russian", "sk":"Slovak", "sl":"Slovenian", "so":"Somali", "sq":"Albanian",
        "sv":"Swedish", "sw":"Swahili", "ta":"Tamil", "te":"Telugu", "th":"Thai", "tl":"Tagalog", "tr":"Turkish",
        "uk":"Ukrainian", "ur":"Urdu", "vi":"Vietnamese", "zh-cn":"Chinese (PRC)", "zh-tw":"Chinese (Taiwan)"}
    lang_count = {}

    for lang in LANGS:
        lang_count[lang] = 0

    #lang detection
    unidentified = 0
    for comment in response["items"]:
        try:
            lang = ld.detect(comment["snippet"]["textDisplay"])
            lang_count[lang] += 1    
        except ld.LangDetectException:
            unidentified += 1
            pass

    #output results
    results = make_results(response, lang_count)
    if args.output is None:
        #console
        print(results)
    else:
        #file
        with open(args.output, "w") as out:
            out.write()
        print("Results written to"< args.output)
                

if __name__ == "__main__":
    main()



        
        


    
                        

