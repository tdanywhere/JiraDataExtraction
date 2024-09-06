import json

# ========= Convert incoming data to json ==========
def convertRawdataToJson(rawdata):
    try:
        jData = json.loads(rawdata)
    except json.decoder.JSONDecodeError:
        print(f"Error decoding JSON from rawdata {rawdata}")
        print(f"EXCEPT")

    #print(json.dumps(rawdata, indent=2, sort_keys=False))
    return jData

# ========= Write json file ==========
def writeJsonFile(jData, path):
    f = open(path, "x")
    f.write (json.dumps(jData, indent=2, sort_keys=False))
    f.close()
    print(f"File {path} has been created successfully.")
