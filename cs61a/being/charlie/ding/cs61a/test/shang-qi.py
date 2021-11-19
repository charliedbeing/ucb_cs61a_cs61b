
result =""
with open('shang.ass', 'r', encoding='utf-8') as f:
    lines = f.readlines();
    for item in lines:
        temp =str(item)
        ss= temp.split("}")
        if len(ss)==2:
            result = result +ss[1]

print(result)

with open("Output.txt", "w") as text_file:
    text_file.write("Purchase Amount: %s" % result)


