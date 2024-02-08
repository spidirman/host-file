import requests, json, os.path
file_types = {'gif': 'image/gif', 'jpeg': 'image/jpeg', 'jpg': 'image/jpg', 'png': 'image/png', 'mp4': 'video/mp4'}#all accepted file types by telegraph api
def telegraph_file_upload(file_types, path_to_file):
    
    file_ext = path_to_file.split('.')[-1]
    
    if file_ext in file_types:
        file_type = file_types[file_ext]
    else:
        return f'error, {file_ext}-file can not be proccessed' 
      
    with open(path_to_file, 'rb') as f:
        url = 'https://telegra.ph/upload'
        response = requests.post(url, files={'file': ('file', f, file_type)}, timeout=1)
    
    telegraph_url = json.loads(response.content)
    telegraph_url = telegraph_url[0]['src']
    telegraph_url = f'https://telegra.ph{telegraph_url}'
    
    return telegraph_url
 
check = True
while check:
    file = input("your file name (ex : file.jpg)\n>>>")
    if "." not in file:
        print(f"\"{file}\" is an invalid file type.")
    else:
        if file.split('.')[-1] not in file_types:
            print("invalid file type, available file types: [.jpg, .png, .jpeg, .gif, .mp4]")
        else:
            if os.path.isfile(file):
                check = False
            else:
                print("file does not exist")
        
r = telegraph_file_upload(file_types, file)
print(r)
input()
