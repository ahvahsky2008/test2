Итак. Я создал 3 endpoint, каждый из которых возвращает свой диапазон json

'http://localhost:5555/url1' возвращает 1-10,31-40 
'http://localhost:5555/url2' 11-20,41-50
'http://localhost:5555/url3' 21-30,51-60

Есть основной endpoint / который непосредственно и обращается ассинхронно ко всем 3 endpoint, аккумулирует данные, сортирует по id и вы даёт в виде json. Всё в принципе получилось, кроме обработки таймаута в 2сек. 

Чтобы увидеть результат просто перейдите по ссылке http://localhost:5555