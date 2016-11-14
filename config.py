
pkg_name = raw_input("Enter package name : ")
url = "https://play.google.com/store/getreviews?authuser=0"
final_referer = "https://play.google.com/store/apps/details?id="+pkg_name
headers = {'Host':'play.google.com', 'referer':final_referer}
payload = {'reviewType':0, 'pageNum':0, 'id':pkg_name, 'reviewSortOrder':2, 'xhr':1}