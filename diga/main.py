import os
import time
import datetime

import sqlite3

import requests
'''
activate_this_file = os.path.join('..','.venv','Scripts','activate.bat')

exec(open(activate_this_file).read())
'''


looping = True


base_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(base_path,'data')
tmp_path = os.path.join(data_path,'tmp')

tmp_link_storage_file = os.path.join(tmp_path,'tmp_links.diga')
tmp_idea_storage_file = os.path.join(tmp_path,'tmp_ideas.diga')
tmp_diary_storage_file = os.path.join(tmp_path,'tmp_diary.diga')

db_path = os.path.join(data_path,'diga.db')

def db_connect(db_path):
    con = sqlite3.connect(db_path)
    return(con)


def create_table(table_name,keys,con):
    # Create table
    key_line = ''
    key_index = 0
    for key in keys:
        if key_index == 0:
            key_line += key
        else:
            key_line += f', {key}'
    cur.execute(f'''CREATE TABLE {table_name} ({key_line})''')

def prompt():
    print('''\nWhat would you like to do?
            \n\t[link] Write a link
            \n\t[idea] Write an idea
            \n\t[article] Get an article
            \n\t[diary] Write diary input
            \n\t[clear] Clear tmp links file
            \n\t[exit]
            ''')
    resp = input('\n-- ')

    ######################### INPUT CONDITIONS ######################
    if resp.lower() == 'link' or resp.lower() == 'l':
        link = input('What link would you like to write? \n')
        tag = input('Tag?\t')
        write_link(tag,link)
        looping = True

    elif resp.lower() == 'idea' or resp.lower() == 'i':
        idea = input('What idea would you like to write? \n')
        tag = input('Tag?\t')
        write_idea(tag,idea)
        looping = True

    elif resp.lower() == 'article' or resp.lower() == 'a':
        url = input("\n\t--What is the url?")
        file_name = input("\n\t--What would you like to name the article?  \n\t")
        get_article(url,file_name)
        looping = True


    elif resp.lower() == 'diary' or resp.lower() == 'd' :
        idea = print('Diary input, type ;; to end: \n')
        contents = run_diary()
        tag = input('Tag?\t')
        write_diary(tag,contents)

        looping = True

    elif resp.lower() == 'clear' or resp.lower() == 'c':
        cl = input('''Which tmp files would you like to be cleared?
                        [links]
                        [ideas]
                        [diary]
                        [all]
                    \n- ''')
        if cl.lower() == 'links':
            clear_tmp(tmp_link_storage_file)
        elif cl.lower() == 'ideas':
            clear_tmp(tmp_idea_storage_file)
        elif cl.lower() == 'diary':
            clear_tmp(tmp_diary_storage_file)
        elif cl.lower() =='all':
            clear_tmp(tmp_diary_storage_file)
            clear_tmp(tmp_idea_storage_file)
            clear_tmp(tmp_link_storage_file)

        looping = True
    elif resp.lower() == 'exit':
        looping = False
    else:
        print("\nInvalid input\n")
        looping = True
    return(looping)

def run_diary():
    contents = []
    diary_running = True
    while diary_running:
        line = input()
        contents.append(line)
        if ';;' in line:
            contents.append('}\n')
            diary_running = False
    return(contents)

def write_diary(tag,contents):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('\n{\n%Y-%m-%d %H:%M:%S')
    line = "{}\nTags:{}\n\t ".format(st,tag)
    with open(tmp_diary_storage_file,'a') as f:

        f.write(line)
        f.write('\n')
        f.close()
    with open(tmp_diary_storage_file,'a') as f:
        f.write("Contents:\n\t")
        for line in contents:
            f.write(line)
            f.write('\n')
        f.close()
    return()



def write_link(tag,link):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    line = "{},{},{}".format(st,tag,link)
    with open(tmp_link_storage_file,'a') as f:

        f.write(line)
        f.write('\n')
        f.close()
    return()

def write_idea(tag,idea):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    line = "{},{},{}".format(st,tag,idea)
    with open(tmp_idea_storage_file,'a') as f:
        f.write(line)
        f.write('\n')
        f.close()
    return()


def commit():
    a = 2
    return()
def clear_tmp(tmp_file):
    print('\nClearing Temp Files\n')
    with open(tmp_file,'w') as f:
        f.write('')
        f.close()
    return()


def get_article(url,file_name):
    article = requests.get(url)
    with open(os.path.join('articles',file_name),'wb') as f:
        f.write(article.content)
        f.close()
    return()



while looping == True:
    looping = prompt()
    os.system('cls||clear')
