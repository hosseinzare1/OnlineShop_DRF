
# Online shop 

An online shop server side that implemented with django rest freamwork.


**This project is made for learning purpose and some codes and methods used are not implemented in the correct way** 

# UML Diagram
![UML](https://github.com/hosseinzare1/OnlineShop_DRF/blob/master/UML.png)
# API Reference

## Products list

### 1. Get products with special discounts

```
  GET /api/v1/get_special_discounts/
```

### 2. Get bestselling products

```
  GET /api/v1/get_bestselling/
```

### 3. Get groups

```
  GET /api/v1/groups/
```

### 4. Get categories

```
  GET /api/v1/categories/{group_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `group_id`| `Path - Int` | **Required**. Group id |


### 5. Get products of a specific category

```
  GET /api/v1/get_products_by_category/{category}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category`| `Path - str`    | **Required**. Category name  |


### 6. Get products of a specific group

```
  GET /api/v1/get_products_by_group/{group}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `group`      | `Path - str` | **Required**. Group name |



## Product detail

### 1. Get product detail

```
  GET /api/v1/get_product/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |


### 2. Get product images

```
  GET /api/v1/get_images/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |


### 3. Get product comments

```
  GET /api/v1/get_comments/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |



### 4. Get product attributes

```
  GET /api/v1/get_product_attributes/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |


## Comments



### 1. Get all comments of a user

```
  GET /api/v1/get_user_comments/{user_number}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` | `Path - Int`   | **Required**. User id |



### 2. Submit comment

```
  Post /api/v1/submit_comment/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `comment`      | `body`    | **Required**. Comment body  |

### 3. Delete comments

```
  POST /api/v1/delete_comment/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Comment id  |


### 4. Edit comment

```
  POST /api/v1/edit_comment/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Comment id   |




## Order

### 1. Submit Order

```
  POST /api/v1/submit_comment/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `comment` | `body`   | **Required**. Order body          |


### 2. Get orders of a user

```
  GET /api/v1/get_orders/{user_number}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_number` | `Path - Int`| **Required**.User number  |


### 3. Get order detail

```
  GET /api/v1/get_order_details/{order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`| `Path - Int`    | **Required**. Order id  |



