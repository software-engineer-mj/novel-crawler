# novel-crawler

크롬 드라이브를 사용하여 [문피아](https://www.munpia.com)에서 소설을 다운받아서 텍스트 파일로 저장하는 간단한 크롤러 예제 코드입니다.

설정한 소설 장르에서 가장 최신 작품을 ```novels``` 폴더에 다운받는 프로그램입니다.

#### 1. 설정하기

사용하고 있는 운영체제에 따라서 config.json 파일을 수정합니다.

operating_system에는 사용하고 있는 운영체제를 ```"linux64"``` 또는 ```"mac64"```를 넣습니다.

website_url은 문피아에서 제공하는 "무료 웹 소설" 링크입니다.

genres는 다운받을 소설 장르 목록입니다.

```
{
    "operating_system": "linux64",
    "website_url": "http://novel.munpia.com/page/hd.novel/group/nv.regular",
    "genres": ["로맨스", "무협", "현대판타지", "일반소설"]
}
```

#### 2. 설치하기

```
$ sudo pip3 install selenium
```

#### 3. 실행하기

```
$ python3 crawler.py
```