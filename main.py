import mysql.connector
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='data_fb')

browser  = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("https://www.facebook.com/LuShangXin/videos/1099297274113281?idorvanity=364997627165697")
sleep(5)


# login
# txtemail = browser.find_element(By.ID, "email")
# txtemail.send_keys("hoangann2312@gmail.com")
# txtpass = browser.find_element(By.ID, "pass")
# txtpass.send_keys("pass")

# txtpass.send_keys(Keys.ENTER)

# i = 0
# while(i <= 20000):
#     browser.execute_script(f"window.scrollBy(0,1080)", "")
#     post_list = browser.find_elements(By.CLASS_NAME, "x1ja2u2z.xh8yej3.x1n2onr6.x1yztbdb")
#     print(post_list)
#     for post in post_list:
#         user_post = post.find_element(By.CLASS_NAME, "x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz.x1gslohp.x1yc453h")
#         print(user_post.text)
#     i += 1000

# post_list = browser.find_elements(By.CLASS_NAME, "x1ja2u2z.xh8yej3.x1n2onr6.x1yztbdb")
# for post in post_list:
#
#     user_post = post.find_element(By.CLASS_NAME, "x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz.x1gslohp.x1yc453h")
#     print(user_post.text)
#     user = post.find_element(By.CLASS_NAME,"x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x676frb.x1nxh6w3.x1sibtaa.x1s688f.xzsf02u")
#     content = post.find_element(By.CLASS_NAME, "xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs")
#     print(user.text)
#     print(content.text)
# sleep(5)


#click hiện comment
comment_more = browser.find_element(By.CLASS_NAME, "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.x1s688f.xi81zsa")
comment_more.click()
sleep(5)

# lấy div comment
detail_post = browser.find_elements(By.CLASS_NAME, "x1r8uery.x1iyjqo2.x6ikm8r.x10wlt62.x1pi30zi")
print(detail_post)
for i in detail_post:
    user_comment = i.find_element(By.CLASS_NAME, "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x676frb.x1nxh6w3.x1sibtaa.x1s688f.xzsf02u")
    content_comment = i.find_element(By.CLASS_NAME, "xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs")
    field1 = user_comment.text
    field2 = content_comment.text
    print(field1, "----",field2)
    data_employee = ("INSERT INTO users "
                     "(user_comment, content_comment) "
                     f"VALUES (%s,%s)")
    add_employee = (field1, field2)
    a = cnx.cursor()
    a.execute(data_employee,add_employee)
    cnx.commit()

cnx.close()