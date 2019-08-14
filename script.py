libs=['discord',
'pyDictionary',
'Vocabulary',
'string',
'base64',
'BeautifulSoup',
'urllib',
'hashlib',
'wikipedia']

from subprocess import check_output
for lib in libs:
    try:
        print("Trying " + lib + "...")
        out=check_output("C:\\Users\\varni\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\pip.exe install " + lib, shell=True).decode()
        print(out)
    except Exception as e:
        print(str(e))
        
        
