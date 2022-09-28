import time
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tkinter import *

from selenium.webdriver.support.wait import WebDriverWait


# wait_sec = 3
# keys_c = {'0': Keys.NUMPAD0,
#           '1': Keys.NUMPAD1,
#           '2': Keys.NUMPAD2,
#           '3': Keys.NUMPAD3,
#           '4': Keys.NUMPAD4,
#           '5': Keys.NUMPAD5,
#           '6': Keys.NUMPAD6,
#           '7': Keys.NUMPAD7,
#           '8': Keys.NUMPAD8,
#           '9': Keys.NUMPAD9}


# driver = None


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.web_driver = NONE
        # self.title = "Удаление трэков"

        Label(self, text="Выбери браузер ").grid(column=0, row=0)
        self.combo = tkinter.ttk.Combobox()
        self.combo['values'] = ("FireFox", "Chrome")
        self.combo.current(0)
        self.combo.grid(column=1, row=0)

        Label(self, text="Логин: ").grid(column=0, row=1)
        self.login_txt = StringVar()
        Entry(self, width=23, textvariable=self.login_txt).grid(column=1, row=1)

        Label(self, text="Пароль: ").grid(column=0, row=2)
        self.password_txt = StringVar()
        Entry(self, width=23, textvariable=self.password_txt).grid(column=1, row=2)

        Label(self, text="Что будем удалять?").grid(column=0, row=3)
        self.selected = IntVar()
        Radiobutton(self, text="Все трэtки", value=1, variable=self.selected).grid(column=1, row=3)
        Radiobutton(self, text="Только лайкнутые", value=2, variable=self.selected).grid(column=1, row=4)

        Label(self, text="Сколько треков удалить?").grid(column=0, row=5)
        self.amount = StringVar()
        Entry(width=23, textvariable=self.amount).grid(column=1, row=5)

        Button(self, text='Удалить', command=self.delete_music).grid(column=0, row=6)

        # Label(self, text="Надо ввести код из смс").grid(column=0, row=5)
        # self.kod = StringVar()
        # self.entry_kod = Entry(self, width=23, textvariable=self.kod, state='disabled').grid(column=1, row=5)
        # self.button_kod = Button(self, text='Ввести', command=self.podtv, state='disabled').grid(column=0, row=6)

    def delete_music(self):
        self.web_driver = Driver(self.combo.get())
        # if self.combo.get() == "FireFox":
        #     driver = webdriver.Firefox()
        # elif self.combo.get() == "Chrome":
        #     driver = webdriver.Chrome()
        #
        # driver.set_window_size(600, 800)
        # driver.get(
        #     "https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D40774908516613193747876383989412377%26from-passport")
        try:
            # but = WebDriverWait(driver, timeout=wait_sec).until(EC.element_to_be_clickable((By.XPATH,
            #                                                                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button")))
            # but.click()
            # driver.find_element("xpath", '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button').click()
            self.web_driver.click_on_email_enter()
            self.web_driver.input_login(self.login_txt.get())
            self.web_driver.input_password(self.password_txt.get())

            # self.confirm()
            # self.web_driver.delete(self.selected.get(), int(self.amount.get()))

            # self.enter_ligin()
            # print(EC.invisibility_of_element_located((By.ID, 'field:input-login:hintsdgfvefds')))
            # if EC.invisibility_of_element_located((By.ID, 'field:input-login:hint')):
            #     #// *[ @ id = "field:input-login:hint"]
            #     messagebox.showinfo("GUI Python", "Такого аккаунта нет")
            #     return
            # self.enter_pass()
            # but = WebDriverWait(driver, timeout=wait_sec).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/button')))
            # but.click()
        except TimeoutException:
            messagebox.showinfo("GUI Python", "Что-то пошло не так с логином или паролем")
            return
        else:
            try:
                self.confirm(self.selected.get(), int(self.amount.get()))
            except TimeoutException:
                messagebox.showinfo("GUI Python", "Подтверждение не нужно")
                try:
                    self.web_driver.delete(self.selected.get(), int(self.amount.get()))
                except TimeoutException:
                    messagebox.showinfo("GUI Python", "Что-то пошло не так с удалением")
                    return
                # print("Подтверждение не нужно")
            # finally:
            #     try:
            #         self.web_driver.delete(self.selected.get(), int(self.amount.get()))
            #     except TimeoutException:
            #         messagebox.showinfo("GUI Python", "Что-то пошло не так с удалением")
            #         return

    # def podtv(self):
    #     try:
    #         print("DDD")
    #         print(self.kod)
    #         print(self.kod.get()[1])
    #         print(keys_c.get(self.kod[1]))
    #         # kod_field = WebDriverWait(driver, timeout=wait_sec).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/form/div[1]/div[2]/div")))
    #         ActionChains(driver) \
    #             .key_down(keys_c.get(self.kod.get()[1])).key_up(keys_c.get(self.kod.get()[1])) \
    #             .key_down(keys_c.get(self.kod.get()[2])).key_up(keys_c.get(self.kod.get()[2])) \
    #             .key_down(keys_c.get(self.kod.get()[3])).key_up(keys_c.get(self.kod.get()[3])) \
    #             .key_down(keys_c.get(self.kod.get()[4])).key_up(keys_c.get(self.kod.get()[4])) \
    #             .key_down(keys_c.get(self.kod.get()[5])).key_up(keys_c.get(self.kod.get()[5])) \
    #             .key_down(keys_c.get(self.kod.get()[6])).key_up(keys_c.get(self.kod.get()[6])) \
    #             .perform()
    #     except TimeoutException:
    #         messagebox.showinfo("GUI Python", "Что-то пошло не так")
    #         return

    # def enter_ligin(self):
    #     login = WebDriverWait(driver, timeout=wait_sec).until(
    #         EC.presence_of_element_located((By.ID, 'passp-field-login')))
    #     # login = driver.find_element("id", 'passp-field-login')
    #     # login.send_keys(login_txt.get())
    #     for i in range(len(self.login_txt.get())):
    #         login.send_keys(self.login_txt.get()[i])
    #         time.sleep(0.17)
    #     driver.find_element("id", "passp:sign-in").click()

    # def enter_pass(self):
    #     password = WebDriverWait(driver, timeout=wait_sec).until(
    #         EC.presence_of_element_located((By.ID, 'passp-field-passwd')))
    #     # password = driver.find_element("id", 'passp-field-passwd')
    #     # password.send_keys(password_txt.get())
    #     for i in range(len(self.password_txt.get())):
    #         password.send_keys(self.password_txt.get()[i])
    #         time.sleep(0.16)
    #     driver.find_element("id", "passp:sign-in").click()

    def confirm(self, where, amount):
        # but2 = WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                           "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/button")))
        # but2.click()
        # win_phone_kod(driver)
        self.web_driver.click_confirm()
        win2 = Window2(self, self.web_driver, where, amount)
        win2.title("Подтверждение профиля")
        win2.grab_set()
        # messagebox.showwarning("Предупреждение",
        #                        "Яндекс требует подтвердить номер телефона. Впишите в окно программы код из СМС.")
        # print(self.entry_kod)
        # self.entry_kod['state'] = tkinter.NORMAL
        # self.button_kod['state'] = tkinter.DISABLED


class Window2(tkinter.Toplevel):
    def __init__(self, parent, web_driver, where, amount):
        super().__init__(parent)
        self.web_driver = web_driver
        self.where = where
        self.amount = amount
        Label(self, text="Надо ввести код из смс").grid(column=0, row=0)
        self.kod = StringVar()
        self.entry_kod = Entry(self, width=23, textvariable=self.kod).grid(column=1, row=0)
        self.button_kod = Button(self, text='Ввести', command=self.confirm_phone_code).grid(column=0, row=1)

    def confirm_phone_code(self):
        try:
            self.web_driver.input_phone_code(self.kod.get())
        except TimeoutException:
            messagebox.showinfo("GUI Python", "Что-то пошло не так в ведении кода")
            return
        else:
            # try:
            self.quit()
            self.web_driver.delete(self.where, self.amount)
        # except TimeoutException:
        #   return


class Driver:
    def __init__(self, browser):
        self.wait_sec = 3
        self.keys_c = {'0': Keys.NUMPAD0,
                       '1': Keys.NUMPAD1,
                       '2': Keys.NUMPAD2,
                       '3': Keys.NUMPAD3,
                       '4': Keys.NUMPAD4,
                       '5': Keys.NUMPAD5,
                       '6': Keys.NUMPAD6,
                       '7': Keys.NUMPAD7,
                       '8': Keys.NUMPAD8,
                       '9': Keys.NUMPAD9}

        if browser == "FireFox":
            self.driver = webdriver.Firefox()
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()

        self.driver.set_window_size(600, 800)
        self.driver.get(
            "https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D40774908516613193747876383989412377%26from-passport")

    def click_on_email_enter(self):
        but = WebDriverWait(self.driver, timeout=self.wait_sec).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button")))
        but.click()

    def input_login(self, login_txt):
        login = WebDriverWait(self.driver, timeout=self.wait_sec).until(
            EC.presence_of_element_located((By.ID, 'passp-field-login')))
        for i in range(len(login_txt)):
            login.send_keys(login_txt[i])
            time.sleep(0.17)
        self.driver.find_element("id", "passp:sign-in").click()

    def input_password(self, password_txt):
        password = WebDriverWait(self.driver, timeout=self.wait_sec).until(
            EC.presence_of_element_located((By.ID, 'passp-field-passwd')))
        for i in range(len(password_txt)):
            password.send_keys(password_txt[i])
            time.sleep(0.16)
        self.driver.find_element("id", "passp:sign-in").click()

    def click_confirm(self):
        but2 = WebDriverWait(self.driver, timeout=self.wait_sec).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/button")))
        but2.click()

    def input_phone_code(self, code):
        # kod_field = WebDriverWait(driver, timeout=wait_sec).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/form/div[1]/div[2]/div")))
        ActionChains(self.driver) \
            .key_down(self.keys_c.get(code[0])).key_up(self.keys_c.get(code[0])) \
            .key_down(self.keys_c.get(code[1])).key_up(self.keys_c.get(code[1])) \
            .key_down(self.keys_c.get(code[2])).key_up(self.keys_c.get(code[2])) \
            .key_down(self.keys_c.get(code[3])).key_up(self.keys_c.get(code[3])) \
            .key_down(self.keys_c.get(code[4])).key_up(self.keys_c.get(code[4])) \
            .key_down(self.keys_c.get(code[5])).key_up(self.keys_c.get(code[5])) \
            .perform()

    def delete(self, where, amount):
        print(where)
        time.sleep(20)
        print(self.driver.title)
        self.driver.find_element("link text", "Коллекция").click()
        if where == 1:
            time.sleep(4)
            self.driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/a").click()
            time.sleep(1)
            self.driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[3]/nav/button[1]").click()
            time.sleep(3)
            for i in range(amount):
                traks = self.driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]")
                but_del = self.driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[3]/div[3]/div[1]/button")
                hov = ActionChains(self.driver).move_to_element(traks).click(but_del)
                hov.perform()
                print("Delete: ", i)
            # print('tttt')
            # # time.sleep(40)
            #
            # # self.driver.find_element("link text", "Коллекция").click()
            # # try:
            # #     kol = WebDriverWait(self.driver, timeout=self.wait_sec * 4).until(
            # #         EC.presence_of_element_located((By.LINK_TEXT, "Коллекция")))
            # #     kol.click()
            # #     print("rrrrr")
            # # except:
            # #     messagebox.showinfo("GUI Python", "Что-то пошло не так с переходом в коллекции")
            #
            # # kol.click()
            # try:
            #     alt = WebDriverWait(self.driver, timeout=self.wait_sec).until(
            #         EC.presence_of_element_located(
            #             (By.XPATH, "/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/a")))
            #     alt.click()
            # except:
            #     messagebox.showinfo("GUI Python", "Что-то пошло не так с переходом во все теки")
            # else:
            #     try:
            #         b = WebDriverWait(self.driver, timeout=self.wait_sec).until(
            #             EC.presence_of_element_located(
            #                 (By.XPATH, "/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/a")))
            #         b.click()
            #     except:
            #         messagebox.showinfo("GUI Python", "Что-то пошло не так с переключателем")
            #     else:
            #         for i in range(amount):
            #             trak = WebDriverWait(self.driver, timeout=self.wait_sec).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[9]/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]")))
            #             but_del = WebDriverWait(self.driver, timeout=self.wait_sec).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[9]/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[3]/div[3]/div[1]/button")))
            #             hov = ActionChains(self.driver).move_to_element(trak).click(but_del)
            #             hov.perform()
            #             print("Delete: ", i)
            # # driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/a").click()
        elif where == 2:
            print("d")
        else:
            messagebox.showinfo("GUI Python", "Выбери каталог")


if __name__ == "__main__":
    win = Window()
    win.title("Удаление трэков из Яндекс.Музыки")
    win.mainloop()

# def win_phone_kod(driver):
#     new_window = Tk().winfo_toplevel()
#     new_window.title("AAAA")
#     new_window.geometry("250x150+500+500")
#     Label(new_window, text="Надо ввести код из смс").grid(column=0, row=0)
#     kod = StringVar()
#     Entry(new_window, width=23, textvariable=kod).grid(column=0, row=1)
#     Button(new_window, text='Ввести', command=podtv(driver, kod.get())).grid(column=0, row=2)
#     new_window.mainloop()


#
# window = Tk()
# window.title("sdsdsd")
#
# Label(window, text="Выбери браузер ").grid(column=0, row=0)
# combo = Combobox(window)
# combo['values'] = ("FireFox", "Chrome")
# combo.current(0)
# combo.grid(column=1, row=0)
#
# Label(window, text="Логин: ").grid(column=0, row=1)
#
# login_txt = StringVar()
# Entry(window, width=23, textvariable=login_txt).grid(column=1, row=1)
#
# Label(window, text="Пароль: ").grid(column=0, row=2)
# password_txt = StringVar()
# Entry(window, width=23, textvariable=password_txt).grid(column=1, row=2)
#
# Label(window, text="Сколько треков удалить?").grid(column=0, row=3)
# n = Entry(window, width=23).grid(column=1, row=3)
#
# del_but = Button(window, text='Удалить', command=delete_music).grid(column=0, row=4)
#
# Label(window, text="Надо ввести код из смс").grid(column=0, row=5)
# kod = StringVar()
# entry_kod = Entry(window, width=23, textvariable=kod, state='disabled').grid(column=1, row=5)
# button_kod = Button(window, text='Ввести', command=podtv, state='disabled').grid(column=0, row=6)
#
# window.mainloop()


#
# driver = webdriver.Firefox()
# driver.get("https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D40774908516613193747876383989412377%26from-passport")
# time.sleep(1)
#
# login = driver.find_element("id", 'passp-field-login')
# login.send_keys("login")
# driver.find_element("id", "passp:sign-in").click()
# time.sleep(2)
#
# password = driver.find_element("id", 'passp-field-passwd')
# password.send_keys("password")
# driver.find_element("id", "passp:sign-in").click()
# time.sleep(40)
# print(driver.title)
#
########### driver.find_element("link text", "Коллекция").click()
# time.sleep(4)
# print(driver.title)
#
# driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/a").click()
# time.sleep(1)
#
# driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[3]/nav/button[1]").click()
# time.sleep(3)
#
# for i in range(1, 300):
#     traks = driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]")
#     but_del = driver.find_element("xpath", "/html/body/div[1]/div[9]/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[3]/div[3]/div[1]/button")
#     hov = ActionChains(driver).move_to_element(traks).click(but_del)
#     hov.perform()
#     print("Delete: ", i)
