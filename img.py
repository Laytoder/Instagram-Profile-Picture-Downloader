import urllib.request
x = input("Enter the username : ")
link = 'https://www.instagram.com/' + x
response = urllib.request.urlopen(link)
page_source_str = response.read().decode('utf-8')
start = page_source_str.find('profile_pic_url_hd') + len('profile_pic_url_hd') + 3
end = page_source_str.find('"', start)
durl = page_source_str[start : end]
urllib.request.urlretrieve(durl, r'D:\stark\stark.jpg')