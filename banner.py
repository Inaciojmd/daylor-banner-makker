import pyfiglet

def create_banner(text, font="standard"):
    if font not in pyfiglet.FigletFont.getFonts():
        font = "standard" 
    banner = pyfiglet.figlet_format(text, font=font)
    return banner

if __name__ == "__main__":
    input_text = input("Enter text for the banner: ")

    available_fonts = pyfiglet.FigletFont.getFonts()
    print("\nAvailable fonts:")
    for i, font in enumerate(available_fonts, start=1):
        print(f"{i}. {font}")

    selected_font = input("Select a font number (1-{}): ".format(len(available_fonts)))
    selected_font = available_fonts[int(selected_font) - 1]

    banner_result = create_banner(input_text, font=selected_font)
    print("\nBanner:")
    print(banner_result)