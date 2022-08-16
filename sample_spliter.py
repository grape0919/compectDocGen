with open("./temp.txt", "r") as rf:
    all = rf.read()
    
posts = all.split("====")

for post in posts:
    pass