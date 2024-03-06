from fpdf import FPDF

class MyPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 35)
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align = 'C')

    def add_name(self, name):
        self.set_font('Arial', '', 25)
        self.set_text_color(255, 255, 255)
        self.text(x =60, y= 140, txt = f"{name} took CS50")

    def add_shirt_image(self, image_path):
        self.image(image_path,  w=self.epw)

def shirtir(name):
    pdf = MyPDF(format='A4', orientation='P')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.add_shirt_image("shirtificate.png")
    pdf.add_name(name)
    pdf.output("shirtificate.pdf")

def main():
    shirtir(input('Name: '))

if __name__ == "__main__":
    main()
