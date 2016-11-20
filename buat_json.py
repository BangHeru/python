import json

name = dict(first='Heru', last='Gunawan')
rec = dict(name=name, job=['PNS','Mahasiswa'], age=34)
print(rec)
json.dump(rec, fp=open('coba_json.txt','w'), indent=4)

print(open('coba_json.txt').read())