from fpdf import FPDF

def main():
    name = input("Name: ")
    make_shirtificate(name)

def make_shirtificate(name: str):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

    pdf.image("shirtificate.png", x=0, y=60, w=210)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    text = f"{name} took CS50"
    pdf.set_xy(0, 150)
    pdf.cell(210, 10, text, align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
