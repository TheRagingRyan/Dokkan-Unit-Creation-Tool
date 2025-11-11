import requests
from bs4 import BeautifulSoup
from dearpygui.dearpygui import *
import re

class Translations:
    
    Fandom_URL = 'https://dbz-dokkanbattle.fandom.com/wiki/'
    Fandom_Fallback_URL = 'https://dbz-dokkanbattle.fandom.com/wiki/'
    Character_Name = ''
    Active_Skill_Name = ''
    Active_Skill_Conditions = ''
    Active_Skill_Description = ''
    Leader_Skill_Name = ''
    Leader_Skill_Description = ''
    Passive_Description = ''
    Passive_Name = ''
    Super_Attacks_Names = []
    Super_Attacks = []
    Standby_Skill = ''
    Finish_Skills_Names = []
    Finish_Skills = []


def DokkanInfo():
    
    # Send a GET request to the website
    url = f'https://dokkaninfo.com/cards/' + get_value('Card ID')  # Replace with the desired website URL
    response = requests.get(url)

    # Get the HTML content
    html_content = response.content

    # Create a BeautifulSoup object for parsing the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # # Find all elements with tag 'td'
    meta_element = soup.find('meta', {'property': 'og:keywords'})
    text_element = soup.find('meta', {'name': 'description'})
    title_element = soup.find('meta', {'property' : 'og:title'})

    keywords_content = meta_element['content'].strip()
    text_element = text_element['content'].strip()
    title_element = title_element['content'].strip()
    
    pattern = r"\[[^\]]*\]"
    character_name = re.sub(pattern, '', title_element)
    
    if character_name[0] == ' ':
        character_name = character_name[1:]
        Translations.Character_Name = character_name
    else:
        Translations.Character_Name = character_name
        
    leader_skill_name = title_element.split('] ')
    leader_skill_name = leader_skill_name[0][1:]
    Translations.Leader_Skill_Name = leader_skill_name
    set_value('Leader_Name', leader_skill_name)
    text_width, text_height = get_text_size(leader_skill_name, font='fonts/ARIALBD.ttf')
    set_item_width('Leader_Desc', text_width + 10)
    
    title_element = title_element.replace('[', '').replace(']', '').replace(' ', '_')
    
    Translations.Fandom_Fallback_URL = Translations.Fandom_Fallback_URL + title_element
    print(Translations.Fandom_Fallback_URL)
    

    # # Loop through the elements and add spaces after </td>
    # # for element in elements:
    #     # Add a space after the text of each </td> tag
    #     # element.string = element.text + ' '

    # # Get the modified HTML content
    modified_html = soup.prettify()

    # # Print the modified HTML content



    # print(keywords_content)
    # print(text_element)
    start_index = keywords_content.find(text_element)
    # print(start_index)

    if start_index != -1:
        result_text = keywords_content[start_index:]
    else:
        result_text = keywords_content

    result_text = result_text.replace(text_element, '')
    result_text = result_text.replace(',', '', 1).lstrip()
    result_text = result_text[:-1]
    
    Translations.Passive_Description = result_text
    # Translations.Leader_Skill_Name = 

    card_id = get_value('Card ID')
    
    card_id = card_id[:-1] + '0'
    DokkanFandom(card_id)

def replace_numbers_inside_brackets(text):
    import re

    pattern = r'\[\d+\]'

    replaced_text = re.sub(pattern, '', text)
    
    replaced_text = add_newline_break(replaced_text, line_length=40)
    
    return replaced_text
    
def add_newline_break(text, line_length=40):
    # Define the regular expression pattern to match the whitespace after 40 characters
    pattern = rf'(.{{1,{line_length}}})(\s|$)'
    
    # Use re.sub() to find all occurrences of the pattern and add a new line break after each match
    replaced_text = re.sub(pattern, r'\1\n', text)
    
    return replaced_text

def DokkanFandom(card_id):
    
    def Translation_Info():
        try:
            Num_Of_Supers = get_value('Number_Of_Special_Sets')
            if Num_Of_Supers == 1:
                Translations.Super_Attacks_Names.append(content_list[0])
                Translations.Passive_Name = content_list[1]

                Translations.Super_Attacks.append(replace_numbers_inside_brackets(elements[1]))
                # Translations.Passive_Description = replace_numbers_inside_brackets(elements[2])
                if get_value('Active_Skill_Check'):
                    Translations.Active_Skill_Name = content_list[2]

                    Translations.Active_Skill_Description = replace_numbers_inside_brackets(elements[3])
                    Translations.Active_Skill_Conditions = replace_numbers_inside_brackets(elements[4])
                    Translations.Active_Skill_Description = Translations.Active_Skill_Description.replace('\n', ' ')
                    Translations.Active_Skill_Conditions = Translations.Active_Skill_Conditions.replace('\n', ' ')
            elif Num_Of_Supers == 2:
                Translations.Super_Attacks_Names.append(content_list[0])
                Translations.Super_Attacks_Names.append(content_list[1])
                Translations.Passive_Name = content_list[2]

                Translations.Super_Attacks.append(replace_numbers_inside_brackets(elements[1]))
                Translations.Super_Attacks.append(replace_numbers_inside_brackets(elements[2]))
                # Translations.Passive_Description = replace_numbers_inside_brackets(elements[3])
                if get_value('Active_Skill_Check'):
                    Translations.Active_Skill_Name = content_list[3]

                    Translations.Active_Skill_Description = replace_numbers_inside_brackets(elements[4])
                    Translations.Active_Skill_Conditions = replace_numbers_inside_brackets(elements[5])
                    Translations.Active_Skill_Description = Translations.Active_Skill_Description.replace('\n', ' ')
                    Translations.Active_Skill_Conditions = Translations.Active_Skill_Conditions.replace('\n', ' ')

            elif Num_Of_Supers == 3:
                Translations.Super_Attacks_Names.append(content_list[0])
                Translations.Super_Attacks_Names.append(content_list[1])
                Translations.Super_Attacks_Names.append(content_list[2])
                Translations.Passive_Name = content_list[3]

                Translations.Super_Attacks.append(replace_numbers_inside_brackets(elements[1]))
                Translations.Super_Attacks.append(replace_numbers_inside_brackets(elements[2]))
                Translations.Super_Attacks.append(replace_numbers_inside_brackets(elements[3]))
                # Translations.Passive_Description = replace_numbers_inside_brackets(elements[4])
                if get_value('Active_Skill_Check'):
                    Translations.Active_Skill_Name = content_list[4]

                    Translations.Active_Skill_Description = replace_numbers_inside_brackets(elements[5])
                    Translations.Active_Skill_Conditions = replace_numbers_inside_brackets(elements[6])
                    Translations.Active_Skill_Description = Translations.Active_Skill_Description.replace('\n', ' ')
                    Translations.Active_Skill_Conditions = Translations.Active_Skill_Conditions.replace('\n', ' ')
            
            Translations.Leader_Skill_Description = elements[0]
            set_value('Leader_Desc', elements[0])
            text_width, text_height = get_text_size(elements[0], font='fonts/ARIALBD.ttf')
            set_item_width('Leader_Desc', text_width + 10)

            set_value('Translation_Good', True)
        except Exception as e:
            print(e)
            set_value('log', 'Error getting unit information, Fandom said \"Fuck You!\"')
            set_value('Translation_Good', False)
            
    if get_value('Card_Rarity') is 5:
        url = Translations.Fandom_URL + f'File:Card_{card_id}_thumb_apng.png'
        
    else:
        url = Translations.Fandom_URL + f'File:Card_{card_id}_thumb.png'
        

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    
    td_elements = soup.find_all('td', colspan="2")
    # Find all elements with the <strong> tags
    strong_tags = soup.find_all('strong')
    
    
    if strong_tags:
        content_list = []
        elements = []
        # Loop through all the <strong> tags and extract the text
        for strong_tag in strong_tags:
            # Extract the text within <strong> tags
            content = strong_tag.get_text().strip()
            content_list.append(content)


        for td in td_elements:
            if td.text != '':
                elements.append(td.text)

        # print(content_list)
        del elements[0]
        # print(content_list)
        # print(elements)
        print(elements)
        
        Translation_Info()

        content_list.clear()
        elements.clear()
        # print(elements[1])
    
    else:
        url = Translations.Fandom_Fallback_URL

        # Send an HTTP request to the URL and get the HTML content of the page
        response = requests.get(url)
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        # content_list = []
        elements = []
        # Find all the strong tags in the page
        strong_tags = soup.find_all("strong")
        elements = soup.find_all("td", colspan="2")
        # Extract the text from each strong tag and store it in a list
        content_list = [strong_tag.get_text() for strong_tag in strong_tags]
        # td_text_list = [td.get_text() for td in elements]
        for td in td_elements:
            if td.text != '':
                elements.append(td.text)

        # Print the content of the strong tags
        # print(content_list)
        # print(elements)
        Translation_Info()
        content_list.clear()
        elements.clear()
            
        # del elements[0]
        # print(elements[1])
        # print(strong_tags)
        # div_element = body_element.find("div", id="mw-imagepage-section-linkstoimage")
        # print('div not found')
        

    
    # print(Translations.Super_Attacks)
    
    
