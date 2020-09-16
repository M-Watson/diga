import os
import time
import datetime


looping = True


base_path = os.getcwd()
data_path = os.path.join(base_path,'data')
tmp_path = os.path.join(data_path,'tmp')

tmp_link_storage_file = os.path.join(tmp_path,'tmp_links.diga')
tmp_idea_storage_file = os.path.join(tmp_path,'tmp_ideas.diga')

def prompt():
    print('''\nWhat would you like to do?
            \n\t[link] Write a link
            \n\t[idea] Write an idea
            \n\t[clear] Clear tmp links file
            \n\t[exit]
            ''')
    resp = input('\n-- ')
    if resp.lower() == 'link':
        link = input('What link would you like to write? \n')
        tag = input('Tag?\t')
        write_link(tag,link)
        looping = True
    elif resp.lower() == 'idea':
        idea = input('What idea would you like to write? \n')
        tag = input('Tag?\t')
        write_idea(tag,idea)
        looping = True

    elif resp.lower() == 'clear':
        cl = input('''Which tmp files would you like to be cleared?
                        [links]
                        [ideas]
                    \n- ''')
        if cl.lower() == 'links':
            clear_tmp(tmp_link_storage_file)
        elif cl.lower() == 'ideas':
            clear_tmp(tmp_idea_storage_file)

        looping = True
    elif resp.lower() == 'exit':
        looping = False
    else:
        print("\nInvalid input\n")
        looping = True
    return(looping)

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

def clear_tmp(tmp_file):
    print('\nClearing Temp Files\n')
    with open(tmp_file,'w') as f:
        f.write('')
        f.close()
    return()

while looping == True:
    looping = prompt()
