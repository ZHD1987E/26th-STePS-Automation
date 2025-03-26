import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

moduleCodes = ["CP3108","CS3203","CS3217","CS3247","CS4240","CS4248","MComp-FYP"]
f1 = open("project names.md","w", encoding="utf-8")
f2 = open("project videos.md", "w", encoding="utf-8")
f3 = open("project-details.json", "w", encoding="utf-8")
jsonDCT = {}
for moduleCode in moduleCodes:
    f1.write(f"# {moduleCode} project names\n")
    f2.write(f"# {moduleCode} project videos\n")
    baseURL = f"https://uvents.nus.edu.sg/event/26th-steps/module/{moduleCode}/project/"
    jsonDCT[moduleCode] = {}
    k = 1
    while True:
        try:
            page = requests.get(baseURL + str(k))
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                div1 = soup.find('div',class_="text-container")
                div2 = soup.find('div', class_="section media")
                div3 = soup.find('div', class_="student-list-wrapper")
                if div2:
                    youtube_links = div2.find_all('a', href=lambda href: href and ("youtube.com" in href or "youtu.be" in href))
                    if youtube_links:
                        for link in youtube_links:
                            f2.write(f"{moduleCode}-{k}: {link['href']}\n\n")
                    else:
                        f2.write(f"{moduleCode}-{k}: NIL\n\n")
                else:
                    f2.write(f"{moduleCode}-{k}: NIL\n\n")
                projName = div1.find('h3').text.strip()
                studentList1 = div3.findAll('li')
                finalStudentList = list(map(lambda e: e.text.strip().title(), studentList1))
                f1.write(f"{moduleCode}-{k}: {projName}\n\n")
                jsonDCT[moduleCode][k] = {'projName': projName, 'nameList': finalStudentList}
                k += 1
            else:
                break
        except Exception as e:
            f1.write(f"An error somehow occured. {e}\n")
            f2.write(f"An error somehow occured. {e}\n")
            break
f1.write(f"Last updated: {datetime.now()}")
f2.write(f"Last updated: {datetime.now()}")
json.dump(jsonDCT, f3, indent = 4)
f1.close()
f2.close()
f3.close()
