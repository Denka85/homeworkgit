# My bank
## Программа на Python для работы с банковскими картами

## Описание проекта

Данный проект представляет собой виджет (или модуль) для работы с банковскими операциями клиентов.
Цель — фильтрация и сортировка списка банковских операций на языке Python с использованием
рекомендаций PEP 8, GitFlow и классических инструментов код-ревью (Pull Request на GitHub).

## Основные возможности

**Функция маскировки номера
функция `get_mask_card_number`
 принимает на вход номер карты в виде числа и возвращает маску номера по правилу 
XXXX XX** **** XXXX
 
функция `get_mask_account`
 принимает на вход номер счета в виде числа и возвращает маску номера по правилу 
**XXXX


1. **Фильтрация по статусу операции**  
   Функция `filter_by_state` позволяет получить только те операции, у которых ключ `state` соответствует
   нужному значению (по умолчанию `'EXECUTED'`).

2. **Сортировка по дате**  
   Функция `sort_by_date` сортирует операции по убыванию (самые последние операции — первыми) либо
   по возрастанию (если передать параметр `descending=False`).

   ## Установка и настройка

1. Склонируйте репозиторий (или скачайте, форкните, если требуется):
   ```bash
   git clone 
   https://github.com/Denka85/homeworkgit/
   
2. запустите фаил homeworkgit\tets\main.py 
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |

