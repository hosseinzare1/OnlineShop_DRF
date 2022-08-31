
# Online shop 

An online shop server side that implemented with django rest freamwork.


**This project is made for learning purpose and some codes and methods used are not implemented in the correct way** 


# API Reference

## Products list

### 1. Get products with special discounts

```http
  GET /api/v1/get_special_discounts/
```

### 2. Get bestselling products

```http
  GET /api/v1/get_bestselling/
```

### 3. Get groups

```http
  GET /api/v1/groups/
```

### 4. Get categories

```http
  GET /api/v1/categories/{group_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `group_id`| `Path - Int` | **Required**. Group id |


### 5. Get products of a specific category

```http
  GET /api/v1/get_products_by_category/{category}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category`| `Path - str`    | **Required**. Category name  |


### 6. Get products of a specific group

```http
  GET /api/v1/get_products_by_group/{group}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `group`      | `Path - str` | **Required**. Group name |



## Product detail

### 1. Get product detail

```http
  GET /api/v1/get_product/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |


### 2. Get product images

```http
  GET /api/v1/get_images/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |


### 3. Get product comments

```http
  GET /api/v1/get_comments/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |



### 4. Get product attributes

```http
  GET /api/v1/get_product_attributes/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Product id   |


## Comments



### 1. Get all comments of a user

```http
  GET /api/v1/get_user_comments/{user_number}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` | `Path - Int`   | **Required**. User id |



### 2. Submit comment

```http
  Post /api/v1/submit_comment/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `comment`      | `body`    | **Required**. Comment body  |

### 3. Delete comments

```http
  POST /api/v1/delete_comment/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Comment id  |


### 4. Edit comment

```http
  POST /api/v1/edit_comment/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Path - Int`    | **Required**. Comment id   |




## Order

### 1. Submit Order

```http
  POST /api/v1/submit_comment/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `comment` | `body`   | **Required**. Order body          |


### 2. Get orders of a user

```http
  GET /api/v1/get_orders/{user_number}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_number` | `Path - Int`| **Required**.User number  |


### 3. Get order detail

```http
  GET /api/v1/get_order_details/{order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`| `Path - Int`    | **Required**. Order id  |



