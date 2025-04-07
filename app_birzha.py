
import streamlit as st
import datetime
from docx import Document
import os

st.set_page_config(page_title="Биржевой Анализатор", layout="wide")
st.title("Биржевой Анализатор — отчёты по товарным биржам")

# Выбор периода
st.subheader("Выберите месяц и год для анализа")
month = st.selectbox(
    "Месяц",
    ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
     "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
)
year = st.selectbox("Год", list(reversed(range(2020, datetime.datetime.now().year + 1))))

# Кнопка запуска анализа
if st.button("Сформировать отчёт"):
    with st.spinner("Идёт сбор и анализ публикаций по биржам..."):
        # ЗАГЛУШКА: Здесь будет подключение к поиску и анализу новостей
        articles = [
            {
                "title": "Казахстанская товарная биржа провела рекордные торги по углю",
                "summary": "Объём сделок по углю в октябре достиг 2.3 млрд тенге...",
                "url": "https://example.kz/birzha-oct2022",
                "lang": "RU"
            },
            {
                "title": "Kazakh exchange reports increase in commodity trading volume",
                "summary": "Total coal trading volume on the exchange grew 18% in October.",
                "translation": "Общий объём торговли углём на бирже вырос на 18% в октябре.",
                "url": "https://example.com/kz-commodity-oct2022",
                "lang": "EN"
            }
        ]

        # Создание Word-документа
        doc = Document()
        doc.add_heading(f"Биржевой анализ — {month} {year}", 0)
        doc.add_paragraph(f"Период: {month} {year}")
        doc.add_paragraph(f"Всего публикаций: {len(articles)}")

        for i, a in enumerate(articles, 1):
            doc.add_paragraph(f"{i}. {a['title']}")
            doc.add_paragraph(a["summary"])
            if a["lang"] == "EN" and "translation" in a:
                doc.add_paragraph(f"Перевод: {a['translation']}")
            doc.add_paragraph(f"Источник: {a['url']}")
            doc.add_paragraph("")

        doc.add_heading("Выводы и рекомендации", level=1)
        doc.add_paragraph("Растущий объём торговли углём требует внимания к инфраструктуре биржи и прозрачности операций.")

        file_name = f"birzha_report_{month}_{year}.docx"
        file_path = os.path.join("./", file_name)
        doc.save(file_path)

        with open(file_path, "rb") as f:
            st.download_button(
                label="Скачать отчёт в Word",
                data=f,
                file_name=file_name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        os.remove(file_path)
