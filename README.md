# StripePR

## Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
1. Django Модель Item с полями (name, description, price) 
2. API с двумя методами:
    - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

## Проект доступен
```
http://stripepj.ddns.net/item/1/
```

## Данные для входа в admin

```
login: rt
password: 1
```
