import json
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



def count_word_in_json(file_path, word):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        # fonction to search the @ in the file
        def search_in_json(obj):
            nonlocal count
            if isinstance(obj, dict):
                for key, value in obj.items():
                    search_in_json(value)
            elif isinstance(obj, list):
                for item in obj:
                    search_in_json(item)
            elif isinstance(obj, str):
                count += obj.count(word)
                
        search_in_json(data)
    
    return count

# number of json files that you have (remove if you have less)
file_path = (r'path')
file_path2 = (r'path')
file_path3 = (r'path')
file_path4 = (r'path')
file_path5 = (r'path')

#put the usernames in the convo
username = ''
username2 = ''
names = [username, username2]


occurrences1 = count_word_in_json(file_path, username) + count_word_in_json(file_path2, username) + count_word_in_json(file_path3, username) + count_word_in_json(file_path4, username) + count_word_in_json(file_path5, username)

occurrences2 = count_word_in_json(file_path, username2) + count_word_in_json(file_path2, username2) + count_word_in_json(file_path3, username2) + count_word_in_json(file_path4, username2) + count_word_in_json(file_path5, username2)
nbword = [occurrences1, occurrences2]
c = ['red', 'blue']


fig, ax = plt.subplots()

a = plt.barh(names, nbword, color=c, label=list)

plt.bar_label(a, label_type='center', color='white')

ax.set_title('Number of messages')

plt.show()
