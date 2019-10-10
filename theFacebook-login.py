import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')]
browser.open('https://www.linkedin.com/')
browser.select_form(nr=0)
browser.form['username']="viniciuspoa2@hotmail.com"
browser.form['password']="sesbdv7t10"
submit =  browser.submit()
print(submit.geturl())
