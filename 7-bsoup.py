from bs4 import BeautifulSoup

# 1 - Importando arquivo local
with open("pages/index.html", "r") as file_html:
    content = file_html.read()
    #  print(content)
    soup = BeautifulSoup(content, "lxml")
    print(soup.prettify())

    # 2 - Recuperando títulos das vagas
    vagas = soup.find("h5")
    cursos = soup.find_all("h5")
    #  print(cursos)
    for curso in cursos:
        print(curso.text)

    # 3 - Pegando mais informações
    course_cards = soup.find_all("div", class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(course_name)
        print(course_price)
        print(f"{course_name} custa {course_price}")
