from app.sniff import Sniff

if __name__ == '__main__':
    url = 'http://honorsprogram.gwublogs.com/2017/11/08/honorsproblems-ive-messed-up-everything-oh-no/'
    url2 = "https://www.wintellect.com/containerize-python-app-5-minutes/"
    url3 = "http://encouragementforeverydaystruggles.blogspot.com/"
    sd = Sniff(url3)
    ls = sd.fetch_data()
    print(ls)