#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Данные сотрудников по ресторанам
restaurants = [
    {
        "id": 1,
        "name": "Ресторан Мартынова 22",
        "employees": [
            {
                "photo": "photos/242b6b22-1657-476b-bc42-24d2fb44d106.jfif",
                "name": "Киреева Алиса",
                "role": "22 года, стаж 3 года",
                "description": "Пришла менеджером доставки на Мира, потом перешла на Мартынова. Позитивная, всегда готова помочь, заряжает своей энергией!",
                "quote": "«Нравится отношения руководства к персоналу, дружелюбный коллектив, хорошая оплата труда. Люблю Грильницу!»"
            },
            {
                "photo": "photos/4c120d19-9e0e-4b47-8265-53ff9d8f388e.jfif",
                "name": "Ермолович Анна",
                "role": "21 год, стаж 3 года",
                "description": "Пришла работать в 2023 году на кассу, со времени доросла до менеджера доставки. Потом перешла работать на Кутузова, ушла работать в другую компанию. Но поняла, что лучше Грильницы ничего нет и вернулась назад на Мартынова. Веселая, трудолюбивая, отзывчивая.",
                "quote": "«Люблю грильницу за её открытость, за отношение к сотрудникам, люблю наш ресторан, люблю радовать наших гостей»"
            }
        ]
    },
    {
        "id": 2,
        "name": "Ресторан Красноярский рабочий 87",
        "employees": [
            {
                "photo": "photos/2c69f172-5b4f-4dc9-becd-090099f463c6.jfif",
                "name": "Суксин Дмитрий Юрьевич",
                "role": "31 год, управляющий, стаж 2 года",
                "description": "Управляющий рестораном Красноярский рабочий 87. Лидер команды, ответственный за все процессы в ресторане.",
                "quote": ""
            },
            {
                "photo": "photos/6df8af7d-1f70-48fe-a7b0-b90d5f3cdcb9.jfif",
                "name": "Кылычбек кызы Элиза",
                "role": "30 лет, стаж 5 лет",
                "description": "Одна из опытнейших сотрудников ресторана. Профессионал своего дела, наставник для новичков.",
                "quote": ""
            },
            {
                "photo": "photos/10dcacd1-8678-4903-be80-97c0eb1a4a58.jfif",
                "name": "Каблукова Анастасия Владимировна",
                "role": "18 лет, стаж 2 года",
                "description": "За время работы в компании достигла должности менеджера смены, начиная с кассира. На моем пути мне встретились прекрасные коллеги, которые помогли мне добиться отличных результатов и поделились с мной большим опытом!",
                "quote": ""
            },
            {
                "photo": "photos/1d943e78-33c0-4356-9f8f-a4a64046523e.jfif",
                "name": "Кузьмина Виктория Александровна",
                "role": "31 год, стаж 4 года",
                "description": "В компанию пришла работать пиццером, постепенно обучилась работать на всех станциях, стала старшим поваром. Добрая, отзывчивая, терпеливая, целеустремленная, ответственная.",
                "quote": "«Моя команда лучшая мы вместе развиваемся и делаем показатели»"
            }
        ]
    },
    {
        "id": 3,
        "name": "Ресторан Вильского 26/1",
        "employees": [
            {
                "photo": "photos/fb60fe86-67b8-41f2-ba3e-9f07c3d8f0b3.jfif",
                "name": "Ахмеджанова Диана",
                "role": "26 лет, управляющая, стаж 5 лет",
                "description": "Управляющая рестораном Вильского 26/1. Опытный руководитель с пятилетним стажем работы в компании.",
                "quote": ""
            },
            {
                "photo": "photos/26ce7279-8034-4361-a272-0a244e9ac1c5.jfif",
                "name": "Ахмеджанова Дарья",
                "role": "23 года, стаж 5 лет",
                "description": "Опытный сотрудник ресторана с пятилетним стажем. Профессионал в своем деле.",
                "quote": ""
            },
            {
                "photo": "photos/acfd316e-2d8a-4bd7-abed-3a18b0d559cc.jfif",
                "name": "Абдуллаева Дилфуза",
                "role": "28 лет, стаж 5 лет",
                "description": "Пришла в апреле 2021 года. Карьера: уборщица → холодный цех → повар шаурмы → повар универсала (2023). Замечательный пример карьерного роста в компании!",
                "quote": "«Мне нравится здесь работать потому что хорошая команда, есть карьерный рост, хорошее отношение компании к сотрудникам»"
            },
            {
                "photo": "photos/15a774b3-0103-48c5-8d30-cb6685bf324b.jfif",
                "name": "Давыдов Денис",
                "role": "18 лет, стаж 2 года",
                "description": "Начал работать в Грильнице в 2023 году, когда ему было 16. Карьера: кассир → менеджер доставки → кухня повар гриль/шаурмы → освоил станцию яблоний. Очень добрый, отзывчивый, трудолюбивый человек.",
                "quote": "«Мне нравится работать в грильнице, потому что здесь классный коллектив»"
            },
            {
                "photo": "photos/f2676e70-ce61-4440-8275-503b5bdc854c.jfif",
                "name": "Моложникова Маргарита",
                "role": "19 лет, стаж 1,5 года",
                "description": "Пришла работать в 2024 году на должность кассира. В 2025 году доросла до должности старший кассир. Целеустремленная и ответственная, грамотно и уверенно презентует скрипт кассира.",
                "quote": "«Мне нравится работать в Грильнице, здесь хорошая перспектива карьерного роста, классная команда»"
            },
            {
                "photo": "photos/19931cdf-6314-4d8e-bf02-f4894160dede.jfif",
                "name": "Гайс Дана",
                "role": "28 лет, стаж 4,5 года",
                "description": "Пришла в компанию в 2022 году на должность кассира. В первый же день стажировки оценили сообразительность, предложили должность менеджера доставки. К концу 2022 года доросла до должности менеджера смены. Упорство, лидерство, невероятная харизма!",
                "quote": "«Люблю работать в Грильнице, потому что здесь можно развиваться, нравится выполнять все показатели, и команда стала для меня семьей!»"
            },
            {
                "photo": "photos/7b5adac1-ddef-410f-9440-12be3759b45d.jfif",
                "name": "Исмаилова Татьяна",
                "role": "66 лет, стаж 3 года",
                "description": "Пришла в компанию в 2023 году на должность повара холодного цеха. В 2025 году освоила станцию гриль. В начале этого года освоила станцию шаурмы. Очень любит станцию холодного цеха, наладила логистику заготовок на всех станциях. Трудолюбивая, добрая, открытая.",
                "quote": "«Команда - огонь, все слаженно, работаем добросовестно. Компания всегда идет на встречу, нет не решаемых вопросов. Мы не стоим на месте, все лучше и лучше. Спасибо Грильница, мы лучшие, компания № 1»"
            },
            {
                "photo": "photos/b90a33ec-1c60-4a33-bb7f-4eb73d34951c.jfif",
                "name": "Козлова Татьяна",
                "role": "51 год, стаж 5 лет",
                "description": "В 2021 года пришла на должность фей чистоты и по сей день наводит порядок и уют. Открытая, добрая, веселая и чистолюбивая, что очень помогает в её работе.",
                "quote": "«Мне нравится работать в Грильнице, потому что здесь самая лучшая команда. Живу близко к работе, все удобства для работы всегда предоставляют»"
            }
        ]
    },
    {
        "id": 4,
        "name": "Ресторан Металлургов 53",
        "employees": [
            {
                "photo": "photos/db870c32-1930-48fd-b6a6-e216c9480ac0.jfif",
                "name": "Миракшев Тойир",
                "role": "21 год, стаж 2,5 года",
                "description": "Начал работать поваром, постепенно обучился до универсала и стал Старшим поваром. Ответственный сотрудник работающий на результат.",
                "quote": ""
            },
            {
                "photo": "photos/ebb79be9-4e8e-4209-b4e1-dea9c4d0fb97.jfif",
                "name": "Бобоколонова Рахима",
                "role": "36 лет",
                "description": "Пришла работать в Грильницу уборщицей, дальше повысили её до повара пиццы, она научилась всем станциям и уже в 2025 году стала Старшим поваром.",
                "quote": "«Терпение и труд - все перетрут»"
            },
            {
                "photo": "photos/92fcc065-e0a2-49f9-b36f-eecf22b280ce.jfif",
                "name": "Чувичкина Ангелина",
                "role": "22 года, стаж 2,5 года",
                "description": "Пришла работать кассиром, за годы доросла до Менеджера смены.",
                "quote": "«Не все в курсе, но, оказывается, можно иметь работу своей мечты»"
            },
            {
                "photo": "photos/00e9a787-2b4d-452c-988a-7f7f6d41d361.jfif",
                "name": "Баган Елизавета",
                "role": "21 год, стаж 4 года",
                "description": "Пришла работать кассиром, доросла до менеджера доставки в 2024 году, и стала Менеджером Смены в 2025 году.",
                "quote": "«Там где твой труд ценят, работать легко»"
            }
        ]
    },
    {
        "id": 5,
        "name": "Ресторан Кутузова 1/5",
        "employees": [
            {
                "photo": "photos/9305a58f-78ec-4efa-84d6-dc408181647c.jfif",
                "name": "Липовцев Андрей",
                "role": "Управляющий, стаж 2,5 года",
                "description": "Управляющий рестораном Кутузова 1/5. Опытный руководитель, лидер команды.",
                "quote": ""
            },
            {
                "photo": "photos/a6255703-5173-479f-8acb-7f011efd3be3.jfif",
                "name": "Филяева Александра",
                "role": "Стаж 1,5 года",
                "description": "Пришла в октябре 2024 года на кассира, через месяц ей предложили на менеджера доставки, через 3 месяца повысили до повара пиццера. Далее постепенно освоила все станции, в 2026 году доросла до повара универсала. Сейчас работает старшим поваром. Ответственная, любит смеяться, веселиться, рыбные котлеты на штат и вкладываться в работу ресторана.",
                "quote": "«Мне нравится здесь работать потому что у нас самый лучший управляющий, есть карьерный рост, мы стали как одна семья»"
            },
            {
                "photo": "photos/1bb440b9-97f3-4121-997d-c7a3e94a12e6.jfif",
                "name": "Урюпина Валерия",
                "role": "Стаж 4 года",
                "description": "Пришла 1 апреля 2022 года на сушиста на пару месяцев но так понравилось что осталась по сей день. Через время стала менеджером смены, так и пошло развитие в карьере и теплая привязанность к кухне и коллективу. Трудолюбивая, любит улыбаться.",
                "quote": "«Очень атмосферный коллектив, хороший рост, интересные задачи, рада что попала именно сюда»"
            }
        ]
    },
    {
        "id": 6,
        "name": "Ресторан Судостроительная 52А",
        "employees": [
            {
                "photo": "photos/baeab0bc-a04f-4018-9a67-800a271b77c9.jfif",
                "name": "Крис (Полина)",
                "role": "Стаж 2,5 года",
                "description": "Пришла 27 октября 2023 года по чистой случайности 😊 Когда только устроилась думала, что это только на пару месяцев, но в итоге меня затянуло на столько, что уже идёт третий год 😊 Я не жалею конечно, это место меня многому научило, а особенно выносливости (это я про запары и тяжебесие стажеров-думаю жиза 😊). Мне нравится мой коллектив, он интересный и очень весёлый:) О себе мне, наверное, нечего особо сказать об этом могут как раз рассказать именно мои коллеги, но думаю они бы точно сказали: \"Крис у нас бука, но при этом очень мягкий человек, который никогда не откажет и всегда поможет, если надо. И когда есть время и возможность всегда покормит нас шаткой, которую мы просто обожаем!\"",
                "quote": "«Мне нравится работать в грильнице потому что работаю с самой лучшей управляющей, сама атмосфера общепита и прокачивать поварские навыки»"
            }
        ]
    }
]

# Генерируем HTML
output = []

# Читаем заголовок и стили из page5_adaptive.txt
with open('page5_adaptive.txt', 'r', encoding='utf-8') as f:
    output.append(f.read())

# Генерируем контент для каждого ресторана
for rest in restaurants:
    output.append(f'\n      <!-- {rest["name"]} -->\n')
    output.append(f'      <div class="restaurant-section">\n')
    output.append(f'        <h2 class="restaurant-title">🏠 {rest["name"]}</h2>\n\n')

    # ДЕСКТОП - СЕТКА
    output.append(f'        <!-- Десктопная версия - СЕТКА -->\n')
    output.append(f'        <div class="employee-grid">\n')
    for emp in rest["employees"]:
        output.append(f'          <div class="employee-card">\n')
        output.append(f'            <img src="{emp["photo"]}" alt="{emp["name"]}">\n')
        output.append(f'            <h3>{emp["name"]}</h3>\n')
        output.append(f'            <p class="role">{emp["role"]}</p>\n')
        output.append(f'            <div class="description">{emp["description"]}</div>\n')
        if emp["quote"]:
            output.append(f'            <div class="quote">{emp["quote"]}</div>\n')
        output.append(f'          </div>\n')
    output.append(f'        </div>\n\n')

    # МОБИЛЬНАЯ - КАРУСЕЛЬ
    output.append(f'        <!-- Мобильная версия - КАРУСЕЛЬ -->\n')
    output.append(f'        <div class="carousel-container">\n')
    output.append(f'          <button class="carousel-btn carousel-btn-prev" onclick="prevSlide({rest["id"]})">‹</button>\n')
    output.append(f'          <div class="carousel-track" id="track-{rest["id"]}">\n')
    for emp in rest["employees"]:
        output.append(f'            <div class="carousel-card">\n')
        output.append(f'              <img src="{emp["photo"]}" alt="{emp["name"]}">\n')
        output.append(f'              <h3>{emp["name"]}</h3>\n')
        output.append(f'              <p class="role">{emp["role"]}</p>\n')
        output.append(f'              <div class="description">{emp["description"]}</div>\n')
        if emp["quote"]:
            output.append(f'              <div class="quote">{emp["quote"]}</div>\n')
        output.append(f'            </div>\n')
    output.append(f'          </div>\n')
    output.append(f'          <button class="carousel-btn carousel-btn-next" onclick="nextSlide({rest["id"]})">›</button>\n')
    output.append(f'        </div>\n')
    output.append(f'        <div class="carousel-dots" id="dots-{rest["id"]}"></div>\n')
    output.append(f'      </div>\n\n')

output.append('    </div>\n')
output.append('  </section>\n\n')

# JavaScript для карусели
output.append('  <script>\n')
output.append('const carousels = {};\n\n')
output.append('function initCarousel(restaurantId, count) {\n')
output.append('  carousels[restaurantId] = { current: 0, total: count };\n')
output.append('  const dotsContainer = document.getElementById(`dots-${restaurantId}`);\n')
output.append('  if (!dotsContainer) return;\n')
output.append('  dotsContainer.innerHTML = "";\n')
output.append('  for (let i = 0; i < count; i++) {\n')
output.append('    const dot = document.createElement("span");\n')
output.append('    dot.className = `carousel-dot ${i === 0 ? "active" : ""}`;\n')
output.append('    dot.onclick = () => goToSlide(restaurantId, i);\n')
output.append('    dotsContainer.appendChild(dot);\n')
output.append('  }\n')
output.append('  updateCarousel(restaurantId);\n')
output.append('}\n\n')
output.append('function updateCarousel(restaurantId) {\n')
output.append('  const carousel = carousels[restaurantId];\n')
output.append('  if (!carousel) return;\n')
output.append('  const { current } = carousel;\n')
output.append('  const track = document.getElementById(`track-${restaurantId}`);\n')
output.append('  const dots = document.querySelectorAll(`#dots-${restaurantId} .carousel-dot`);\n')
output.append('  if (track) track.style.transform = `translateX(-${current * 100}%)`;\n')
output.append('  dots.forEach((dot, i) => dot.classList.toggle("active", i === current));\n')
output.append('}\n\n')
output.append('function nextSlide(restaurantId) {\n')
output.append('  const carousel = carousels[restaurantId];\n')
output.append('  if (!carousel) return;\n')
output.append('  carousel.current = (carousel.current + 1) % carousel.total;\n')
output.append('  updateCarousel(restaurantId);\n')
output.append('}\n\n')
output.append('function prevSlide(restaurantId) {\n')
output.append('  const carousel = carousels[restaurantId];\n')
output.append('  if (!carousel) return;\n')
output.append('  carousel.current = (carousel.current - 1 + carousel.total) % carousel.total;\n')
output.append('  updateCarousel(restaurantId);\n')
output.append('}\n\n')
output.append('function goToSlide(restaurantId, index) {\n')
output.append('  const carousel = carousels[restaurantId];\n')
output.append('  if (!carousel) return;\n')
output.append('  carousel.current = index;\n')
output.append('  updateCarousel(restaurantId);\n')
output.append('}\n\n')
output.append('if (typeof window !== "undefined") {\n')
output.append('  window.addEventListener("DOMContentLoaded", () => {\n')
for rest in restaurants:
    count = len(rest["employees"])
    output.append(f'    initCarousel({rest["id"]}, {count});\n')
output.append('  });\n')
output.append('}\n')
output.append('  </script>\n')

# Записываем результат
with open('page5_final.txt', 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f"OK: Создан page5_final.txt с {len(restaurants)} ресторанами")
for rest in restaurants:
    print(f"  - {rest['name']}: {len(rest['employees'])} сотрудников")
