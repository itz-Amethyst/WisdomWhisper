import requests
import pyfiglet
import sys
import random
import inquirer

ocate_quotes = [
    "Run fast. Hit fast. Win fast.",
    "Come by casa de Octane for a cold one!",
    "By the time you see me coming, I'll be going, and you'll be gone.",
    "They say Death catches up to everyone. He can certainly try!",
    "My legs are ready to go! (Some assembly required.)",
    "Just wanna give a shoutout to all my fans watching.",
    "Catch me if you can.",
    "Don't worry about my legs getting tired. I made sure that will never happen again! [laughs]",
    "I'm going up, and you're going down.",
    "I do this for the rush. The fans are just a bonus.",
    "I like the wind in my hair, bugs in my teeth, and long walks off a high cliff.",
    "I make it look easy, but I'm still the champ.",
    "Better watch your front! I'm always in the lead.",
    "I can see all of you in the rearview mirror.",
    "Mira, check out that giant banner of me! Awesome!",
    "See that blur right before you bite it? That's me!",
    "The good news is that with me, at least it will be over quick!",
    "Time is flying, and I am too.",
    "You all ready for the Octrain?",
    "You better run. Make it interesting.",
    "You think I'm afraid of you? I blew off my own legs!"
    ]


def main():
    apply_selected_font()
    select_category()


def select_figlet_font():
    choices = ["standard - recommended!", "weird", "univers", "type_set", "tombstone", "stop", "starwars", "slant", "fuzzy", "poison"]
    valid_fonts = [font for font in choices]

    if not valid_fonts:
        raise ValueError("None of the specified fonts are available.")

    
    questions = [inquirer.List('font',message="Select a Figlet font:",choices=valid_fonts,)]
    answers = inquirer.prompt(questions)
    return answers['font'].replace(" - recommended!", "")

def apply_selected_font():
    global selected_font
    try:
        selected_font = select_figlet_font()

        figlet_text = pyfiglet.figlet_format("Hello, Figlet!", font=selected_font)
        print(figlet_text)
    except ValueError as e:
        print(e)


def select_category():
    choices = ["Warhammer 40K Darktide", "Apex Legends(Octane)"]
    valid_categories = [font for font in choices]

    if not valid_categories:
        raise ValueError("None of the specified categories are available.")

    questions = [inquirer.List('category',message="Select a Category Quotes:",choices=valid_categories,)]
    answers = inquirer.prompt(questions)
    print_data(answers['category'])


def print_data(category):
    try:
        
        if category == "Warhammer 40K Darktide":
            get_darktide_quotes()
            generate_another_one(category)

            
        elif category == "Apex Legends(Octane)":
            get_octane_randomly()
            generate_another_one(category)


    except Exception:
        print("Wrong Category")
        sys.exit(1)


def get_darktide_quotes():
    gist_url = "https://api.github.com/gists/1548c09877ac012ed181fa067fd9b1d7"
    file_name = "darktide_warhammer_quotes.txt"

    response = requests.get(gist_url)

    if response.status_code == 200:
        gist_data = response.json()
            
        # Check if the file exists in the gist
        if file_name in gist_data['files']:
            file_content_url = gist_data['files'][file_name]['raw_url']
                
            # Now fetch the content of the file
            file_content_response = requests.get(file_content_url)
                
            if file_content_response.status_code == 200:
                quotes_data = file_content_response.text
                quotes_list = quotes_data.splitlines()

                random_quote = random.choice(quotes_list)
                print_in_figlet_way(random_quote)
            else:
                print(f"Failed to retrieve file content. Status code: {file_content_response.status_code}")
        else:
            print(f"The file '{file_name}' does not exist in the gist.")
    else:
        print(f"Failed to retrieve gist data. Status code: {response.status_code}")


def get_octane_randomly():
    random_quote = random.choice(ocate_quotes)

    print_in_figlet_way(random_quote)
   

def generate_another_one(category):
    questions = [inquirer.List('generate_another',message="Generate another one?",choices=['Yes', 'No'],default='Yes',),]

    answers = inquirer.prompt(questions)
    user_input = answers['generate_another'].lower()

    if user_input == 'yes':
        print_data(category)
    elif user_input == 'no':
        print("Exiting...")
        sys.exit(1)
    else:
        print("Invalid input. Please select 'Yes' or 'No.")


def print_in_figlet_way(text, selected_font = 'mini'):
    figlet_text = pyfiglet.figlet_format(text, font = selected_font, width=90, justify="center")

    print(figlet_text)

if __name__ == "__main__":
    main()