import requests
from bs4 import BeautifulSoup
moduleCodes = ["CS3203","CS3216","CS4350","IS4103","IS4250","MComp-FYP"]
f1 = open("project names.md","w", encoding="utf-8")
f2 = open("project videos.md", "w", encoding="utf-8")
for moduleCode in moduleCodes:
    f1.write(f"# {moduleCode} project names\n")
    f2.write(f"# {moduleCode} project videos\n")
    baseURL = f"https://uvents.nus.edu.sg/event/25th-steps/module/{moduleCode}/project/"
    k = 1
    while True:
        try:
            page = requests.get(baseURL + str(k))
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                div1 = soup.find('div',class_="text-container")
                div2 = soup.find('div', class_="section media")
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
                f1.write(f"{moduleCode}-{k}: {projName}\n\n")
                k += 1
            else:
                break
        except Exception as e:
            f1.write(f"An error somehow occured. {e}\n")
            f2.write(f"An error somehow occured. {e}\n")
            break

f1.close()
f2.close()